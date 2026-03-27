#!/usr/bin/env python3
"""
SQL Server Performance Monitoring Dashboard
============================================
Real-time performance monitoring dashboard for dpa_EDSAdmin database.

Features:
- Real-time metrics (auto-refresh every 30 seconds)
- Hourly trends (last 24 hours)
- Top performance issues (last 7 days)
- Index implementation tracking
- Interactive charts and visualizations

Requirements:
    pip install streamlit plotly pandas pyodbc python-dotenv

Usage:
    streamlit run dashboard.py

    # Custom port:
    streamlit run dashboard.py --server.port 8080

    # Custom database:
    streamlit run dashboard.py -- --database dpa_EDSAdmin

Environment Variables (.env):
    DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com,1433
    DB_USERNAME=your_username
    DB_PASSWORD=your_password

Author: DBA Team
Created: 2025-12-04
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pyodbc
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import time

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

# Page configuration
st.set_page_config(
    page_title="SQL Server Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .critical { color: #ff4b4b; font-weight: bold; }
    .high { color: #ffa500; font-weight: bold; }
    .good { color: #00cc00; font-weight: bold; }
    .stMetric label { font-size: 14px !important; }
    .stMetric value { font-size: 28px !important; }
</style>
""", unsafe_allow_html=True)

# Database connection
@st.cache_resource
def get_connection():
    """Create database connection with caching."""
    try:
        server = os.getenv('DB_SERVER')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        database = 'dpa_EDSAdmin'

        if not all([server, username, password]):
            st.error("Missing database credentials in .env file")
            return None

        # Detect best available driver
        drivers = [d for d in pyodbc.drivers() if 'SQL Server' in d]
        if not drivers:
            st.error("No SQL Server ODBC driver found")
            return None

        driver = drivers[0]

        conn_str = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=yes"
        )

        conn = pyodbc.connect(conn_str, timeout=30)
        return conn

    except Exception as e:
        st.error(f"Database connection error: {str(e)}")
        return None

def execute_query(query, conn):
    """Execute query and return DataFrame."""
    try:
        return pd.read_sql(query, conn)
    except Exception as e:
        st.error(f"Query execution error: {str(e)}")
        return pd.DataFrame()

# Data fetching functions
def get_health_score(conn):
    """Calculate overall database health score."""
    query = """
    DECLARE @NewHighImpactIndexes INT
    DECLARE @TotalBlockingHours DECIMAL(10,2)
    DECLARE @HighLatencyCount INT
    DECLARE @SlowQueryCount INT
    DECLARE @HealthScore INT = 100

    -- New high-impact missing indexes
    SELECT @NewHighImpactIndexes = COUNT(*)
    FROM CON_WHATIF_SRC_1
    WHERE D >= DATEADD(day, -1, GETDATE())
        AND EST_SAVING > 95;

    -- Blocking events
    SELECT
        @TotalBlockingHours = CAST(SUM(BLEETIMESECS) / 3600.0 AS DECIMAL(10,2))
    FROM CON_BLOCKING_SUM_1
    WHERE DATEHOUR >= DATEADD(day, -1, GETDATE())
        AND BLEETIMESECS > 60;

    -- I/O latency events
    SELECT @HighLatencyCount = COUNT(*)
    FROM CON_IO_DETAIL_1
    WHERE D >= DATEADD(day, -1, GETDATE())
        AND READ_LATENCY > 100;

    -- Slow queries
    SELECT @SlowQueryCount = COUNT(DISTINCT SQL_HASH)
    FROM CON_QUERY_PLAN_1
    WHERE D >= DATEADD(day, -1, GETDATE())
        AND SQL_BUFFER_GETS > 10000000;

    -- Calculate health score (use ELSE IF to prevent double-penalty)
    IF @NewHighImpactIndexes > 10 SET @HealthScore = @HealthScore - 20
    ELSE IF @NewHighImpactIndexes > 5 SET @HealthScore = @HealthScore - 10

    IF @TotalBlockingHours > 5 SET @HealthScore = @HealthScore - 25
    ELSE IF @TotalBlockingHours > 1 SET @HealthScore = @HealthScore - 10

    IF @HighLatencyCount > 100 SET @HealthScore = @HealthScore - 25
    ELSE IF @HighLatencyCount > 50 SET @HealthScore = @HealthScore - 15

    IF @SlowQueryCount > 20 SET @HealthScore = @HealthScore - 20
    ELSE IF @SlowQueryCount > 10 SET @HealthScore = @HealthScore - 10

    SELECT
        @HealthScore as HealthScore,
        @NewHighImpactIndexes as NewIndexes,
        ISNULL(@TotalBlockingHours, 0) as BlockingHours,
        @HighLatencyCount as HighLatencyEvents,
        @SlowQueryCount as SlowQueries
    """
    return execute_query(query, conn)

