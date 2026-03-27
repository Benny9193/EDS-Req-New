# EDS Universal Requisition System - Demo Script

**Format:** Microsoft Teams screen share
**Duration:** ~12-15 minutes
**Presenter prep:** Have all three versions open in separate browser tabs before the call. Log in to each beforehand so you're on the main catalog page.

- Tab 1: `http://localhost:8000/v3/`
- Tab 2: `http://localhost:8000/v4/`
- Tab 3: `http://localhost:8000/v5/`

---

## Opening (1 min)

> "I want to walk you through three design directions we've been exploring for the new Universal Requisition frontend. All three connect to the same backend API and database -- same product data, same cart logic, same auth. The difference is purely the UI/UX approach. I'll show you the key features on each one so you can see which direction feels right."

---

## Version 3 - Professional / Warm (3-4 min)

**Switch to Tab 1**

> "This first version goes for a clean, professional look. Warm earth tones, Georgia serif font -- it feels more like a polished internal tool than a typical school purchasing site."

### Walk through:

1. **Point out the layout** - header, search bar, product grid, sidebar
2. **Search** - Type a product name (e.g., "paper") in the search bar
   - Point out results update in real time
3. **Filters** - Select a category from the dropdown, then a vendor
   - Point out the **filter pills** that appear below the bar showing active filters
   - Point out the **result count** next to the pills
   - Click the **X** on one pill to remove just that filter
4. **Price range** - Enter a Min price (e.g., 1) and Max price (e.g., 20)
   - Point out a new pill appears for the price range
5. **Sort** - Select "Price: Low to High" from the sort dropdown
6. **Clear All** - Click the Clear All button to reset everything at once
7. **Add to cart** - Click "Add to Cart" on a product, show the toast notification
8. **Save List** - Click the Save List button, type a name like "Office Basics", click Save
   - Show the saved list appears in the dropdown with item count and date
   - Mention: "These persist across sessions via localStorage"
9. **Load More** - If enough products, scroll down and point out the "Load More (X remaining)" button

> "So that's v3 -- professional, functional, straightforward."

---

## Version 4 - School / Playful (3-4 min)

**Switch to Tab 2**

> "This next version leans into the school theme. Think classroom whiteboard, notebook paper, bold handwritten feel. The idea is that school district staff might find this more approachable and fun."

### Walk through:

1. **Point out the theme** - Comic Sans-style font, notebook paper textures, bold black borders, crayon-style category tabs
2. **Category tabs** - Click a category tab across the top (the crayon-style selector)
   - Note: "These do server-side filtering -- it re-fetches from the API"
3. **Filters** - Select a vendor, enter a price range
   - Point out the filter pills use the same bold school-themed styling
   - Note the "Erase All" button instead of "Clear All" -- on-theme naming
4. **Search** - Type something, show real-time filtering
5. **Save List** - Click Save List, save one called "Art Supplies"
   - Show the saved lists dropdown
   - Click the cart icon on a saved list to add all items to cart at once
6. **Load More** - Point out "Show More (X left)" button -- different label, same function
7. **Add to cart** - Add an item, show the school-themed toast notification

> "Same features, completely different personality. The question is whether this resonates with the audience or if it's too casual."

---

## Version 5 - Modern / Glassmorphism (3-4 min)

**Switch to Tab 3**

> "This last version is the most modern. It uses glassmorphism -- frosted glass effects, translucent panels, depth through blur. It's the kind of design you see in newer consumer apps. The sidebar has an AI assistant widget and spending analytics built in."

### Walk through:

1. **Point out the design** - Dark indigo gradient background, frosted glass cards, subtle blur effects throughout
2. **Sidebar** - Point out the AI assistant widget, spending chart, quick actions
   - "These are mock-ups right now but show where we could go with smart features"
3. **Filters** - Use the category and vendor dropdowns (glass-styled dropdowns)
   - Show filter pills with the translucent indigo styling
4. **Price range** - Enter min/max values, show the pill
5. **Sort + Clear All** - Demonstrate both
6. **Save List** - Click Save List, save one, show the frosted glass dropdown
   - Demo adding a saved list to cart
7. **Load More** - Show the glass-styled Load More button
8. **Add to cart** - Add an item, show the indigo glass toast notification

> "This one pushes the visual design furthest. It looks premium, but the tradeoff is it's a bigger departure from what people expect from a procurement tool."

---

## Wrap-up / Comparison (2 min)

> "So to recap the three directions:"

| | V3 - Professional | V4 - School | V5 - Modern |
|---|---|---|---|
| **Feel** | Clean, corporate | Fun, approachable | Premium, cutting-edge |
| **Font** | Georgia serif | Comic Sans display | System sans-serif |
| **Color** | Warm earth tones | Black/white, bold | Indigo gradients |
| **Best for** | Broad appeal | K-12 audience | Tech-forward districts |

> "All three have identical functionality under the hood: search, category/vendor filters, price range, sort, filter pills, save-as-list, dynamic loading, server-side cart persistence. The backend is the same FastAPI + SQL Server stack regardless of which direction we pick."

**Ask:**
> "Which direction feels closest to what you'd want to show clients? Or do you want us to mix elements -- say, v3's layout with some of v5's polish?"

---

## If Asked About Technical Details

- **Backend:** FastAPI with pyodbc connecting to SQL Server (EDS database)
- **Frontend:** Pure Alpine.js -- no build step, no npm, deploys as static HTML
- **Cart:** Persists both in localStorage and server-side (in-memory store keyed by session)
- **Auth:** Uses existing `sp_FA_AttemptLogin` stored proc, session-based
- **Saved lists:** localStorage with `eds_saved_lists` key, shared across all versions
- **Dynamic loading:** Client-side pagination, shows 24 items then Load More
