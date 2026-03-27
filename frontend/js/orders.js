// Order fetching, display, and detail view
function ordersModule() {
    return {
        orders: [],
        orderCount: 0,
        ordersLoading: false,
        ordersError: '',
        ordersTab: 'all',
        showOrderDetail: false,
        selectedOrder: null,
        orderDetailItems: [],
        orderDetailLoading: false,
        pendingApprovalCount: 0,

        // NOTE: filteredOrders getter lives in app.js (getters can't survive spread)

        async fetchOrders() {
            const sid = this._getSessionId();
            if (!sid) return;
            this.ordersLoading = true;
            this.ordersError = '';
            try {
                const r = await fetch('/api/requisitions?session_id=' + encodeURIComponent(sid));
                if (r.ok) {
                    const d = await r.json();
                    this.orders = d.items || d.requisitions || d || [];
                    this.orderCount = this.orders.filter(o => !['Fulfilled', 'Cancelled', 'Rejected'].includes(o.status)).length;
                } else {
                    this.orders = [];
                    this.orderCount = 0;
                }
            } catch (e) {
                console.error('Orders fetch error:', e);
                this.orders = [];
                this.orderCount = 0;
            } finally {
                this.ordersLoading = false;
            }
        },

        async openOrderDetail(order) {
            this.selectedOrder = order;
            this.orderDetailItems = [];
            this.orderDetailLoading = true;
            this.showOrderDetail = true;
            const sid = this._getSessionId();
            try {
                const r = await fetch('/api/requisitions/' + encodeURIComponent(order.requisition_id) + '/items?session_id=' + encodeURIComponent(sid));
                if (r.ok) {
                    this.orderDetailItems = await r.json();
                }
            } catch (e) { console.error('Order detail fetch error:', e); }
            finally { this.orderDetailLoading = false; }
        }
    };
}
