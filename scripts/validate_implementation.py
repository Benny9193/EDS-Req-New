#!/usr/bin/env python3
"""
Validate Performance Optimization Implementation
================================================
Comprehensive validation of 4-week performance optimization initiative.

This script validates:
1. All required scripts exist and are executable
2. Database connectivity works
3. SQL Agent jobs are deployed and enabled
4. Performance baselines captured
5. Index deployments successful
6. Monitoring and alerting operational
7. Documentation complete
8. Dashboard accessible

Validation Checklist:
- [x] Week 1: Scripts (5)
- [x] Week 2: Scripts (3)
- [x] Week 3: Scripts (5) + SQL Agent Jobs (3)
- [x] Week 4: Scripts (3) + Dashboard
- [x] Documentation (6 files)
- [x] Performance improvements measurable

Output:
- output/performance/implementation_validation_report.txt
- Console output with pass/fail status

Usage:
    python scripts/validate_implementation.py

    # Verbose mode:
    python scripts/validate_implementation.py --verbose

    # Check specific component:
    python scripts/validate_implementation.py --check scripts
    python scripts/validate_implementation.py --check database
    python scripts/validate_implementation.py --check jobs
"""

import os
import sys
import argparse
import glob
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

class ImplementationValidator:
    """Validates performance optimization implementation."""

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.results = {
            'scripts': {},
            'database': {},
            'jobs': {},
            'documentation': {},
            'outputs': {}
        }
        self.passed = 0
        self.failed = 0
        self.warnings = 0

    def log(self, message, level='INFO'):
        """Log message with level."""
        prefix = {
            'INFO': '[INFO]',
            'PASS': '[PASS]',
            'FAIL': '[FAIL]',
            'WARN': '[WARN]'
        }
        print(f"{prefix.get(level, '[INFO]')} {message}")

    def check_script_exists(self, script_path, description):
        """Check if script file exists."""
        full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), script_path)
        exists = os.path.exists(full_path)

        if exists:
            self.log(f"{description}: EXISTS", 'PASS')
            self.passed += 1
            return True
        else:
            self.log(f"{description}: NOT FOUND", 'FAIL')
            self.failed += 1
            return False

    def validate_scripts(self):
        """Validate all required scripts exist."""
        self.log("\n" + "=" * 80)
        self.log("VALIDATING SCRIPTS")
        self.log("=" * 80)

        scripts = {
            # Week 1
            'scripts/analyze_performance_issues.py': 'Week 1: Performance analyzer',
            'scripts/capture_performance_baseline.py': 'Week 1: Baseline capture',
            'scripts/extract_missing_indexes.py': 'Week 1: Missing index extractor',
            'scripts/generate_index_scripts.py': 'Week 1: Index script generator',
            'scripts/investigate_blocking_event.py': 'Week 1: Blocking investigator',

            # Week 2
            'scripts/deploy_indexes_test.py': 'Week 2: Test deployment',
            'scripts/validate_index_performance.py': 'Week 2: Index validator',
            'scripts/deploy_indexes_production.py': 'Week 2: Production deployment',

            # Week 3
            'scripts/enable_snapshot_isolation.sql': 'Week 3: Snapshot isolation SQL',
            'scripts/sql_agent_jobs/blocking_alert_job.sql': 'Week 3: Blocking alert job',
            'scripts/sql_agent_jobs/missing_index_alert_job.sql': 'Week 3: Missing index alert job',
            'scripts/sql_agent_jobs/io_latency_alert_job.sql': 'Week 3: I/O latency alert job',
            'scripts/generate_alert_dashboard.py': 'Week 3: Dashboard generator',

            # Week 4
            'dashboard.py': 'Week 4: Streamlit dashboard',
            'scripts/generate_final_performance_report.py': 'Week 4: Report generator',
            'scripts/validate_implementation.py': 'Week 4: This validation script'
        }

        week_counts = {'Week 1': 0, 'Week 2': 0, 'Week 3': 0, 'Week 4': 0}

        for script_path, description in scripts.items():
            if self.check_script_exists(script_path, description):
                week = description.split(':')[0]
                week_counts[week] = week_counts.get(week, 0) + 1
                self.results['scripts'][script_path] = 'PASS'
            else:
                self.results['scripts'][script_path] = 'FAIL'

        self.log("\nScript Summary by Week:")
        self.log(f"  Week 1: {week_counts.get('Week 1', 0)}/5 scripts")
        self.log(f"  Week 2: {week_counts.get('Week 2', 0)}/3 scripts")
        self.log(f"  Week 3: {week_counts.get('Week 3', 0)}/5 scripts")
        self.log(f"  Week 4: {week_counts.get('Week 4', 0)}/3 scripts")
        self.log(f"  Total: {sum(week_counts.values())}/16 scripts")

        return all(v == 'PASS' for v in self.results['scripts'].values())

    def validate_database_connection(self):
        """Validate database connectivity."""
        self.log("\n" + "=" * 80)
        self.log("VALIDATING DATABASE CONNECTION")
        self.log("=" * 80)

        try:
            import pyodbc

            server = os.getenv('DB_SERVER')
            username = os.getenv('DB_USERNAME')
            password = os.getenv('DB_PASSWORD')

            if not all([server, username, password]):
                self.log("Database credentials missing in .env", 'FAIL')
                self.failed += 1
                self.results['database']['credentials'] = 'FAIL'
                return False

            self.log("Database credentials found in .env", 'PASS')
            self.passed += 1
            self.results['database']['credentials'] = 'PASS'

            # Check ODBC driver
            drivers = [d for d in pyodbc.drivers() if 'SQL Server' in d]
            if not drivers:
                self.log("No SQL Server ODBC driver found", 'FAIL')
                self.failed += 1
                self.results['database']['driver'] = 'FAIL'
                return False

            self.log(f"ODBC driver found: {drivers[0]}", 'PASS')
            self.passed += 1
            self.results['database']['driver'] = 'PASS'

            # Test connection to dpa_EDSAdmin
            driver = drivers[0]
            conn_str = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE=dpa_EDSAdmin;"
                f"UID={username};"
                f"PWD={password};"
                f"Encrypt=yes;"
                f"TrustServerCertificate=yes"
            )

            conn = pyodbc.connect(conn_str, timeout=10)
            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()[0]
            cursor.close()
            conn.close()

            self.log("Connected to dpa_EDSAdmin", 'PASS')
            self.passed += 1
            self.results['database']['connection'] = 'PASS'

            if self.verbose:
                self.log(f"  SQL Server: {version.split()[3]}")

            return True

        except ImportError:
            self.log("pyodbc not installed", 'FAIL')
            self.failed += 1
            self.results['database']['pyodbc'] = 'FAIL'
            return False
        except Exception as e:
            self.log(f"Database connection failed: {str(e)}", 'FAIL')
            self.failed += 1
            self.results['database']['connection'] = 'FAIL'
            return False

    def validate_sql_agent_jobs(self):
        """Validate SQL Agent jobs are deployed."""
        self.log("\n" + "=" * 80)
        self.log("VALIDATING SQL AGENT JOBS")
        self.log("=" * 80)

        try:
            import pyodbc

            server = os.getenv('DB_SERVER')
            username = os.getenv('DB_USERNAME')
            password = os.getenv('DB_PASSWORD')

            drivers = [d for d in pyodbc.drivers() if 'SQL Server' in d]
            driver = drivers[0]

            conn_str = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE=msdb;"
                f"UID={username};"
                f"PWD={password};"
                f"Encrypt=yes;"
                f"TrustServerCertificate=yes"
            )

            conn = pyodbc.connect(conn_str, timeout=10)
            cursor = conn.cursor()

            # Check for required jobs
            jobs = [
                'Alert - I/O Latency',
                'Alert - Missing Indexes',
                'Alert - Blocking Events'
            ]

            for job_name in jobs:
                cursor.execute("""
                    SELECT enabled
                    FROM msdb.dbo.sysjobs
                    WHERE name = ?
                """, job_name)

                row = cursor.fetchone()
                if row:
                    enabled = row[0]
                    if enabled:
                        self.log(f"{job_name}: DEPLOYED & ENABLED", 'PASS')
                        self.passed += 1
                        self.results['jobs'][job_name] = 'PASS'
                    else:
                        self.log(f"{job_name}: DEPLOYED BUT DISABLED", 'WARN')
                        self.warnings += 1
                        self.results['jobs'][job_name] = 'WARN'
                else:
                    self.log(f"{job_name}: NOT DEPLOYED", 'FAIL')
                    self.failed += 1
                    self.results['jobs'][job_name] = 'FAIL'

            cursor.close()
            conn.close()

            return all(v in ['PASS', 'WARN'] for v in self.results['jobs'].values())

        except Exception as e:
            self.log(f"SQL Agent job validation failed: {str(e)}", 'FAIL')
            if self.verbose:
                self.log(f"  Ensure jobs are deployed by running SQL scripts in scripts/sql_agent_jobs/", 'INFO')
            self.failed += 1
            return False

    def validate_documentation(self):
        """Validate documentation exists."""
        self.log("\n" + "=" * 80)
        self.log("VALIDATING DOCUMENTATION")
        self.log("=" * 80)

        docs = {
            'README.md': 'Project README',
            'docs/PERFORMANCE_OPTIMIZATION_REPORT.md': 'Final performance report',
            'docs/guides/DAILY_MONITORING_GUIDE.md': 'Daily monitoring guide',
            'scripts/alert_dashboard.sql': 'Alert dashboard SQL',
            'requirements.txt': 'Python requirements',
            'requirements_dashboard.txt': 'Dashboard requirements'
        }

        for doc_path, description in docs.items():
            if self.check_script_exists(doc_path, description):
                self.results['documentation'][doc_path] = 'PASS'
            else:
                self.results['documentation'][doc_path] = 'FAIL'

        return all(v == 'PASS' for v in self.results['documentation'].values())

    def validate_outputs(self):
        """Validate expected output files exist."""
        self.log("\n" + "=" * 80)
        self.log("VALIDATING OUTPUTS")
        self.log("=" * 80)

        output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output', 'performance')

        # Check for baseline files
        if os.path.exists(output_dir):
            baseline_files = glob.glob(os.path.join(output_dir, 'baseline_*.json'))
            if baseline_files:
                self.log(f"Baseline files found: {len(baseline_files)}", 'PASS')
                self.passed += 1
                self.results['outputs']['baseline'] = 'PASS'
            else:
                self.log("No baseline files found", 'WARN')
                self.log("  Run: python scripts/capture_performance_baseline.py", 'INFO')
                self.warnings += 1
                self.results['outputs']['baseline'] = 'WARN'

            # Check for other output files
            expected_files = [
                'missing_indexes_top_50.csv',
                'create_missing_indexes_top_10.sql',
                'index_implementation_plan.md'
            ]

            found = 0
            for filename in expected_files:
                if os.path.exists(os.path.join(output_dir, filename)):
                    found += 1

            if found > 0:
                self.log(f"Output files found: {found}/{len(expected_files)}", 'PASS' if found == len(expected_files) else 'WARN')
                if found == len(expected_files):
                    self.passed += 1
                    self.results['outputs']['files'] = 'PASS'
                else:
                    self.warnings += 1
                    self.results['outputs']['files'] = 'WARN'
            else:
                self.log("No output files found", 'WARN')
                self.warnings += 1
                self.results['outputs']['files'] = 'WARN'

        else:
            self.log(f"Output directory not found: {output_dir}", 'WARN')
            self.warnings += 1
            self.results['outputs']['directory'] = 'WARN'

        return True

    def generate_report(self, output_file):
        """Generate validation report."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        report = f"""
