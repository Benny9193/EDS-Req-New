# EDS Universal Requisition - Frontend Concepts Walkthrough
**Prepared for: Gerard Livelli | Date: March 5, 2026**
**Prepared by: Connor Harrison**

---

## Overview

We have **6 frontend concepts** for the next iteration of the OES (Online Entry System). Each takes a different design approach while sharing the same Alpine.js + FastAPI architecture. This document compares them against Gerard's requirements for the Teams walkthrough.

---

## Gerard's Requirements Checklist

| Requirement | frontend/ | v2 | v3 | v4 | v5 | v6 | reimagined |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Filter by Bid | - | Yes | Yes | - | Yes | **Yes** | - |
| Filter by Vendor | Yes | Yes | Yes | Yes | Yes | **Yes** | Yes |
| Non-Amazon Layout | Partial | Yes | Yes | Yes | Yes | **Yes** | Yes |
| My Requisition Summary | Yes | Yes | Yes | Yes | Yes | **Yes** | - |
| Vendor Logo Scroll | - | Yes | - | - | Yes | **Yes** | - |
| Popular Products | Yes | Yes | Yes | Yes | Yes | **Yes** | Yes |
| Starter Orders by Bid/Role | - | - | - | - | - | **Yes** | - |

**Key Update**: `frontend-v6` is the **only version** that implements Starter Orders by bid/role (client-side templates). It also connects to bid-specific API endpoints (`/api/bids/:id/products`). The remaining gap is making starter orders API-backed rather than hardcoded.

---

## Concept-by-Concept Summary

### 1. `frontend/` - The Original (Production-Ready)

**Vibe**: Professional e-commerce platform (think Staples.com meets modern SaaS)

**Colors**: EDS Navy `#1c1a83` + Red accent `#b70c0d`
**Fonts**: Inter
**Tech**: Alpine.js + custom CSS design system, 18 JS modules, 4 HTML pages

**Strengths**:
- Most feature-complete: saved lists, bulk CSV import, recurring orders, AI chat sidebar, admin dashboard, product comparison, order history
- Full filter sidebar: category, vendor, status, price range with URL persistence
- Responsive with mobile search overlay and voice search
- Budget enforcement with soft/hard limits
- Modular architecture (easiest to extend)

**Weaknesses**:
- No bid-based filtering
- No vendor logo carousel
- Layout leans toward traditional e-commerce (sidebar + grid)
- Visual design is clean but conservative

**Best For**: If we want maximum functionality out of the box

---

### 2. `frontend-v2/` - Premium Dark SaaS

**Vibe**: Figma/Linear/Stripe dashboard (dark mode, neon accents)

**Colors**: Dark base `#0a0a0f` + Cyan `#06b6d4` + Purple `#a855f7`
**Fonts**: Plus Jakarta Sans + JetBrains Mono
**Tech**: Alpine.js + custom CSS design system, 6 pages

**Strengths**:
- **Bid selector dropdown** in header - filters entire catalog by bid/contract
- **Vendor marquee** - animated scrolling display of approved vendors per bid
- Dashboard-first: budget circular chart, orders this month, savings stats
- Quick Actions grid (Quick Order, Saved Lists, Recurring, Bulk Import)
- High-contrast dark theme stands out visually
- Glassmorphism effects feel premium

**Weaknesses**:
- Dark theme may not suit all users (no light mode toggle)
- Fewer pages/features than original
- No detailed filter sidebar for category/price
- Neon aesthetic might feel too "techy" for school staff

**Best For**: If Gerard wants maximum visual impact and bid-centric navigation

---

### 3. `frontend-v3/` - Warm & Friendly Dashboard

**Vibe**: Notion/Linear inspired, collaborative workspace

**Colors**: Warm Indigo `#6366f1` + Coral `#d9534f` on Beige neutrals
**Fonts**: DM Sans + Inter
**Tech**: Alpine.js + custom CSS, 3-column layout

**Strengths**:
- **3-column layout**: sidebar nav, main content, right panel (unique among versions)
- **AI Assistant widget** with smart suggestions (budget insights, restock alerts)
- **Bid selector dropdown** in header
- Dashboard with stat cards, charts, activity feed
- Warm, approachable design (less intimidating for non-tech users)
- Collaborative feel with team activity

**Weaknesses**:
- No vendor logo marquee
- 3-column layout may feel cramped on smaller screens
- Fewer product browsing features
- Less traditional e-commerce flow