def get_missing_indexes_trend(conn, days=7):
    """Get missing index recommendations trend."""
    query = f"""
    SELECT
        CAST(D AS DATE) as Date,
        COUNT(*) as TotalRecommendations,
        SUM(CASE WHEN EST_SAVING > 95 THEN 1 ELSE 0 END) as Critical,
        SUM(CASE WHEN EST_SAVING BETWEEN 80 AND 95 THEN 1 ELSE 0 END) as High,
        SUM(CASE WHEN EST_SAVING BETWEEN 50 AND 80 THEN 1 ELSE 0 END) as Medium
    FROM CON_WHATIF_SRC_1
    WHERE D >= DATEADD(day, -{days}, GETDATE())
    GROUP BY CAST(D AS DATE)
    ORDER BY Date
    """
    return execute_query(query, conn)

def get_blocking_trend(conn, hours=24):
    """Get blocking events trend."""
    query = f"""
    SELECT
        DATEADD(hour, DATEDIFF(hour, 0, DATEHOUR), 0) as Hour,
        COUNT(*) as BlockingEvents,
        CAST(SUM(BLEETIMESECS) / 60.0 AS DECIMAL(10,2)) as TotalBlockeeMinutes,
        CAST(MAX(BLEETIMESECS) / 60.0 AS DECIMAL(10,2)) as MaxBlockeeMinutes
    FROM CON_BLOCKING_SUM_1
    WHERE DATEHOUR >= DATEADD(hour, -{hours}, GETDATE())
        AND BLEETIMESECS > 60
    GROUP BY DATEADD(hour, DATEDIFF(hour, 0, DATEHOUR), 0)
    ORDER BY Hour
    """
    return execute_query(query, conn)

def get_io_latency_trend(conn, hours=24):
    """Get I/O latency trend."""
    query = f"""
    SELECT
        DATEADD(hour, DATEDIFF(hour, 0, D), 0) as Hour,
        CAST(AVG(READ_LATENCY) AS DECIMAL(10,2)) as AvgReadLatency,
        CAST(AVG(WRITE_LATENCY) AS DECIMAL(10,2)) as AvgWriteLatency,
        CAST(MAX(READ_LATENCY) AS DECIMAL(10,2)) as MaxReadLatency,
        CAST(MAX(WRITE_LATENCY) AS DECIMAL(10,2)) as MaxWriteLatency
    FROM CON_IO_DETAIL_1
    WHERE D >= DATEADD(hour, -{hours}, GETDATE())
    GROUP BY DATEADD(hour, DATEDIFF(hour, 0, D), 0)
    ORDER BY Hour
    """
    return execute_query(query, conn)

def get_top_missing_indexes(conn, limit=10):
    """Get top missing index recommendations."""
    query = f"""
    SELECT TOP {limit}
        CONVERT(VARCHAR, w.D, 120) as DateIdentified,
        w.EST_SAVING as EstSavingPercent,
        w.SQL_EXECS as Executions,
        fq.ODATABASE as DatabaseName,
        fq.OSCHEMA + '.' + fq.ONAME as TableName,
        fq.OINDEX_COLUMNS as IndexColumns
    FROM CON_WHATIF_SRC_1 w
    LEFT JOIN CON_FQ_OBJECT_1 fq ON w.IDX_ID = fq.ID
    WHERE w.D >= DATEADD(day, -7, GETDATE())
        AND w.EST_SAVING >= 90
    ORDER BY w.EST_SAVING DESC, w.SQL_EXECS DESC
    """
    return execute_query(query, conn)

def get_top_blocking_events(conn, limit=10):
    """Get top blocking events."""
    query = f"""
    SELECT TOP {limit}
        CONVERT(VARCHAR, bs.DATEHOUR, 120) as DateTime,
        CASE bs.DIMENSIONTYPE
            WHEN 'P' THEN 'Program'
            WHEN 'D' THEN 'Database'
            WHEN 'E' THEN 'Event'
            ELSE 'Unknown'
        END as Type,
        m.NAME as Entity,
        CAST(bs.BLEETIMESECS / 60.0 AS DECIMAL(10,2)) as BlockeeMinutes
    FROM CON_BLOCKING_SUM_1 bs
    LEFT JOIN CONM_1 m ON bs.DIMENSIONID = m.ID
    WHERE bs.DATEHOUR >= DATEADD(day, -7, GETDATE())
        AND bs.BLEETIMESECS > 60
    ORDER BY bs.BLEETIMESECS DESC
    """
    return execute_query(query, conn)