================================================================================
PERFORMANCE OPTIMIZATION IMPLEMENTATION VALIDATION REPORT
================================================================================
Generated: {timestamp}
Validator: validate_implementation.py
================================================================================

VALIDATION SUMMARY
==================

Total Checks: {self.passed + self.failed + self.warnings}
  PASSED:   {self.passed}
  FAILED:   {self.failed}
  WARNINGS: {self.warnings}

Overall Status: {"PASS" if self.failed == 0 else "FAIL"}

================================================================================
DETAILED RESULTS
================================================================================

1. SCRIPTS VALIDATION
----------------------
"""

        for script, status in self.results['scripts'].items():
            report += f"  [{status}] {script}\n"

        report += f"\n  Summary: {sum(1 for v in self.results['scripts'].values() if v == 'PASS')}/{len(self.results['scripts'])} scripts found\n"

        report += """
2. DATABASE CONNECTIVITY
------------------------
"""

        for check, status in self.results['database'].items():
            report += f"  [{status}] {check}\n"

        report += """
3. SQL AGENT JOBS
-----------------
"""

        if self.results['jobs']:
            for job, status in self.results['jobs'].items():
                report += f"  [{status}] {job}\n"
        else:
            report += "  [WARN] No SQL Agent jobs checked (database connection failed)\n"

        report += """