**Best For**: If the priority is a dashboard-first experience with AI features

---

### 4. `frontend-v4/` - School Supplies Theme

**Vibe**: Playful, educational (think classroom bulletin board meets modern web)

**Colors**: Crayon Blue `#457b9d` + Teal `#2a9d8f` + Red `#e63946` on Paper White `#fffef9`
**Fonts**: Fredoka + Patrick Hand + Inter
**Tech**: Alpine.js + custom CSS design system

**Strengths**:
- **Instantly recognizable** as education-focused (sticky notes, emoji icons, pencil-shaped buttons)
- Strong category sidebar with tab navigation
- Vendor filtering with playful pencil UI elements
- Budget tracking with visual indicators
- Contract pricing clearly highlighted
- Order timeline view

**Weaknesses**:
- No bid-based filtering
- No vendor logo carousel
- Playful aesthetic may feel unprofessional to some administrators
- Handwriting fonts may impact readability

**Best For**: If the audience is primarily teachers/staff who want something fun and approachable

---

### 5. `frontend-v5/` - Premium Modern (Best-of-All)

**Vibe**: Polished blend of all previous versions with theme switching

**Colors**: Rich Indigo `#6366f1` + Coral `#f43f5e` (default theme)
**Fonts**: Plus Jakarta Sans + Inter + DM Sans + Fredoka
**Tech**: Alpine.js + CSS design system + themes.css (5 complete themes)

**Strengths**:
- **5 switchable themes** at runtime (Bold, Dark, Warm, Educational, Premium)
- **Bid selector** with multiple bid options
- **Vendor marquee carousel** (infinite scroll, pauses on hover)
- **AI Smart Assistant** with 3 suggestion types
- **Team Share** feature for collaborative ordering
- **Budget donut chart** with category breakdown
- "On Bid" badges showing savings percentages
- Keyboard-accessible theme switcher

**Weaknesses**:
- Theme switching adds complexity
- Less feature-complete than original `frontend/`
- No full filter sidebar (relies on bid selector + categories)
- Composite design may feel unfocused

**Best For**: If Gerard wants to choose between multiple looks in one demo, or if different districts want different themes

---

### 6. `frontend-reimagined/` - Bold & Vibrant

**Vibe**: Modern e-commerce with strong branding (think Shopify storefront)

**Colors**: Electric Indigo `#4f46e5` + Coral `#f43f5e` + Pop accents (yellow, cyan, lime)
**Fonts**: Space Grotesk + Inter
**Tech**: Alpine.js + custom CSS, 4 pages, all logic inline

**Strengths**:
- **Hero banner** with compelling stats (50K+ products, 500+ districts)
- **Category pills** for quick filtering (8 categories)
- **Full sidebar filters**: categories with counts, price range, brand filters
- Clean product grid with cart drawer
- Budget impact visualization in checkout
- Split-screen login with animated hero
- Most "modern website" feeling of all versions

**Weaknesses**:
- No bid-based filtering
- No vendor logo marquee
- No requisition management page
- No AI assistant
- Fewest pages (4 total)
- Feels more like a consumer storefront than procurement tool

**Best For**: If the priority is a clean, modern shopping experience with strong visual branding

---

### 7. `frontend-v6/` - Procurement Hub (Bid-Centric)

**Vibe**: Clean procurement platform built entirely around bid navigation (think Coupa meets school purchasing)

**Colors**: Indigo `#6366f1` + contextual semantic colors (success/warning/error) on clean white
**Fonts**: Plus Jakarta Sans + Inter + JetBrains Mono
**Tech**: Alpine.js + custom CSS design system, 3 pages, all logic inline

**Strengths**:
- **Bid pill bar** always visible below header - one-click bid switching filters entire catalog
- **Vendor marquee** with clickable vendor icons that auto-filter products
- **Starter Orders tab** - 6 pre-built order templates by role (Teacher, Art Teacher, STEM, Custodian, Admin, New Teacher) - **only version with this feature**
- **Full filter sidebar**: categories with counts, vendor checkboxes, price range inputs
- **My Requisitions summary** in sidebar with status counts (Draft/Pending/Approved/Fulfilled)
- **Stats row**: budget remaining, orders approved, pending approval, bid savings
- **Grid/List view toggle** with sort options
- **3-step checkout** with stepper (Review Cart > Shipping & Notes > Confirmation)
- Budget impact visualization in checkout with color-coded meter
- "On Bid" and "Popular" badges on product cards
- Bid savings calculated and shown in order summary
- **API-connected**: calls real `/api/bids`, `/api/bids/:id/vendors`, `/api/bids/:id/products` endpoints
- Split-screen login with hero stats panel
- Skip-to-content link (accessibility)
- Clean, professional design without being flashy