def get_slow_queries(conn, limit=10):
    """Get slowest queries by buffer gets."""
    query = f"""
    SELECT TOP {limit}
        CONVERT(VARCHAR, qp.D, 120) as DateTime,
        qp.SQL_HASH as QueryHash,
        CAST(qp.SQL_BUFFER_GETS / 1000000.0 AS DECIMAL(10,2)) as BufferGetsMillions,
        qp.SQL_EXECS as Executions,
        CAST(qp.SQL_ELAPSED_TIME / 1000.0 AS DECIMAL(10,2)) as ElapsedSeconds
    FROM CON_QUERY_PLAN_1 qp
    WHERE qp.D >= DATEADD(day, -7, GETDATE())
        AND qp.SQL_BUFFER_GETS > 10000000
    ORDER BY qp.SQL_BUFFER_GETS DESC
    """
    return execute_query(query, conn)

# Main dashboard
def main():
    """Main dashboard application."""

    # Sidebar
    st.sidebar.title("⚙️ Settings")
    auto_refresh = st.sidebar.checkbox("Auto-refresh (30s)", value=True)
    refresh_interval = st.sidebar.slider("Refresh interval (seconds)", 10, 300, 30)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Dashboard Sections")
    show_health = st.sidebar.checkbox("Health Score", value=True)
    show_indexes = st.sidebar.checkbox("Missing Indexes", value=True)
    show_blocking = st.sidebar.checkbox("Blocking Events", value=True)
    show_io = st.sidebar.checkbox("I/O Latency", value=True)
    show_queries = st.sidebar.checkbox("Slow Queries", value=True)

    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📁 Quick Links")
    st.sidebar.markdown("- [Performance Guide](docs/guides/DAILY_MONITORING_GUIDE.md)")
    st.sidebar.markdown("- [SQL Agent Jobs](scripts/sql_agent_jobs/)")
    st.sidebar.markdown("- [Alert Dashboard SQL](scripts/alert_dashboard.sql)")

    # Header
    st.title("📊 SQL Server Performance Dashboard")
    st.markdown(f"**dpa_EDSAdmin** | Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Get database connection
    conn = get_connection()
    if not conn:
        st.error("Failed to connect to database. Check credentials in .env file.")
        st.stop()

    # Health Score Section
    if show_health:
        st.markdown("## 🏥 Database Health Score")

        health_data = get_health_score(conn)
        if not health_data.empty:
            score = health_data['HealthScore'].iloc[0]
            new_indexes = health_data['NewIndexes'].iloc[0]
            blocking_hours = health_data['BlockingHours'].iloc[0]
            high_latency = health_data['HighLatencyEvents'].iloc[0]
            slow_queries = health_data['SlowQueries'].iloc[0]

            # Status color
            if score >= 90:
                status = "EXCELLENT"
                status_color = "good"
            elif score >= 75:
                status = "GOOD"
                status_color = "good"
            elif score >= 60:
                status = "FAIR"
                status_color = "high"
            elif score >= 40:
                status = "POOR"
                status_color = "high"
            else:
                status = "CRITICAL"
                status_color = "critical"

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric(
                    "Health Score",
                    f"{score}/100",
                    delta=None,
                    help="Overall database health (0-100)"
                )
                st.markdown(f"<p class='{status_color}'>Status: {status}</p>", unsafe_allow_html=True)

            with col2:
                st.metric(
                    "New Indexes",
                    new_indexes,
                    delta=None,
                    help="High-impact missing indexes (>95% improvement)"
                )

            with col3:
                st.metric(
                    "Blocking",
                    f"{blocking_hours:.1f}h",
                    delta=None,
                    help="Total blocking hours (last 24h)"
                )

            with col4:
                st.metric(
                    "High I/O Latency",
                    high_latency,
                    delta=None,
                    help="Events >100ms (last 24h)"
                )

            with col5:
                st.metric(
                    "Slow Queries",
                    slow_queries,
                    delta=None,
                    help="Queries >10M buffer gets"
                )

        st.markdown("---")

    # Missing Indexes Section
    if show_indexes:
        st.markdown("## 📇 Missing Index Recommendations")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("### Trend (Last 7 Days)")
            trend_data = get_missing_indexes_trend(conn, days=7)

            if not trend_data.empty:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=trend_data['Date'],
                    y=trend_data['Critical'],
                    name='Critical (>95%)',
                    mode='lines+markers',
                    line=dict(color='red', width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=trend_data['Date'],
                    y=trend_data['High'],
                    name='High (80-95%)',
                    mode='lines+markers',
                    line=dict(color='orange', width=3)
                ))
                fig.add_trace(go.Scatter(
                    x=trend_data['Date'],
                    y=trend_data['Medium'],
                    name='Medium (50-80%)',
                    mode='lines+markers',
                    line=dict(color='yellow', width=3)
                ))

                fig.update_layout(
                    height=300,
                    margin=dict(l=0, r=0, t=0, b=0),
                    xaxis_title="Date",
                    yaxis_title="Count",
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )

                st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### Top 10 Recommendations")
            top_indexes = get_top_missing_indexes(conn, limit=10)

            if not top_indexes.empty:
                st.dataframe(
                    top_indexes[['DatabaseName', 'TableName', 'EstSavingPercent', 'Executions']],
                    hide_index=True,
                    height=300
                )

        st.markdown("---")

    # Blocking Events Section
    if show_blocking:
        st.markdown("## 🚫 Blocking Events")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("### Hourly Trend (Last 24 Hours)")
            blocking_trend = get_blocking_trend(conn, hours=24)

            if not blocking_trend.empty:
                fig = make_subplots(specs=[[{"secondary_y": True}]])

                fig.add_trace(
                    go.Bar(
                        x=blocking_trend['Hour'],
                        y=blocking_trend['BlockingEvents'],
                        name='Event Count',
                        marker_color='lightblue'
                    ),
                    secondary_y=False
                )

                fig.add_trace(
                    go.Scatter(
                        x=blocking_trend['Hour'],
                        y=blocking_trend['TotalBlockeeMinutes'],
                        name='Total Minutes',
                        mode='lines+markers',
                        line=dict(color='red', width=3)
                    ),
                    secondary_y=True
                )

                fig.update_layout(
                    height=300,
                    margin=dict(l=0, r=0, t=0, b=0),
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                )

                fig.update_xaxes(title_text="Hour")
                fig.update_yaxes(title_text="Event Count", secondary_y=False)
                fig.update_yaxes(title_text="Total Minutes", secondary_y=True)

                st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### Top 10 Events")
            top_blocking = get_top_blocking_events(conn, limit=10)

            if not top_blocking.empty:
                st.dataframe(
                    top_blocking[['Type', 'Entity', 'BlockeeMinutes']],
                    hide_index=True,
                    height=300
                )

        st.markdown("---")

    # I/O Latency Section
    if show_io:
        st.markdown("## 💾 I/O Latency")

        st.markdown("### Hourly Trend (Last 24 Hours)")
        io_trend = get_io_latency_trend(conn, hours=24)

        if not io_trend.empty:
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=io_trend['Hour'],
                y=io_trend['AvgReadLatency'],
                name='Avg Read',
                mode='lines',
                line=dict(color='blue', width=2)
            ))

            fig.add_trace(go.Scatter(
                x=io_trend['Hour'],
                y=io_trend['AvgWriteLatency'],
                name='Avg Write',
                mode='lines',
                line=dict(color='green', width=2)
            ))

            fig.add_trace(go.Scatter(
                x=io_trend['Hour'],
                y=io_trend['MaxReadLatency'],
                name='Max Read',
                mode='lines',
                line=dict(color='red', width=2, dash='dot')
            ))

            # Add threshold lines
            fig.add_hline(y=100, line_dash="dash", line_color="orange",
                         annotation_text="High Threshold (100ms)")
            fig.add_hline(y=200, line_dash="dash", line_color="red",
                         annotation_text="Critical Threshold (200ms)")

            fig.update_layout(
                height=400,
                margin=dict(l=0, r=0, t=0, b=0),
                xaxis_title="Hour",
                yaxis_title="Latency (ms)",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )

            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

    # Slow Queries Section
    if show_queries:
        st.markdown("## 🐌 Slow Queries")

        st.markdown("### Top 10 by Buffer Gets (Last 7 Days)")
        slow_queries_data = get_slow_queries(conn, limit=10)

        if not slow_queries_data.empty:
            st.dataframe(
                slow_queries_data,
                hide_index=True,
                height=400
            )

        st.markdown("---")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>SQL Server Performance Dashboard | DBA Team</p>
        <p>Data source: dpa_EDSAdmin | Refresh: Auto (30s)</p>
    </div>
    """, unsafe_allow_html=True)

    # Auto-refresh
    if auto_refresh:
        time.sleep(refresh_interval)
        st.rerun()

if __name__ == "__main__":
    main()