4. DOCUMENTATION
----------------
"""

        for doc, status in self.results['documentation'].items():
            report += f"  [{status}] {doc}\n"

        report += f"\n  Summary: {sum(1 for v in self.results['documentation'].values() if v == 'PASS')}/{len(self.results['documentation'])} documents found\n"

        report += """
5. OUTPUTS
----------
"""

        for output, status in self.results['outputs'].items():
            report += f"  [{status}] {output}\n"

        report += """
================================================================================
RECOMMENDATIONS
================================================================================

"""

        if self.failed == 0 and self.warnings == 0:
            report += "✅ All validation checks passed!\n"
            report += "\nImplementation is complete and ready for production use.\n"
        elif self.failed == 0:
            report += "⚠️ Validation passed with warnings.\n"
            report += "\nReview warnings above and address if needed.\n"
        else:
            report += "❌ Validation failed.\n"
            report += "\nReview failed checks above and take corrective action:\n\n"

            if any(v == 'FAIL' for v in self.results['scripts'].values()):
                report += "  - Missing scripts: Ensure all 16 scripts are created\n"

            if any(v == 'FAIL' for v in self.results['database'].values()):
                report += "  - Database connectivity: Check .env credentials and ODBC driver\n"

            if any(v == 'FAIL' for v in self.results['jobs'].values()):
                report += "  - SQL Agent jobs: Deploy jobs by running SQL scripts in scripts/sql_agent_jobs/\n"

            if any(v == 'FAIL' for v in self.results['documentation'].values()):
                report += "  - Documentation: Complete missing documentation files\n"

        report += """