**Weaknesses**:
- Only 3 pages (index, login, checkout) - no dedicated product detail page
- No AI assistant
- No theme switching
- No saved lists or bulk import
- Starter orders are client-side templates (not yet API-backed)
- No recurring orders

**Best For**: If Gerard wants the most complete bid-centric experience with starter orders - this is the closest to his stated requirements

---

## Side-by-Side Comparison

### Design Approach

| Version | Theme | Layout | Target Audience |
|---|---|---|---|
| frontend/ | Professional Navy | Sidebar + Grid | Power users, admins |
| v2 | Dark SaaS | Dashboard + Cards | Tech-savvy procurement |
| v3 | Warm Collaborative | 3-Column Dashboard | Teams, collaborative buyers |
| v4 | Playful Educational | Sidebar + Tabs | Teachers, classroom staff |
| v5 | Multi-Theme | Dashboard + Cards | All audiences (theme picks) |
| v6 | Clean Procurement | Bid Bar + Sidebar + Grid | Procurement staff, bid-focused buyers |
| reimagined | Bold Modern | Hero + Grid + Sidebar | Marketing/demo, new users |

### Feature Depth

| Feature | frontend/ | v2 | v3 | v4 | v5 | v6 | reimagined |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Pages | 20+ | 6 | 6 | 5 | 5 | 3 | 4 |
| JS Store Modules | 18 | inline | inline | inline | inline | inline | inline |
| Saved Lists | Yes | Yes | - | - | - | - | - |
| Bulk Import | Yes | Yes | - | - | - | - | - |
| AI Assistant | Yes | - | Yes | - | Yes | - | - |
| Product Comparison | Yes | - | - | - | - | - | - |
| Recurring Orders | Yes | Yes | - | - | - | - | - |
| Admin Dashboard | Yes | - | - | - | - | - | - |
| Theme Switching | - | - | - | - | 5 themes | - | - |
| Voice Search | Yes | - | - | - | - | - | - |
| Budget Charts | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Starter Orders | - | - | - | - | - | **Yes** | - |
| Bid API Connected | - | - | - | - | - | **Yes** | - |
| 3-Step Checkout | - | - | - | - | - | **Yes** | - |

---

## API Capabilities (Current State)

**What Exists**:
- Product search with category, vendor, status, price filters + autocomplete
- Vendor listing with search and product counts
- Category listing with product counts
- Full requisition workflow (submit, list, detail, update, cancel, approve, reject)
- My Requisitions with status counts (the "summary screen")
- Session-based auth with stored procedure login

**What Needs to Be Built for Gerard's Requirements**:
1. **Bid filtering endpoint** - No bid/contract table or filter exists in API
2. **Starter orders / saved templates** - No per-bid or per-role template system
3. **Vendor logos** - No logo URL field in vendor API response
4. **Popular products by bid** - No popularity tracking or bid-scoped product queries

---

## Recommendation

**Lead with `frontend-v6`** — it's the closest match to Gerard's stated requirements (bid filtering, vendor marquee, starter orders, requisition summary). Then show **frontend/** for full feature depth and **v5** for theme flexibility.

For the final build, cherry-pick the best of each:

- **From v6**: Bid pill bar, starter orders, vendor marquee, 3-step checkout, bid API integration
- **From frontend/**: Full feature set (saved lists, bulk import, filters, admin dashboard, recurring orders)
- **From v3**: AI assistant and warm, collaborative feel
- **From v5**: Theme switching for district customization
- **From reimagined**: Hero section and modern product grid
- **Remaining gap**: Make starter orders API-backed (currently client-side templates in v6)

---

## Next Steps

1. Teams walkthrough early next week (confirmed with Gerard)
2. Live demo of v5 theme switching + frontend/ features
3. Review Gerard's feedback on which direction to take
4. Build unified concept incorporating feedback + missing features
5. Add bid filtering to FastAPI backend
