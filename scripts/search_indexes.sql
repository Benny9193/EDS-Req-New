-- =============================================================================
-- EDS Universal Requisition - Search Performance Indexes
-- =============================================================================
-- Purpose: Optimize product search queries by adding targeted indexes
--
-- These indexes support the prefix-first search strategy used in products.py:
--   - Prefix matches: Description LIKE 'query%' (index-friendly)
--   - Word boundary: Description LIKE '% query%' (fallback)
--
-- The prefix match pattern can use these indexes efficiently.
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Index 1: Items Description Search Index
-- Primary index for text search on product descriptions
-- Covers: get_products, autocomplete_search queries
-- -----------------------------------------------------------------------------
IF NOT EXISTS (
    SELECT 1 FROM sys.indexes
    WHERE name = 'IX_Items_Description_Search'
    AND object_id = OBJECT_ID('Items')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Items_Description_Search
    ON Items (Description)
    INCLUDE (ItemId, ItemCode, ShortDescription, CategoryId, VendorId, ListPrice, Active, UnitId, VendorPartNumber)
    WHERE Active = 1 AND ListPrice > 0;

    PRINT 'Created index: IX_Items_Description_Search';
END
ELSE
BEGIN
    PRINT 'Index IX_Items_Description_Search already exists';
END
GO

-- -----------------------------------------------------------------------------
-- Index 2: Items ItemCode Search Index
-- Supports search by product code/SKU
-- Covers: autocomplete_search, get_products queries
-- -----------------------------------------------------------------------------
IF NOT EXISTS (
    SELECT 1 FROM sys.indexes
    WHERE name = 'IX_Items_ItemCode_Search'
    AND object_id = OBJECT_ID('Items')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Items_ItemCode_Search
    ON Items (ItemCode)
    INCLUDE (ItemId, Description, CategoryId, VendorId, ListPrice)
    WHERE Active = 1 AND ListPrice > 0;

    PRINT 'Created index: IX_Items_ItemCode_Search';
END
ELSE
BEGIN
    PRINT 'Index IX_Items_ItemCode_Search already exists';
END
GO

-- -----------------------------------------------------------------------------
-- Index 3: Items VendorPartNumber Search Index
-- Supports search by vendor part number in autocomplete
-- -----------------------------------------------------------------------------
IF NOT EXISTS (
    SELECT 1 FROM sys.indexes
    WHERE name = 'IX_Items_VendorPartNumber_Search'
    AND object_id = OBJECT_ID('Items')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Items_VendorPartNumber_Search
    ON Items (VendorPartNumber)
    INCLUDE (ItemId, Description)
    WHERE Active = 1 AND VendorPartNumber IS NOT NULL;

    PRINT 'Created index: IX_Items_VendorPartNumber_Search';
END
ELSE
BEGIN
    PRINT 'Index IX_Items_VendorPartNumber_Search already exists';
END
GO

-- -----------------------------------------------------------------------------
-- Index 4: Items Category Filter Index
-- Supports category filtering in product list
-- -----------------------------------------------------------------------------
IF NOT EXISTS (
    SELECT 1 FROM sys.indexes
    WHERE name = 'IX_Items_CategoryId_Filter'
    AND object_id = OBJECT_ID('Items')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Items_CategoryId_Filter
    ON Items (CategoryId, Active)
    INCLUDE (ItemId, Description, VendorId, ListPrice)
    WHERE Active = 1 AND ListPrice > 0;

    PRINT 'Created index: IX_Items_CategoryId_Filter';
END
ELSE
BEGIN
    PRINT 'Index IX_Items_CategoryId_Filter already exists';
END
GO

-- -----------------------------------------------------------------------------
-- Index 5: Items Price Range Index
-- Supports price range filtering in product list
-- -----------------------------------------------------------------------------
IF NOT EXISTS (
    SELECT 1 FROM sys.indexes
    WHERE name = 'IX_Items_ListPrice_Filter'
    AND object_id = OBJECT_ID('Items')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_Items_ListPrice_Filter
    ON Items (ListPrice, Active)
    INCLUDE (ItemId, Description, CategoryId, VendorId)
    WHERE Active = 1;

    PRINT 'Created index: IX_Items_ListPrice_Filter';
END
ELSE
BEGIN
    PRINT 'Index IX_Items_ListPrice_Filter already exists';
END
GO

-- -----------------------------------------------------------------------------
-- Index 6: CrossRefs Image Lookup Index
-- Supports batch image fetching for lazy loading
-- Covers: POST /products/images endpoint
-- -----------------------------------------------------------------------------
IF NOT EXISTS (
    SELECT 1 FROM sys.indexes
    WHERE name = 'IX_CrossRefs_ImageURL_Lookup'
    AND object_id = OBJECT_ID('CrossRefs')
)
BEGIN
    CREATE NONCLUSTERED INDEX IX_CrossRefs_ImageURL_Lookup
    ON CrossRefs (ItemId, Active)
    INCLUDE (ImageURL)
    WHERE Active = 1 AND ImageURL IS NOT NULL AND ImageURL != '';

    PRINT 'Created index: IX_CrossRefs_ImageURL_Lookup';
END
ELSE
BEGIN
    PRINT 'Index IX_CrossRefs_ImageURL_Lookup already exists';
END
GO

-- =============================================================================
-- Usage Notes:
-- =============================================================================
-- 1. Run this script during a maintenance window
-- 2. Monitor index usage with:
--    SELECT * FROM sys.dm_db_index_usage_stats
--    WHERE object_id = OBJECT_ID('Items')
-- 3. Check index sizes with:
--    EXEC sp_spaceused 'Items'
-- =============================================================================

PRINT 'Search index creation complete.';
GO