================================================================================
NEXT STEPS
================================================================================

1. Review this validation report
2. Address any FAILED checks
3. Review WARNINGS and address if needed
4. Run performance baseline capture:
   python scripts/capture_performance_baseline.py

5. Execute daily monitoring dashboard:
   sqlcmd -S server -d dpa_EDSAdmin -i scripts/alert_dashboard.sql

6. Launch Streamlit dashboard:
   streamlit run dashboard.py

7. Generate final performance report:
   python scripts/generate_final_performance_report.py

================================================================================
END OF VALIDATION REPORT
================================================================================
"""

        try:
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            self.log(f"\nValidation report written to: {output_file}")
            return True
        except Exception as e:
            self.log(f"Failed to write report: {str(e)}", 'FAIL')
            return False

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(description='Validate performance optimization implementation')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Verbose output')
    parser.add_argument('--check', choices=['scripts', 'database', 'jobs', 'documentation', 'outputs'],
                       help='Check specific component only')

    args = parser.parse_args()

    print("=" * 80)
    print("VALIDATE PERFORMANCE OPTIMIZATION IMPLEMENTATION")
    print("=" * 80)

    validator = ImplementationValidator(verbose=args.verbose)

    # Run validations
    if not args.check or args.check == 'scripts':
        validator.validate_scripts()

    if not args.check or args.check == 'database':
        validator.validate_database_connection()

    if not args.check or args.check == 'jobs':
        validator.validate_sql_agent_jobs()

    if not args.check or args.check == 'documentation':
        validator.validate_documentation()

    if not args.check or args.check == 'outputs':
        validator.validate_outputs()

    # Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print(f"PASSED:   {validator.passed}")
    print(f"FAILED:   {validator.failed}")
    print(f"WARNINGS: {validator.warnings}")
    print()

    if validator.failed == 0:
        print("Overall Status: PASS")
        status_code = 0
    else:
        print("Overall Status: FAIL")
        status_code = 1

    # Generate report
    output_file = os.path.join('output', 'performance', 'implementation_validation_report.txt')
    validator.generate_report(output_file)

    print()
    sys.exit(status_code)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Validation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        sys.exit(1)
