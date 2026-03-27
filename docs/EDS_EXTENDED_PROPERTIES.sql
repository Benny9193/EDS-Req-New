-- EDS Database Extended Properties Script
-- Generated: 2026-01-09 09:52:14
-- Adds MS_Description extended properties for documentation
--
-- Run this script to add inline documentation to SQL Server
-- These descriptions appear in SSMS and documentation tools
--

USE [EDS];
GO

-- ============================================
-- TABLE DESCRIPTIONS
-- ============================================

-- AccountingDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AccountingDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for AccountingDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingDetail';
GO

-- AccountingFormats
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AccountingFormats') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for AccountingFormats', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingFormats';
GO

-- AccountingUserFields
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AccountingUserFields') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for AccountingUserFields', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingUserFields';
GO

-- Accounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Accounts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Chart of accounts', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Accounts';
GO

-- AccountSeparators
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AccountSeparators') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for AccountSeparators', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountSeparators';
GO

-- AddendumItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AddendumItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'AddendumItems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems';
GO

-- additems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.additems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'additems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'additems';
GO

-- Alerts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Alerts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Alerts data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Alerts';
GO

-- allitems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.allitems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'allitems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems';
GO

-- AnswerTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AnswerTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'AnswerTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AnswerTypes';
GO

-- ApprovalLevels
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ApprovalLevels') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Approval hierarchy and thresholds', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalLevels';
GO

-- Approvals
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Approvals') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Approval workflow records', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Approvals';
GO

-- ApprovalsHistory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ApprovalsHistory') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ApprovalsHistory data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalsHistory';
GO

-- Audit
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Audit') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for Audit', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Audit';
GO

-- Awardings
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Awardings') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Awardings data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awardings';
GO

-- Awards
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Awards') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Awards data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards';
GO

-- AwardsCatalogList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AwardsCatalogList') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'AwardsCatalogList data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AwardsCatalogList';
GO

-- AwardTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.AwardTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'AwardTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AwardTypes';
GO

-- BatchBook
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BatchBook') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'BatchBook data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook';
GO

-- BatchDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BatchDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'BatchDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail';
GO

-- BatchDetailInserts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BatchDetailInserts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'BatchDetailInserts data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetailInserts';
GO

-- Batches
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Batches') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Batches data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Batches';
GO

-- BidAnswers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidAnswers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Answers to vendor questions on bids', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswers';
GO

-- BidAnswersJournal
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidAnswersJournal') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidAnswersJournal', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswersJournal';
GO

-- BidCalendar
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidCalendar') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidCalendar', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar';
GO

-- BidderCheckList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidderCheckList') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidderCheckList', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckList';
GO

-- BidderCheckListPkgDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidderCheckListPkgDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidderCheckListPkgDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgDetail';
GO

-- BidderCheckListPkgHeader
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidderCheckListPkgHeader') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidderCheckListPkgHeader', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgHeader';
GO

-- BidDocument
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidDocument') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidDocument', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocument';
GO

-- BidDocumentTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidDocumentTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidDocumentTypes', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocumentTypes';
GO

-- BidHeaderCheckList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidHeaderCheckList') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidHeaderCheckList', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderCheckList';
GO

-- BidHeaderDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidHeaderDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidHeaderDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail';
GO

-- BidHeaderDetail_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidHeaderDetail_Orig') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidHeaderDetail_Orig', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail_Orig';
GO

-- BidHeaderDocument
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidHeaderDocument') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidHeaderDocument', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocument';
GO

-- BidHeaderDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidHeaderDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidHeaderDocuments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocuments';
GO

-- BidHeaders
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidHeaders') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Master bid/solicitation records containing bid numbers, dates, and status', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders';
GO

-- BidImportCatalogList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidImportCatalogList') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidImportCatalogList', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImportCatalogList';
GO

-- BidImportCounties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidImportCounties') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidImportCounties', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImportCounties';
GO

-- BidImports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidImports') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidImports', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports';
GO

-- BidItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Line items within bids specifying products/services being solicited', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems';
GO

-- BidItems_Old
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidItems_Old') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidItems_Old', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old';
GO

-- BidManagers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidManagers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidManagers', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManagers';
GO

-- BidManufacturers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidManufacturers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidManufacturers', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManufacturers';
GO

-- BidMappedItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidMappedItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidMappedItems', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMappedItems';
GO

-- BidMgrConfiguration
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidMgrConfiguration') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidMgrConfiguration', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMgrConfiguration';
GO

-- BidMgrTagFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidMgrTagFile') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidMgrTagFile', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMgrTagFile';
GO

-- BidMSRPResultPrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidMSRPResultPrices') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidMSRPResultPrices', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultPrices';
GO

-- BidMSRPResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidMSRPResults') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidMSRPResults', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults';
GO

-- BidMSRPResultsProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidMSRPResultsProductLines', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines';
GO

-- BidPackage
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidPackage') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidPackage', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackage';
GO

-- BidPackageDocument
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidPackageDocument') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidPackageDocument', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackageDocument';
GO

-- BidProductLinePrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidProductLinePrices') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidProductLinePrices', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLinePrices';
GO

-- BidProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidProductLines') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidProductLines', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLines';
GO

-- BidQuestions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidQuestions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Questions submitted by vendors during bid process', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidQuestions';
GO

-- BidReawards
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidReawards') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidReawards', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidReawards';
GO

-- BidRequestItemMergeActions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestItemMergeActions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestItemMergeActions', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions';
GO

-- BidRequestItemMergeActions_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Orig') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestItemMergeActions_Orig', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Orig';
GO

-- BidRequestItemMergeActions_Saved_101521
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Saved_101521') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestItemMergeActions_Saved_101521', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Saved_101521';
GO

-- BidRequestItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestItems', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems';
GO

-- BidRequestItems_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestItems_Orig') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestItems_Orig', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems_Orig';
GO

-- BidRequestManufacturer
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestManufacturer') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestManufacturer', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestManufacturer';
GO

-- BidRequestOptions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestOptions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestOptions', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions';
GO

-- BidRequestPriceRanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestPriceRanges') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestPriceRanges', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestPriceRanges';
GO

-- BidRequestProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidRequestProductLines') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidRequestProductLines', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestProductLines';
GO

-- BidResponses
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidResponses') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidResponses', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResponses';
GO

-- BidResultChanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidResultChanges') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidResultChanges', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultChanges';
GO

-- BidResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidResults') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Awarded bid results linking vendors to bid items with pricing', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults';
GO

-- BidResults_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidResults_Orig') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidResults_Orig', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig';
GO

-- BidResultsChangeLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidResultsChangeLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidResultsChangeLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultsChangeLog';
GO

-- Bids
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Bids') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for Bids', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids';
GO

-- BidsCatalogList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidsCatalogList') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidsCatalogList', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidsCatalogList';
GO

-- BidTradeCounties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidTradeCounties') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidTradeCounties', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTradeCounties';
GO

-- BidTrades
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidTrades') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidTrades', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTrades';
GO

-- BidTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BidTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for BidTypes', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTypes';
GO

-- BookTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BookTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'BookTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BookTypes';
GO

-- BudgetAccounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.BudgetAccounts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for BudgetAccounts', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BudgetAccounts';
GO

-- Budgets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Budgets') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Budget allocations and tracking', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Budgets';
GO

-- CalDistricts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CalDistricts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CalDistricts data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalDistricts';
GO

-- CalendarDates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CalendarDates') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CalendarDates data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarDates';
GO

-- CalendarIB
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CalendarIB') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CalendarIB data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarIB';
GO

-- CalendarItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CalendarItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CalendarItems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarItems';
GO

-- Calendars
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Calendars') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Calendars data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Calendars';
GO

-- CalendarTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CalendarTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CalendarTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarTypes';
GO

-- Carolina Living Items
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Carolina Living Items') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Carolina Living Items data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Carolina Living Items';
GO

-- Catalog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Catalog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Catalog data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog';
GO

-- CatalogImportFields
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogImportFields') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogImportFields data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportFields';
GO

-- CatalogImportMap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogImportMap') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogImportMap data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportMap';
GO

-- CatalogPricing
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogPricing') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogPricing data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogPricing';
GO

-- CatalogRequest
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogRequest') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogRequest data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest';
GO

-- CatalogRequestDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogRequestDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogRequestDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestDetail';
GO

-- CatalogRequestStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogRequestStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogRequestStatus data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestStatus';
GO

-- CatalogText
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogText') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogText data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogText';
GO

-- CatalogTextParts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatalogTextParts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatalogTextParts data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogTextParts';
GO

-- Category
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Category') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Category data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Category';
GO

-- CatList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CatList') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CatList data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList';
GO

-- CertificateAuthority
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CertificateAuthority') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CertificateAuthority data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CertificateAuthority';
GO

-- ChargeTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ChargeTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ChargeTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ChargeTypes';
GO

-- CommonMSRPVendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CommonMSRPVendorQuery') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for CommonMSRPVendorQuery', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonMSRPVendorQuery';
GO

-- CommonTandMVendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CommonTandMVendorQuery') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for CommonTandMVendorQuery', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonTandMVendorQuery';
GO

-- CommonVendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CommonVendorQuery') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for CommonVendorQuery', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonVendorQuery';
GO

-- CommonVendorQueryAnswer
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CommonVendorQueryAnswer') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for CommonVendorQueryAnswer', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonVendorQueryAnswer';
GO

-- ContractTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ContractTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ContractTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ContractTypes';
GO

-- Control
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Control') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Control data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Control';
GO

-- Coops
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Coops') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Coops data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Coops';
GO

-- CopyRequests
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CopyRequests') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CopyRequests data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CopyRequests';
GO

-- Counties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Counties') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Counties data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Counties';
GO

-- CoverView
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CoverView') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CoverView data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView';
GO

-- CrossRefs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CrossRefs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CrossRefs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs';
GO

-- CSCommands
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CSCommands') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CSCommands data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSCommands';
GO

-- CSMessageFiles
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CSMessageFiles') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CSMessageFiles data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSMessageFiles';
GO

-- CSMessages
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CSMessages') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CSMessages data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSMessages';
GO

-- CSRep
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CSRep') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CSRep data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSRep';
GO

-- CXmlSession
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.CXmlSession') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'CXmlSession data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession';
GO

-- dchtest
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.dchtest') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'dchtest data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest';
GO

-- DebugMsgs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DebugMsgs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DebugMsgs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DebugMsgs';
GO

-- DebugMsgs_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DebugMsgs_Orig') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DebugMsgs_Orig data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DebugMsgs_Orig';
GO

-- Detail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Detail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order line items with quantities and prices', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail';
GO

-- DetailChangeLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DetailChangeLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for DetailChangeLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog';
GO

-- DetailChanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DetailChanges') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DetailChanges data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChanges';
GO

-- DetailHold
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DetailHold') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DetailHold data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold';
GO

-- DetailMatch
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DetailMatch') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DetailMatch data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch';
GO

-- DetailNotifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DetailNotifications') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DetailNotifications data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications';
GO

-- DetailUploads
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DetailUploads') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DetailUploads data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailUploads';
GO

-- District
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.District') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'District data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District';
GO

-- DistrictCategories
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictCategories') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictCategories data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategories';
GO

-- DistrictCategoryTitles
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictCategoryTitles') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictCategoryTitles data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategoryTitles';
GO

-- DistrictCharges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictCharges') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictCharges data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCharges';
GO

-- DistrictChargesNotes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictChargesNotes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictChargesNotes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictChargesNotes';
GO

-- DistrictContacts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictContacts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictContacts data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts';
GO

-- DistrictContactTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictContactTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictContactTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContactTypes';
GO

-- DistrictContinuances
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictContinuances') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictContinuances data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances';
GO

-- DistrictNotes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictNotes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictNotes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotes';
GO

-- DistrictNotifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictNotifications') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictNotifications data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotifications';
GO

-- DistrictPP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictPP') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictPP data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictPP';
GO

-- DistrictProposedCharges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictProposedCharges data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges';
GO

-- DistrictReports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictReports') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Reporting table for DistrictReports', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictReports';
GO

-- DistrictTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DistrictTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictTypes';
GO

-- DistrictVendor
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DistrictVendor') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for DistrictVendor', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictVendor';
GO

-- DMSBidDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DMSBidDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for DMSBidDocuments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSBidDocuments';
GO

-- DMSSDSDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DMSSDSDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'DMSSDSDocuments data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSSDSDocuments';
GO

-- DMSVendorBidDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DMSVendorBidDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for DMSVendorBidDocuments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorBidDocuments';
GO

-- DMSVendorDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.DMSVendorDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for DMSVendorDocuments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorDocuments';
GO

-- dtproperties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.dtproperties') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'dtproperties data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dtproperties';
GO

-- EmailBlast
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.EmailBlast') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'EmailBlast data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlast';
GO

-- EmailBlastAddresses08132012
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.EmailBlastAddresses08132012') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'EmailBlastAddresses08132012 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastAddresses08132012';
GO

-- EmailBlastCopy
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.EmailBlastCopy') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'EmailBlastCopy data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastCopy';
GO

-- EmailBlastLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.EmailBlastLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for EmailBlastLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastLog';
GO

-- FreezeItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.FreezeItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'FreezeItems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems';
GO

-- FreezeItems2015
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.FreezeItems2015') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'FreezeItems2015 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015';
GO

-- HeaderWorkItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.HeaderWorkItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'HeaderWorkItems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'HeaderWorkItems';
GO

-- Headings
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Headings') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Headings data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Headings';
GO

-- HolidayCalendar
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.HolidayCalendar') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'HolidayCalendar data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'HolidayCalendar';
GO

-- HolidayCalendarVendor
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.HolidayCalendarVendor') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for HolidayCalendarVendor', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'HolidayCalendarVendor';
GO

-- ImageErrors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImageErrors') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ImageErrors data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImageErrors';
GO

-- ImageLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImageLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for ImageLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImageLog';
GO

-- Images
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Images') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Images data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Images';
GO

-- ImportCatalogDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImportCatalogDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ImportCatalogDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportCatalogDetail';
GO

-- ImportCatalogHeader
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImportCatalogHeader') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ImportCatalogHeader data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportCatalogHeader';
GO

-- ImportDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImportDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ImportDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportDetail';
GO

-- ImportMessages
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImportMessages') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ImportMessages data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportMessages';
GO

-- ImportProcesses
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ImportProcesses') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ImportProcesses data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportProcesses';
GO

-- Imports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Imports') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Imports data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Imports';
GO

-- InstructionBookContents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.InstructionBookContents') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'InstructionBookContents data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InstructionBookContents';
GO

-- InstructionBookTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.InstructionBookTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'InstructionBookTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InstructionBookTypes';
GO

-- Instructions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Instructions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Instructions data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Instructions';
GO

-- Invoices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Invoices') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor invoices', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Invoices';
GO

-- InvoiceTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.InvoiceTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'InvoiceTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InvoiceTypes';
GO

-- IPQueue
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.IPQueue') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'IPQueue data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueue';
GO

-- IPQueueUsers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.IPQueueUsers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for IPQueueUsers', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueueUsers';
GO

-- ItemContractPrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ItemContractPrices') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ItemContractPrices data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemContractPrices';
GO

-- ItemDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ItemDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ItemDocuments data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemDocuments';
GO

-- Items
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Items') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Master item/product catalog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items';
GO

-- ItemUpdates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ItemUpdates') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ItemUpdates data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemUpdates';
GO

-- jSessions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.jSessions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'jSessions data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'jSessions';
GO

-- Keywords
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Keywords') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Keywords data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Keywords';
GO

-- Ledger
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Ledger') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Ledger data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Ledger';
GO

-- LL_RepArea
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.LL_RepArea') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'LL_RepArea data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'LL_RepArea';
GO

-- LL_RepLay
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.LL_RepLay') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'LL_RepLay data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'LL_RepLay';
GO

-- ManufacturerProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ManufacturerProductLines') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ManufacturerProductLines data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ManufacturerProductLines';
GO

-- Manufacturers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Manufacturers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Manufacturers data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Manufacturers';
GO

-- MappedItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.MappedItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'MappedItems data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MappedItems';
GO

-- Menus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Menus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Menus data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Menus';
GO

-- Messages
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Messages') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Messages data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Messages';
GO

-- Months
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Months') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Months data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Months';
GO

-- MSDS
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.MSDS') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'MSDS data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSDS';
GO

-- MSDSDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.MSDSDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'MSDSDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSDSDetail';
GO

-- MSRPExcelExport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.MSRPExcelExport') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'MSRPExcelExport data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPExcelExport';
GO

-- MSRPExcelImport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.MSRPExcelImport') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'MSRPExcelImport data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPExcelImport';
GO

-- MSRPOptions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.MSRPOptions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for MSRPOptions', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPOptions';
GO

-- NextNumber
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.NextNumber') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'NextNumber data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NextNumber';
GO

-- NotificationOptions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.NotificationOptions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'NotificationOptions data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NotificationOptions';
GO

-- Notifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Notifications') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Notifications data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Notifications';
GO

-- OBPrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OBPrices') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'OBPrices data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices';
GO

-- OBView
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OBView') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'OBView data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView';
GO

-- Options
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Options') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Options data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Options';
GO

-- OptionsLink
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OptionsLink') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'OptionsLink data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OptionsLink';
GO

-- OrderBookAlwaysAdd
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OrderBookAlwaysAdd') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for OrderBookAlwaysAdd', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookAlwaysAdd';
GO

-- OrderBookDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OrderBookDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for OrderBookDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail';
GO

-- OrderBookDetailOld
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for OrderBookDetailOld', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld';
GO

-- OrderBookLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OrderBookLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for OrderBookLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookLog';
GO

-- OrderBooks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OrderBooks') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Order book/catalog management', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks';
GO

-- OrderBookTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.OrderBookTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for OrderBookTypes', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookTypes';
GO

-- Payments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Payments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Payment records', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Payments';
GO

-- PaymentTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PaymentTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PaymentTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PaymentTypes';
GO

-- PendingApprovals
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PendingApprovals') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PendingApprovals data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals';
GO

-- PO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PO') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order headers with vendor, dates, and totals', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO';
GO

-- PODetailItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PODetailItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for PODetailItems', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems';
GO

-- POIDTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POIDTable') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POIDTable', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POIDTable';
GO

-- POLayoutDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POLayoutDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POLayoutDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayoutDetail';
GO

-- POLayoutFields
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POLayoutFields') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POLayoutFields', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayoutFields';
GO

-- POLayouts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POLayouts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POLayouts', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayouts';
GO

-- POPageSummary
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POPageSummary') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POPageSummary', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPageSummary';
GO

-- POPrintTaggedPOFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POPrintTaggedPOFile') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POPrintTaggedPOFile', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPrintTaggedPOFile';
GO

-- POQueue
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POQueue') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POQueue', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueue';
GO

-- POQueueItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POQueueItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POQueueItems', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueueItems';
GO

-- POStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POStatus', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatus';
GO

-- POStatusTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POStatusTable') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POStatusTable', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatusTable';
GO

-- PostCatalogDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PostCatalogDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PostCatalogDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PostCatalogDetail';
GO

-- PostCatalogHeader
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PostCatalogHeader') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PostCatalogHeader data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PostCatalogHeader';
GO

-- POTemp
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POTemp') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POTemp', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POTemp';
GO

-- POTempDetails
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.POTempDetails') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for POTempDetails', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POTempDetails';
GO

-- PPCatalogs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PPCatalogs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PPCatalogs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCatalogs';
GO

-- PPCategory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PPCategory') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PPCategory data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCategory';
GO

-- PriceHolds
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PriceHolds') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PriceHolds data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceHolds';
GO

-- PriceListTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PriceListTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PriceListTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceListTypes';
GO

-- PricePlans
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PricePlans') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PricePlans data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricePlans';
GO

-- PriceRanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PriceRanges') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PriceRanges data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceRanges';
GO

-- Prices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Prices') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Prices data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices';
GO

-- PricingAddenda
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PricingAddenda') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PricingAddenda data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda';
GO

-- PricingConsolidatedOrderCounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PricingConsolidatedOrderCounts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for PricingConsolidatedOrderCounts', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingConsolidatedOrderCounts';
GO

-- PricingMap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PricingMap') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PricingMap data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap';
GO

-- PricingUpdate
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PricingUpdate') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PricingUpdate data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingUpdate';
GO

-- PrintDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.PrintDocuments') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'PrintDocuments data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PrintDocuments';
GO

-- Printers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Printers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Printers data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Printers';
GO

-- ProductVerificationResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ProductVerificationResults') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ProductVerificationResults data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ProductVerificationResults';
GO

-- ProjectTasks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ProjectTasks') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ProjectTasks data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ProjectTasks';
GO

-- QuestionnaireResponses
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.QuestionnaireResponses') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'QuestionnaireResponses data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'QuestionnaireResponses';
GO

-- Rates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Rates') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Rates data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates';
GO

-- RateTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RateTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RateTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RateTypes';
GO

-- RateUnits
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RateUnits') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RateUnits data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RateUnits';
GO

-- Receiving
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Receiving') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Receiving data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Receiving';
GO

-- ReportSession
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ReportSession') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Reporting table for ReportSession', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReportSession';
GO

-- ReportSessionLinks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ReportSessionLinks') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Reporting table for ReportSessionLinks', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReportSessionLinks';
GO

-- ReqAudit
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ReqAudit') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for ReqAudit', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReqAudit';
GO

-- RequisitionChangeLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for RequisitionChangeLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog';
GO

-- RequisitionNoteEmails
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RequisitionNoteEmails') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RequisitionNoteEmails data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionNoteEmails';
GO

-- RequisitionNotes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RequisitionNotes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RequisitionNotes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionNotes';
GO

-- Requisitions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Requisitions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase requisition requests before PO creation', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions';
GO

-- ResetPasswordTracking
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ResetPasswordTracking') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ResetPasswordTracking data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ResetPasswordTracking';
GO

-- Rights
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Rights') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Rights data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rights';
GO

-- RightsLink
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RightsLink') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RightsLink data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RightsLink';
GO

-- RTK_2010NJHSL
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_2010NJHSL') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_2010NJHSL data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_2010NJHSL';
GO

-- RTK_CASFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_CASFile') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_CASFile data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_CASFile';
GO

-- RTK_ContainerCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_ContainerCodes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_ContainerCodes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ContainerCodes';
GO

-- RTK_Documents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Documents') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Documents data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Documents';
GO

-- RTK_FactSheets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_FactSheets') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_FactSheets data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_FactSheets';
GO

-- RTK_HealthHazardCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_HealthHazardCodes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_HealthHazardCodes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_HealthHazardCodes';
GO

-- RTK_Inventories
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Inventories') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Inventories data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Inventories';
GO

-- RTK_InventoryRangeCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_InventoryRangeCodes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_InventoryRangeCodes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_InventoryRangeCodes';
GO

-- RTK_Items
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Items') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Items data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items';
GO

-- RTK_LegacyDistrictCodesMap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_LegacyDistrictCodesMap') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_LegacyDistrictCodesMap data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacyDistrictCodesMap';
GO

-- RTK_LegacySchoolFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_LegacySchoolFile data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile';
GO

-- RTK_MixtureCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_MixtureCodes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_MixtureCodes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_MixtureCodes';
GO

-- RTK_MSDSDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_MSDSDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_MSDSDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_MSDSDetail';
GO

-- RTK_Purposes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Purposes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Purposes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Purposes';
GO

-- RTK_ReportItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_ReportItems') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Reporting table for RTK_ReportItems', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems';
GO

-- RTK_Sites
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Sites') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Sites data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites';
GO

-- RTK_Surveys
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Surveys') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Surveys data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Surveys';
GO

-- RTK_Training
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_Training') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_Training data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Training';
GO

-- RTK_UOMCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_UOMCodes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'RTK_UOMCodes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_UOMCodes';
GO

-- RTK_VendorLinks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.RTK_VendorLinks') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for RTK_VendorLinks', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_VendorLinks';
GO

-- SafetyDataSheets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SafetyDataSheets') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SafetyDataSheets data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SafetyDataSheets';
GO

-- Salutations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Salutations') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Salutations data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Salutations';
GO

-- SaxDups
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SaxDups') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SaxDups data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxDups';
GO

-- SaxNotifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SaxNotifications') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SaxNotifications data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications';
GO

-- ScanEvents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ScanEvents') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ScanEvents data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanEvents';
GO

-- ScanJobs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ScanJobs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ScanJobs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanJobs';
GO

-- ScannerZones
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ScannerZones') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ScannerZones data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScannerZones';
GO

-- ScheduledTask
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ScheduledTask') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ScheduledTask data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduledTask';
GO

-- ScheduleTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ScheduleTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ScheduleTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduleTypes';
GO

-- School
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.School') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'School data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School';
GO

-- SDS_Rpt_Bridge
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDS_Rpt_Bridge') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SDS_Rpt_Bridge data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDS_Rpt_Bridge';
GO

-- SDSDocs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDSDocs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SDSDocs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSDocs';
GO

-- SDSErrors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDSErrors') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SDSErrors data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSErrors';
GO

-- SDSLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDSLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for SDSLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSLog';
GO

-- SDSResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDSResults') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SDSResults data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSResults';
GO

-- SDSs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDSs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SDSs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSs';
GO

-- SDSSyncStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SDSSyncStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SDSSyncStatus data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSSyncStatus';
GO

-- SearchKeywords
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SearchKeywords') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SearchKeywords data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchKeywords';
GO

-- SearchSets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SearchSets') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SearchSets data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchSets';
GO

-- Sections
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Sections') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Sections data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sections';
GO

-- SecurityKeys
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SecurityKeys') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SecurityKeys data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityKeys';
GO

-- SecurityRoleKeys
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SecurityRoleKeys') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SecurityRoleKeys data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoleKeys';
GO

-- SecurityRoles
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SecurityRoles') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SecurityRoles data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoles';
GO

-- SecurityRoleUsers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SecurityRoleUsers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for SecurityRoleUsers', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoleUsers';
GO

-- Services
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Services') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Services data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services';
GO

-- SessionCmds
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SessionCmds') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SessionCmds data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionCmds';
GO

-- SessionTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SessionTable') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SessionTable data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable';
GO

-- ShipLocations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ShipLocations') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ShipLocations data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations';
GO

-- ShippingCosts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ShippingCosts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ShippingCosts data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingCosts';
GO

-- ShippingRequests
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ShippingRequests') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'ShippingRequests data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingRequests';
GO

-- ShippingVendor
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.ShippingVendor') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for ShippingVendor', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingVendor';
GO

-- SSOLoginTracking
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SSOLoginTracking') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for SSOLoginTracking', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SSOLoginTracking';
GO

-- States
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.States') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'States data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'States';
GO

-- StatusTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.StatusTable') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'StatusTable data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'StatusTable';
GO

-- Sulphite
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Sulphite') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Sulphite data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sulphite';
GO

-- SulphiteDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SulphiteDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SulphiteDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteDetail';
GO

-- SulphiteImport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SulphiteImport') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'SulphiteImport data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteImport';
GO

-- SulphiteUsers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.SulphiteUsers') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for SulphiteUsers', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteUsers';
GO

-- sysdiagrams
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.sysdiagrams') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'sysdiagrams data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'sysdiagrams';
GO

-- TableOfContents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TableOfContents') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TableOfContents data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TableOfContents';
GO

-- TagFile_
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TagFile_') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TagFile_ data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TagFile_';
GO

-- TAGFILEP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TAGFILEP') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TAGFILEP data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TAGFILEP';
GO

-- TagFilePos_
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TagFilePos_') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TagFilePos_ data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TagFilePos_';
GO

-- TagSet_
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TagSet_') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TagSet_ data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TagSet_';
GO

-- TaskEvent
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TaskEvent') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TaskEvent data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskEvent';
GO

-- TaskSchedule
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TaskSchedule') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TaskSchedule data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule';
GO

-- TempIrvingtonWincap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TempIrvingtonWincap') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TempIrvingtonWincap data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TempIrvingtonWincap';
GO

-- TM_UOM
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TM_UOM') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TM_UOM data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TM_UOM';
GO

-- TMAwards
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMAwards') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMAwards data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMAwards';
GO

-- TMImport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMImport') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMImport data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport';
GO

-- TMImport1
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMImport1') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMImport1 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport1';
GO

-- TMImport2
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMImport2') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMImport2 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport2';
GO

-- TMImport3
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMImport3') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMImport3 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport3';
GO

-- TMImport5
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMImport5') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMImport5 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport5';
GO

-- TMImport6
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMImport6') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMImport6 data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport6';
GO

-- TmpLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TmpLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for TmpLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpLog';
GO

-- TmpTaskSchedule
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TmpTaskSchedule') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TmpTaskSchedule data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpTaskSchedule';
GO

-- TMSurvey
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMSurvey') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMSurvey data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurvey';
GO

-- TMSurveyNewTrades
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMSurveyNewTrades') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMSurveyNewTrades data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewTrades';
GO

-- TMSurveyNewVendors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for TMSurveyNewVendors', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors';
GO

-- TMSurveyResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMSurveyResults') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TMSurveyResults data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyResults';
GO

-- TMVendors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TMVendors') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for TMVendors', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMVendors';
GO

-- TopUOM
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TopUOM') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TopUOM data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TopUOM';
GO

-- Trades
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Trades') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Trades data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Trades';
GO

-- TransactionLog_HISTORY
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TransactionLog_HISTORY') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for TransactionLog_HISTORY', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TransactionLog_HISTORY';
GO

-- TransactionLogCF
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TransactionLogCF') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for TransactionLogCF', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TransactionLogCF';
GO

-- TransactionTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TransactionTypes') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'TransactionTypes data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TransactionTypes';
GO

-- TransmitLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.TransmitLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Audit/logging table for TransmitLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TransmitLog';
GO

-- Units
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Units') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Units data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Units';
GO

-- UNSPSCs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UNSPSCs') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'UNSPSCs data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UNSPSCs';
GO

-- UnsubscriptionEmail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UnsubscriptionEmail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'UnsubscriptionEmail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UnsubscriptionEmail';
GO

-- UserAccounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UserAccounts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User login accounts and credentials', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts';
GO

-- UserAdminLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UserAdminLog') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for UserAdminLog', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAdminLog';
GO

-- UserCategory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UserCategory') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for UserCategory', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserCategory';
GO

-- UserImports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UserImports') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for UserImports', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserImports';
GO

-- Users
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Users') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User profile information', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users';
GO

-- UserTrees
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.UserTrees') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User/security table for UserTrees', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserTrees';
GO

-- VendorCatalogNote
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorCatalogNote') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorCatalogNote', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCatalogNote';
GO

-- VendorCategory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorCategory') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorCategory', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategory';
GO

-- VendorCategoryPP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorCategoryPP') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorCategoryPP', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategoryPP';
GO

-- VendorCertificates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorCertificates') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorCertificates', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCertificates';
GO

-- VendorContacts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorContacts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Contact persons at vendor companies', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts';
GO

-- VendorDeliveryRule
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorDeliveryRule') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorDeliveryRule', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDeliveryRule';
GO

-- VendorDocRequest
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorDocRequest') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorDocRequest', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest';
GO

-- VendorDocRequestDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorDocRequestDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail';
GO

-- VendorDocRequestStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorDocRequestStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorDocRequestStatus', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestStatus';
GO

-- VendorLocations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorLocations') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor address and location information', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorLocations';
GO

-- VendorLogoDisplays
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorLogoDisplays') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorLogoDisplays', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorLogoDisplays';
GO

-- VendorOrders
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorOrders') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorOrders', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorOrders';
GO

-- VendorOverrideMessages
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorOverrideMessages') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorOverrideMessages', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorOverrideMessages';
GO

-- VendorPOtags
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorPOtags') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorPOtags', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorPOtags';
GO

-- VendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQuery') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQuery', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery';
GO

-- VendorQueryDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail';
GO

-- VendorQueryMSRP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryMSRP', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP';
GO

-- VendorQueryMSRPDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryMSRPDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail';
GO

-- VendorQueryMSRPStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryMSRPStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryMSRPStatus', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPStatus';
GO

-- VendorQueryStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryStatus', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryStatus';
GO

-- VendorQueryTandM
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryTandM') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryTandM', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM';
GO

-- VendorQueryTandMDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryTandMDetail', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail';
GO

-- VendorQueryTandMStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorQueryTandMStatus') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorQueryTandMStatus', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMStatus';
GO

-- Vendors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.Vendors') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Master vendor/supplier records with contact information', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors';
GO

-- VendorSessions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorSessions') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorSessions', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorSessions';
GO

-- VendorUploads
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VendorUploads') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VendorUploads', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorUploads';
GO

-- VPOLoginAttempts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VPOLoginAttempts') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for VPOLoginAttempts', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOLoginAttempts';
GO

-- VPORegistrations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VPORegistrations') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Purchase order table for VPORegistrations', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPORegistrations';
GO

-- VPOVendorLinks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.VPOVendorLinks') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Vendor management table for VPOVendorLinks', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOVendorLinks';
GO

-- WizHelpFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.WizHelpFile') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'WizHelpFile data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'WizHelpFile';
GO

-- YearlyTotals
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.YearlyTotals') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'YearlyTotals data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'YearlyTotals';
GO

-- z4zbBidFix
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.z4zbBidFix') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Bidding system table for z4zbBidFix', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix';
GO

-- z4zbReqDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('dbo.z4zbReqDetail') AND minor_id = 0 AND name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'z4zbReqDetail data table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail';
GO


-- ============================================
-- COLUMN DESCRIPTIONS
-- ============================================


-- Table: AccountingDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingDetail') AND c.name = 'AccountingDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AccountingDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingDetail', @level2type = N'COLUMN', @level2name = N'AccountingDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingDetail') AND c.name = 'UserAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingDetail', @level2type = N'COLUMN', @level2name = N'UserAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingDetail') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingDetail', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingDetail') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingDetail', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingDetail') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingDetail', @level2type = N'COLUMN', @level2name = N'Amount';
GO

-- Table: AccountingFormats
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingFormats') AND c.name = 'AccountingFormatId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AccountingFormats table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingFormats', @level2type = N'COLUMN', @level2name = N'AccountingFormatId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingFormats') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingFormats', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingFormats') AND c.name = 'ShortName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingFormats', @level2type = N'COLUMN', @level2name = N'ShortName';
GO

-- Table: AccountingUserFields
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingUserFields') AND c.name = 'AccountingUserFieldId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AccountingUserFields table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingUserFields', @level2type = N'COLUMN', @level2name = N'AccountingUserFieldId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingUserFields') AND c.name = 'AccountingFormatId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AccountingFormats table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingUserFields', @level2type = N'COLUMN', @level2name = N'AccountingFormatId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingUserFields') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingUserFields', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountingUserFields') AND c.name = 'FieldName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountingUserFields', @level2type = N'COLUMN', @level2name = N'FieldName';
GO

-- Table: Accounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Accounts') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Accounts', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Accounts') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Accounts', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Accounts') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Accounts', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Accounts') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Accounts', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Accounts') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Accounts', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: AccountSeparators
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountSeparators') AND c.name = 'AccountSeparatorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AccountSeparators table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountSeparators', @level2type = N'COLUMN', @level2name = N'AccountSeparatorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountSeparators') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountSeparators', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AccountSeparators') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AccountSeparators', @level2type = N'COLUMN', @level2name = N'Code';
GO

-- Table: AddendumItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'PriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Prices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'PriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'CatalogName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'CatalogName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AddendumItems') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AddendumItems', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: allitems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.allitems') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'allitems', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO

-- Table: AnswerTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AnswerTypes') AND c.name = 'AnswerTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AnswerTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AnswerTypes', @level2type = N'COLUMN', @level2name = N'AnswerTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AnswerTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AnswerTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: ApprovalLevels
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ApprovalLevels') AND c.name = 'ApprovalLevelId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ApprovalLevels table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalLevels', @level2type = N'COLUMN', @level2name = N'ApprovalLevelId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ApprovalLevels') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalLevels', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Approvals
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Approvals') AND c.name = 'ApprovalId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Approvals table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Approvals', @level2type = N'COLUMN', @level2name = N'ApprovalId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Approvals') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Approvals', @level2type = N'COLUMN', @level2name = N'StatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Approvals') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Approvals', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO

-- Table: ApprovalsHistory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ApprovalsHistory') AND c.name = 'ApprovalId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Approvals table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalsHistory', @level2type = N'COLUMN', @level2name = N'ApprovalId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ApprovalsHistory') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalsHistory', @level2type = N'COLUMN', @level2name = N'StatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ApprovalsHistory') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ApprovalsHistory', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO

-- Table: Audit
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Audit') AND c.name = 'AuditId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Audit table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Audit', @level2type = N'COLUMN', @level2name = N'AuditId';
GO

-- Table: Awardings
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awardings') AND c.name = 'AwardingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awardings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awardings', @level2type = N'COLUMN', @level2name = N'AwardingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awardings') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awardings', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: Awards
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'BidStartDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective start date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'BidStartDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'BidEndDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective end date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'BidEndDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Awards') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Awards', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO

-- Table: AwardsCatalogList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AwardsCatalogList') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AwardsCatalogList', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AwardsCatalogList') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AwardsCatalogList', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: AwardTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AwardTypes') AND c.name = 'AwardTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AwardTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AwardTypes', @level2type = N'COLUMN', @level2name = N'AwardTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.AwardTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'AwardTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: BatchBook
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'BatchBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchBook table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'BatchBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'CometCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'CometCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'AccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'AccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'BudgetAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BudgetAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'BudgetAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'UserAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'UserAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'InputAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'InputAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'CalcAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'CalcAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchBook') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchBook', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO

-- Table: BatchDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'BatchDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'BatchDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'BatchBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchBook table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'BatchBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'BookAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'BookAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'OrigDistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'OrigDistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'OrigCometCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'OrigCometCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'OrigItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'OrigItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'OrigQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'OrigQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'ModifiedBy' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User who last modified the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'ModifiedBy';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'OrigBookAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'OrigBookAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'BatchFileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'BatchFileName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: BatchDetailInserts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetailInserts') AND c.name = 'BatchDetailInsertId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchDetailInserts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetailInserts', @level2type = N'COLUMN', @level2name = N'BatchDetailInsertId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetailInserts') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetailInserts', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetailInserts') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetailInserts', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BatchDetailInserts') AND c.name = 'BatchDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BatchDetailInserts', @level2type = N'COLUMN', @level2name = N'BatchDetailId';
GO

-- Table: Batches
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Batches') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Batches', @level2type = N'COLUMN', @level2name = N'Amount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Batches') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Batches', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: BidAnswers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidAnswers') AND c.name = 'BidAnswerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidAnswers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswers', @level2type = N'COLUMN', @level2name = N'BidAnswerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidAnswers') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswers', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidAnswers') AND c.name = 'BidQuestionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidQuestions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswers', @level2type = N'COLUMN', @level2name = N'BidQuestionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidAnswers') AND c.name = 'BidTradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidTrades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswers', @level2type = N'COLUMN', @level2name = N'BidTradeId';
GO

-- Table: BidAnswersJournal
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidAnswersJournal') AND c.name = 'BidAnswerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidAnswers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidAnswersJournal', @level2type = N'COLUMN', @level2name = N'BidAnswerId';
GO

-- Table: BidCalendar
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'CalendarId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Calendars table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'CalendarId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'CategoryName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'CategoryName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'StateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidCalendar') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidCalendar', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO

-- Table: BidderCheckList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckList') AND c.name = 'BidderCheckListId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidderCheckList table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckList', @level2type = N'COLUMN', @level2name = N'BidderCheckListId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckList') AND c.name = 'DocumentName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckList', @level2type = N'COLUMN', @level2name = N'DocumentName';
GO

-- Table: BidderCheckListPkgDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckListPkgDetail') AND c.name = 'BidderCheckListPkgDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidderCheckListPkgDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgDetail', @level2type = N'COLUMN', @level2name = N'BidderCheckListPkgDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckListPkgDetail') AND c.name = 'BidderCheckListPkgHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgDetail', @level2type = N'COLUMN', @level2name = N'BidderCheckListPkgHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckListPkgDetail') AND c.name = 'BidderCheckListId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidderCheckList table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgDetail', @level2type = N'COLUMN', @level2name = N'BidderCheckListId';
GO

-- Table: BidderCheckListPkgHeader
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckListPkgHeader') AND c.name = 'BidderCheckListPkgHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgHeader', @level2type = N'COLUMN', @level2name = N'BidderCheckListPkgHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidderCheckListPkgHeader') AND c.name = 'PackageName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidderCheckListPkgHeader', @level2type = N'COLUMN', @level2name = N'PackageName';
GO

-- Table: BidDocument
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidDocument') AND c.name = 'BidDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidDocument table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocument', @level2type = N'COLUMN', @level2name = N'BidDocumentId';
GO

-- Table: BidDocumentTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidDocumentTypes') AND c.name = 'BidDocumentTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidDocumentTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocumentTypes', @level2type = N'COLUMN', @level2name = N'BidDocumentTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidDocumentTypes') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocumentTypes', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidDocumentTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocumentTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidDocumentTypes') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidDocumentTypes', @level2type = N'COLUMN', @level2name = N'State';
GO

-- Table: BidHeaderCheckList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderCheckList') AND c.name = 'BidHeaderCheckListId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidHeaderCheckList table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderCheckList', @level2type = N'COLUMN', @level2name = N'BidHeaderCheckListId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderCheckList') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderCheckList', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderCheckList') AND c.name = 'BidderCheckListId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidderCheckList table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderCheckList', @level2type = N'COLUMN', @level2name = N'BidderCheckListId';
GO

-- Table: BidHeaderDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail') AND c.name = 'BidHeaderDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidHeaderDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO

-- Table: BidHeaderDetail_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail_Orig') AND c.name = 'BidHeaderDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidHeaderDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail_Orig', @level2type = N'COLUMN', @level2name = N'BidHeaderDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail_Orig') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail_Orig', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail_Orig') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail_Orig', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail_Orig') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail_Orig', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDetail_Orig') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDetail_Orig', @level2type = N'COLUMN', @level2name = N'Quantity';
GO

-- Table: BidHeaderDocument
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDocument') AND c.name = 'BidHeaderDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidHeaderDocuments table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocument', @level2type = N'COLUMN', @level2name = N'BidHeaderDocumentId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDocument') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocument', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDocument') AND c.name = 'BidDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidDocument table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocument', @level2type = N'COLUMN', @level2name = N'BidDocumentId';
GO

-- Table: BidHeaderDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDocuments') AND c.name = 'BidHeaderDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidHeaderDocuments table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocuments', @level2type = N'COLUMN', @level2name = N'BidHeaderDocumentId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaderDocuments') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaderDocuments', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: BidHeaders
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'MinimumPOAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'MinimumPOAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'ParentBidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'ParentBidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'CalendarId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Calendars table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'CalendarId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'StateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'HostDistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'HostDistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidHeaders') AND c.name = 'BidManagerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidManagers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidHeaders', @level2type = N'COLUMN', @level2name = N'BidManagerId';
GO

-- Table: BidImportCatalogList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImportCatalogList') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImportCatalogList', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImportCatalogList') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImportCatalogList', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: BidImportCounties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImportCounties') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImportCounties', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO

-- Table: BidImports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'AdditionalHandlingAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'AdditionalHandlingAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'FreeHandlingAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'FreeHandlingAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'ContactEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'ContactEmail';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'ContactName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidImports') AND c.name = 'ContactPhone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidImports', @level2type = N'COLUMN', @level2name = N'ContactPhone';
GO

-- Table: BidItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'BidQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'BidQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'PackedItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'PackedItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO

-- Table: BidItems_Old
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'BidQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'BidQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'PackedItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'PackedItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidItems_Old') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidItems_Old', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO

-- Table: BidManagers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManagers') AND c.name = 'BidManagerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidManagers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManagers', @level2type = N'COLUMN', @level2name = N'BidManagerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManagers') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManagers', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManagers') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManagers', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManagers') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManagers', @level2type = N'COLUMN', @level2name = N'Phone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManagers') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManagers', @level2type = N'COLUMN', @level2name = N'Email';
GO

-- Table: BidManufacturers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManufacturers') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManufacturers', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidManufacturers') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidManufacturers', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO

-- Table: BidMappedItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMappedItems') AND c.name = 'BidMappedItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMappedItems', @level2type = N'COLUMN', @level2name = N'BidMappedItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMappedItems') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMappedItems', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMappedItems') AND c.name = 'OrigItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMappedItems', @level2type = N'COLUMN', @level2name = N'OrigItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMappedItems') AND c.name = 'NewItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMappedItems', @level2type = N'COLUMN', @level2name = N'NewItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMappedItems') AND c.name = 'ReasonCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMappedItems', @level2type = N'COLUMN', @level2name = N'ReasonCode';
GO

-- Table: BidMgrConfiguration
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMgrConfiguration') AND c.name = 'BidMgrConfigurationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMgrConfiguration table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMgrConfiguration', @level2type = N'COLUMN', @level2name = N'BidMgrConfigurationId';
GO

-- Table: BidMgrTagFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMgrTagFile') AND c.name = 'BidMgrTagFileId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMgrTagFile table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMgrTagFile', @level2type = N'COLUMN', @level2name = N'BidMgrTagFileId';
GO

-- Table: BidMSRPResultPrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultPrices') AND c.name = 'BidMSRPResultPricesId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMSRPResultPrices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultPrices', @level2type = N'COLUMN', @level2name = N'BidMSRPResultPricesId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultPrices') AND c.name = 'BidMSRPResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMSRPResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultPrices', @level2type = N'COLUMN', @level2name = N'BidMSRPResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultPrices') AND c.name = 'BidMSRPResultsProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMSRPResultsProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultPrices', @level2type = N'COLUMN', @level2name = N'BidMSRPResultsProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultPrices') AND c.name = 'BidRequestPriceRangeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestPriceRanges table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultPrices', @level2type = N'COLUMN', @level2name = N'BidRequestPriceRangeId';
GO

-- Table: BidMSRPResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'BidMSRPResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMSRPResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'BidMSRPResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'VendorNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'VendorNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'BidRequestManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestManufacturer table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'BidRequestManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResults') AND c.name = 'PriceListTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PriceListTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResults', @level2type = N'COLUMN', @level2name = N'PriceListTypeId';
GO

-- Table: BidMSRPResultsProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'BidMSRPResultsProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMSRPResultsProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'BidMSRPResultsProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'BidMSRPResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidMSRPResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'BidMSRPResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'BidRequestProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'BidRequestProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'WriteInProductLineName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'WriteInProductLineName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'BidRequestOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'BidRequestOptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'MSRPOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSRPOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'MSRPOptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'OptionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'OptionName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidMSRPResultsProductLines') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidMSRPResultsProductLines', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO

-- Table: BidPackage
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidPackage') AND c.name = 'BidPackageId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidPackage table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackage', @level2type = N'COLUMN', @level2name = N'BidPackageId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidPackage') AND c.name = 'BidPackageName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackage', @level2type = N'COLUMN', @level2name = N'BidPackageName';
GO

-- Table: BidPackageDocument
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidPackageDocument') AND c.name = 'BidPackageDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidPackageDocument table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackageDocument', @level2type = N'COLUMN', @level2name = N'BidPackageDocumentId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidPackageDocument') AND c.name = 'BidPackageId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidPackage table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackageDocument', @level2type = N'COLUMN', @level2name = N'BidPackageId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidPackageDocument') AND c.name = 'BidDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidDocument table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidPackageDocument', @level2type = N'COLUMN', @level2name = N'BidDocumentId';
GO

-- Table: BidProductLinePrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidProductLinePrices') AND c.name = 'BidProductLinePriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidProductLinePrices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLinePrices', @level2type = N'COLUMN', @level2name = N'BidProductLinePriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidProductLinePrices') AND c.name = 'BidProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLinePrices', @level2type = N'COLUMN', @level2name = N'BidProductLineId';
GO

-- Table: BidProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidProductLines') AND c.name = 'BidProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLines', @level2type = N'COLUMN', @level2name = N'BidProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidProductLines') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLines', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidProductLines') AND c.name = 'MSRPOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSRPOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidProductLines', @level2type = N'COLUMN', @level2name = N'MSRPOptionId';
GO

-- Table: BidQuestions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidQuestions') AND c.name = 'BidQuestionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidQuestions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidQuestions', @level2type = N'COLUMN', @level2name = N'BidQuestionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidQuestions') AND c.name = 'BidTradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidTrades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidQuestions', @level2type = N'COLUMN', @level2name = N'BidTradeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidQuestions') AND c.name = 'AnswerTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AnswerTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidQuestions', @level2type = N'COLUMN', @level2name = N'AnswerTypeId';
GO

-- Table: BidReawards
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidReawards') AND c.name = 'BidReawardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidReawards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidReawards', @level2type = N'COLUMN', @level2name = N'BidReawardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidReawards') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidReawards', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: BidRequestItemMergeActions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions') AND c.name = 'BidRequestItemMergeActionsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestItemMergeActions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions', @level2type = N'COLUMN', @level2name = N'BidRequestItemMergeActionsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions') AND c.name = 'DestinationBidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions', @level2type = N'COLUMN', @level2name = N'DestinationBidRequestItemId';
GO

-- Table: BidRequestItemMergeActions_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Orig') AND c.name = 'BidRequestItemMergeActionsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestItemMergeActions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Orig', @level2type = N'COLUMN', @level2name = N'BidRequestItemMergeActionsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Orig') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Orig', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Orig') AND c.name = 'DestinationBidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Orig', @level2type = N'COLUMN', @level2name = N'DestinationBidRequestItemId';
GO

-- Table: BidRequestItemMergeActions_Saved_101521
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Saved_101521') AND c.name = 'BidRequestItemMergeActionsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestItemMergeActions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Saved_101521', @level2type = N'COLUMN', @level2name = N'BidRequestItemMergeActionsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Saved_101521') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Saved_101521', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItemMergeActions_Saved_101521') AND c.name = 'DestinationBidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItemMergeActions_Saved_101521', @level2type = N'COLUMN', @level2name = N'DestinationBidRequestItemId';
GO

-- Table: BidRequestItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems') AND c.name = 'BidRequestAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems', @level2type = N'COLUMN', @level2name = N'BidRequestAmount';
GO

-- Table: BidRequestItems_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems_Orig') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems_Orig', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems_Orig') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems_Orig', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems_Orig') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems_Orig', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems_Orig') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems_Orig', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestItems_Orig') AND c.name = 'BidRequestAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestItems_Orig', @level2type = N'COLUMN', @level2name = N'BidRequestAmount';
GO

-- Table: BidRequestManufacturer
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestManufacturer') AND c.name = 'BidRequestManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestManufacturer table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestManufacturer', @level2type = N'COLUMN', @level2name = N'BidRequestManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestManufacturer') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestManufacturer', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestManufacturer') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestManufacturer', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO

-- Table: BidRequestOptions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'BidRequestOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'BidRequestOptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'OptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Options table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'OptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'BidRequestManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestManufacturer table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'BidRequestManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'BidRequestProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'BidRequestProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestOptions') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestOptions', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: BidRequestPriceRanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestPriceRanges') AND c.name = 'BidRequestPriceRangeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestPriceRanges table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestPriceRanges', @level2type = N'COLUMN', @level2name = N'BidRequestPriceRangeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestPriceRanges') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestPriceRanges', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestPriceRanges') AND c.name = 'BidRequestManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestManufacturer table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestPriceRanges', @level2type = N'COLUMN', @level2name = N'BidRequestManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestPriceRanges') AND c.name = 'BidRequestProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestPriceRanges', @level2type = N'COLUMN', @level2name = N'BidRequestProductLineId';
GO

-- Table: BidRequestProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestProductLines') AND c.name = 'BidRequestProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestProductLines', @level2type = N'COLUMN', @level2name = N'BidRequestProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestProductLines') AND c.name = 'BidRequestManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidRequestManufacturer table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestProductLines', @level2type = N'COLUMN', @level2name = N'BidRequestManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidRequestProductLines') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidRequestProductLines', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO

-- Table: BidResponses
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResponses') AND c.name = 'BidResponseId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResponses table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResponses', @level2type = N'COLUMN', @level2name = N'BidResponseId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResponses') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResponses', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResponses') AND c.name = 'BidQuestionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidQuestions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResponses', @level2type = N'COLUMN', @level2name = N'BidQuestionId';
GO

-- Table: BidResultChanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultChanges') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultChanges', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultChanges') AND c.name = 'PrevUnitPrice' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Price per unit', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultChanges', @level2type = N'COLUMN', @level2name = N'PrevUnitPrice';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultChanges') AND c.name = 'NewUnitPrice' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Price per unit', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultChanges', @level2type = N'COLUMN', @level2name = N'NewUnitPrice';
GO

-- Table: BidResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'UnitPrice' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Price per unit', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'UnitPrice';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'ModifiedDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Last modification timestamp', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'ModifiedDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'ModifiedBy' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User who last modified the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'ModifiedBy';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults') AND c.name = 'MinimumOrderQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults', @level2type = N'COLUMN', @level2name = N'MinimumOrderQuantity';
GO

-- Table: BidResults_Orig
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'BidRequestItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'BidRequestItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'UnitPrice' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Price per unit', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'UnitPrice';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'ModifiedDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Last modification timestamp', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'ModifiedDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResults_Orig') AND c.name = 'ModifiedBy' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User who last modified the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResults_Orig', @level2type = N'COLUMN', @level2name = N'ModifiedBy';
GO

-- Table: BidResultsChangeLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultsChangeLog') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultsChangeLog', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultsChangeLog') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultsChangeLog', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultsChangeLog') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultsChangeLog', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultsChangeLog') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultsChangeLog', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidResultsChangeLog') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidResultsChangeLog', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: Bids
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'CoopId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Coops table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'CoopId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'AdditionalHandlingAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'AdditionalHandlingAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Bids') AND c.name = 'FreeHandlingAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Bids', @level2type = N'COLUMN', @level2name = N'FreeHandlingAmount';
GO

-- Table: BidsCatalogList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidsCatalogList') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidsCatalogList', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidsCatalogList') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidsCatalogList', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: BidTradeCounties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidTradeCounties') AND c.name = 'BidTradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidTrades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTradeCounties', @level2type = N'COLUMN', @level2name = N'BidTradeId';
GO

-- Table: BidTrades
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidTrades') AND c.name = 'BidTradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidTrades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTrades', @level2type = N'COLUMN', @level2name = N'BidTradeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidTrades') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTrades', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidTrades') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTrades', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: BidTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidTypes') AND c.name = 'BidTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTypes', @level2type = N'COLUMN', @level2name = N'BidTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BidTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BidTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: BookTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BookTypes') AND c.name = 'BookTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BookTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BookTypes', @level2type = N'COLUMN', @level2name = N'BookTypeId';
GO

-- Table: BudgetAccounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BudgetAccounts') AND c.name = 'BudgetAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BudgetAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BudgetAccounts', @level2type = N'COLUMN', @level2name = N'BudgetAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BudgetAccounts') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BudgetAccounts', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BudgetAccounts') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BudgetAccounts', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.BudgetAccounts') AND c.name = 'BudgetAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'BudgetAccounts', @level2type = N'COLUMN', @level2name = N'BudgetAmount';
GO

-- Table: Budgets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Budgets') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Budgets', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Budgets') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Budgets', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Budgets') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Budgets', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Budgets') AND c.name = 'StartDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective start date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Budgets', @level2type = N'COLUMN', @level2name = N'StartDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Budgets') AND c.name = 'EndDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective end date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Budgets', @level2type = N'COLUMN', @level2name = N'EndDate';
GO

-- Table: CalDistricts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalDistricts') AND c.name = 'CalDistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalDistricts', @level2type = N'COLUMN', @level2name = N'CalDistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalDistricts') AND c.name = 'CalendarId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Calendars table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalDistricts', @level2type = N'COLUMN', @level2name = N'CalendarId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalDistricts') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalDistricts', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: CalendarDates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarDates') AND c.name = 'CalendarDateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CalendarDates table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarDates', @level2type = N'COLUMN', @level2name = N'CalendarDateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarDates') AND c.name = 'CalendarId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Calendars table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarDates', @level2type = N'COLUMN', @level2name = N'CalendarId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarDates') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarDates', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: CalendarIB
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarIB') AND c.name = 'CalendarIBId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CalendarIB table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarIB', @level2type = N'COLUMN', @level2name = N'CalendarIBId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarIB') AND c.name = 'CalendarId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Calendars table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarIB', @level2type = N'COLUMN', @level2name = N'CalendarId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarIB') AND c.name = 'CalendarTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CalendarTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarIB', @level2type = N'COLUMN', @level2name = N'CalendarTypeId';
GO

-- Table: CalendarItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarItems') AND c.name = 'CalendarItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarItems', @level2type = N'COLUMN', @level2name = N'CalendarItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarItems') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarItems', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Calendars
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Calendars') AND c.name = 'CalendarId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Calendars table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Calendars', @level2type = N'COLUMN', @level2name = N'CalendarId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Calendars') AND c.name = 'CalendarTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CalendarTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Calendars', @level2type = N'COLUMN', @level2name = N'CalendarTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Calendars') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Calendars', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: CalendarTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarTypes') AND c.name = 'CalendarTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CalendarTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarTypes', @level2type = N'COLUMN', @level2name = N'CalendarTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CalendarTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CalendarTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Carolina Living Items
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Carolina Living Items') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Carolina Living Items', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Catalog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Catalog') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Catalog') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Catalog') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Catalog') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Catalog') AND c.name = 'DisplayedVendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog', @level2type = N'COLUMN', @level2name = N'DisplayedVendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Catalog') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Catalog', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: CatalogImportFields
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogImportFields') AND c.name = 'CatalogImportFieldId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogImportFields table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportFields', @level2type = N'COLUMN', @level2name = N'CatalogImportFieldId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogImportFields') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportFields', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: CatalogImportMap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogImportMap') AND c.name = 'CatalogImportMapId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogImportMap table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportMap', @level2type = N'COLUMN', @level2name = N'CatalogImportMapId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogImportMap') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportMap', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogImportMap') AND c.name = 'CatalogImportFieldId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogImportFields table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogImportMap', @level2type = N'COLUMN', @level2name = N'CatalogImportFieldId';
GO

-- Table: CatalogPricing
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogPricing') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogPricing', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogPricing') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogPricing', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogPricing') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogPricing', @level2type = N'COLUMN', @level2name = N'BidId';
GO

-- Table: CatalogRequest
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequest') AND c.name = 'CatalogRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogRequest table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest', @level2type = N'COLUMN', @level2name = N'CatalogRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequest') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequest') AND c.name = 'EmailAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest', @level2type = N'COLUMN', @level2name = N'EmailAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequest') AND c.name = 'EmailCCAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest', @level2type = N'COLUMN', @level2name = N'EmailCCAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequest') AND c.name = 'CatalogRequestNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest', @level2type = N'COLUMN', @level2name = N'CatalogRequestNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequest') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequest', @level2type = N'COLUMN', @level2name = N'ContactName';
GO

-- Table: CatalogRequestDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestDetail') AND c.name = 'CatalogRequestDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogRequestDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestDetail', @level2type = N'COLUMN', @level2name = N'CatalogRequestDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestDetail') AND c.name = 'CatalogRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogRequest table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestDetail', @level2type = N'COLUMN', @level2name = N'CatalogRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestDetail') AND c.name = 'CatalogRequestNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestDetail', @level2type = N'COLUMN', @level2name = N'CatalogRequestNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestDetail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestDetail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: CatalogRequestStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestStatus') AND c.name = 'CatalogRequestStatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestStatus', @level2type = N'COLUMN', @level2name = N'CatalogRequestStatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestStatus') AND c.name = 'CatalogRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogRequest table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestStatus', @level2type = N'COLUMN', @level2name = N'CatalogRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogRequestStatus') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogRequestStatus', @level2type = N'COLUMN', @level2name = N'StatusId';
GO

-- Table: CatalogText
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogText') AND c.name = 'CatalogTextId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogText table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogText', @level2type = N'COLUMN', @level2name = N'CatalogTextId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogText') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogText', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogText') AND c.name = 'BaseFileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogText', @level2type = N'COLUMN', @level2name = N'BaseFileName';
GO

-- Table: CatalogTextParts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogTextParts') AND c.name = 'CatalogTextPartId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogTextParts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogTextParts', @level2type = N'COLUMN', @level2name = N'CatalogTextPartId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatalogTextParts') AND c.name = 'CatalogTextId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CatalogText table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatalogTextParts', @level2type = N'COLUMN', @level2name = N'CatalogTextId';
GO

-- Table: Category
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Category') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Category', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Category') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Category', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Category') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Category', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Category') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Category', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: CatList
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'CategoryName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'CategoryName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'PriceplanCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'PriceplanCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'SchoolName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'SchoolName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'SchoolAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'SchoolAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'SchoolCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'SchoolCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'SchoolState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'SchoolState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CatList') AND c.name = 'SchoolZip' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Postal/ZIP code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CatList', @level2type = N'COLUMN', @level2name = N'SchoolZip';
GO

-- Table: CertificateAuthority
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CertificateAuthority') AND c.name = 'CertificateAuthorityId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CertificateAuthority table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CertificateAuthority', @level2type = N'COLUMN', @level2name = N'CertificateAuthorityId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CertificateAuthority') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CertificateAuthority', @level2type = N'COLUMN', @level2name = N'StateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CertificateAuthority') AND c.name = 'CertificateName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CertificateAuthority', @level2type = N'COLUMN', @level2name = N'CertificateName';
GO

-- Table: ChargeTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ChargeTypes') AND c.name = 'ChargeTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ChargeTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ChargeTypes', @level2type = N'COLUMN', @level2name = N'ChargeTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ChargeTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ChargeTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ChargeTypes') AND c.name = 'AccountingChargeCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ChargeTypes', @level2type = N'COLUMN', @level2name = N'AccountingChargeCode';
GO

-- Table: CommonMSRPVendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CommonMSRPVendorQuery') AND c.name = 'CommonMSRPVendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CommonMSRPVendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonMSRPVendorQuery', @level2type = N'COLUMN', @level2name = N'CommonMSRPVendorQueryId';
GO

-- Table: CommonTandMVendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CommonTandMVendorQuery') AND c.name = 'CommonTandMVendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CommonTandMVendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonTandMVendorQuery', @level2type = N'COLUMN', @level2name = N'CommonTandMVendorQueryId';
GO

-- Table: CommonVendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CommonVendorQuery') AND c.name = 'CommonVendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CommonVendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonVendorQuery', @level2type = N'COLUMN', @level2name = N'CommonVendorQueryId';
GO

-- Table: CommonVendorQueryAnswer
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CommonVendorQueryAnswer') AND c.name = 'CommonVendorQueryAnswerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CommonVendorQueryAnswer table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonVendorQueryAnswer', @level2type = N'COLUMN', @level2name = N'CommonVendorQueryAnswerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CommonVendorQueryAnswer') AND c.name = 'CommonVendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CommonVendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CommonVendorQueryAnswer', @level2type = N'COLUMN', @level2name = N'CommonVendorQueryId';
GO

-- Table: Control
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Control') AND c.name = 'ControlId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Control table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Control', @level2type = N'COLUMN', @level2name = N'ControlId';
GO

-- Table: Coops
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Coops') AND c.name = 'CoopId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Coops table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Coops', @level2type = N'COLUMN', @level2name = N'CoopId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Coops') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Coops', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Coops') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Coops', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: CopyRequests
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CopyRequests') AND c.name = 'CopyRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CopyRequests table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CopyRequests', @level2type = N'COLUMN', @level2name = N'CopyRequestId';
GO

-- Table: Counties
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Counties') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Counties', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Counties') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Counties', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Counties') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Counties', @level2type = N'COLUMN', @level2name = N'StateId';
GO

-- Table: CoverView
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'DistrictCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'DistrictCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'DistrictState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'DistrictState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'SchoolName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'SchoolName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'SchoolCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'SchoolCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'SchoolState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'SchoolState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'UserName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'UserName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'AccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'AccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'BudgetStartDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective start date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'BudgetStartDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'BudgetEndDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective end date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'BudgetEndDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'OrderBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBooks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'OrderBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'CategoryDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'CategoryDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'PricePlanDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'PricePlanDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'StateName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'StateName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CoverView') AND c.name = 'CoverViewId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CoverView table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CoverView', @level2type = N'COLUMN', @level2name = N'CoverViewId';
GO

-- Table: CrossRefs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'FullDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'FullDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'ShortDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'ShortDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'ImageId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Images table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'ImageId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CrossRefs') AND c.name = 'MinimumOrderQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CrossRefs', @level2type = N'COLUMN', @level2name = N'MinimumOrderQuantity';
GO

-- Table: CSCommands
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSCommands') AND c.name = 'CSCommandId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CSCommands table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSCommands', @level2type = N'COLUMN', @level2name = N'CSCommandId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSCommands') AND c.name = 'FullDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSCommands', @level2type = N'COLUMN', @level2name = N'FullDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSCommands') AND c.name = 'SecurityRoleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SecurityRoles table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSCommands', @level2type = N'COLUMN', @level2name = N'SecurityRoleId';
GO

-- Table: CSMessageFiles
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSMessageFiles') AND c.name = 'CSFileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSMessageFiles', @level2type = N'COLUMN', @level2name = N'CSFileName';
GO

-- Table: CSRep
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSRep') AND c.name = 'CSRepId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CSRep table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSRep', @level2type = N'COLUMN', @level2name = N'CSRepId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSRep') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSRep', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSRep') AND c.name = 'ID' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSRep', @level2type = N'COLUMN', @level2name = N'ID';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSRep') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSRep', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CSRep') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CSRep', @level2type = N'COLUMN', @level2name = N'Phone';
GO

-- Table: CXmlSession
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CXmlSession') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CXmlSession') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CXmlSession') AND c.name = 'BudgetAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BudgetAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession', @level2type = N'COLUMN', @level2name = N'BudgetAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CXmlSession') AND c.name = 'UserAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession', @level2type = N'COLUMN', @level2name = N'UserAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CXmlSession') AND c.name = 'AccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession', @level2type = N'COLUMN', @level2name = N'AccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.CXmlSession') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'CXmlSession', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO

-- Table: dchtest
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'Amount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'BudgetName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'BudgetName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'AccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'AccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictNameAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictNameAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'SchoolName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'SchoolName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'SchoolNameAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'SchoolNameAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorPhone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorPhone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictVendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictVendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorNameAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorNameAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'CategoryCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'CategoryCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'CategoryName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'CategoryName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DiscountAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DiscountAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'LocationCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'LocationCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'ShippingAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'ShippingAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'ShippingNameAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'ShippingNameAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'DistrictState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'DistrictState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'SchoolCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'SchoolCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'SchoolState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'SchoolState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorsCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorsCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'VendorsState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'VendorsState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'ShipLocationsCity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'ShipLocationsCity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'ShipLocationsState' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'ShipLocationsState';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'ShipLocationsName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'ShipLocationsName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'UsersDistrictAcctgCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'UsersDistrictAcctgCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.dchtest') AND c.name = 'AwardsBidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'dchtest', @level2type = N'COLUMN', @level2name = N'AwardsBidHeaderId';
GO

-- Table: Detail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'LastYearsQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'LastYearsQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'PriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Prices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'PriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'BatchDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'BatchDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'ExtraDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'ExtraDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'SectionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Sections table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'SectionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'SectionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'SectionName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'OriginalItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'OriginalItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'KeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Keywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'KeywordId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'ShippingQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'ShippingQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'DoctorsName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'DoctorsName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'DigitallyDeliveredEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'DigitallyDeliveredEmail';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Detail') AND c.name = 'MinimumOrderQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Detail', @level2type = N'COLUMN', @level2name = N'MinimumOrderQuantity';
GO

-- Table: DetailChangeLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'DetailChangeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DetailChanges table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'DetailChangeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'OrigBidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'OrigBidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'NewBidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'NewBidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'OrigVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'OrigVendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChangeLog') AND c.name = 'NewVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChangeLog', @level2type = N'COLUMN', @level2name = N'NewVendorId';
GO

-- Table: DetailChanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChanges') AND c.name = 'DetailChangeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DetailChanges table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChanges', @level2type = N'COLUMN', @level2name = N'DetailChangeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChanges') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChanges', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChanges') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChanges', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChanges') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChanges', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailChanges') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailChanges', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO

-- Table: DetailHold
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'LastYearsQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'LastYearsQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'PriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Prices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'PriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'BatchDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'BatchDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'ExtraDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'ExtraDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'SectionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Sections table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'SectionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'SectionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'SectionName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'OriginalItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'OriginalItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailHold') AND c.name = 'KeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Keywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailHold', @level2type = N'COLUMN', @level2name = N'KeywordId';
GO

-- Table: DetailMatch
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'LastYearsQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'LastYearsQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'PriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Prices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'PriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'BatchDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BatchDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'BatchDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'ExtraDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'ExtraDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'SectionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Sections table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'SectionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'SectionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'SectionName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'OriginalItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'OriginalItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailMatch') AND c.name = 'KeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Keywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailMatch', @level2type = N'COLUMN', @level2name = N'KeywordId';
GO

-- Table: DetailNotifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'DetailNotificationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DetailNotifications table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'DetailNotificationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'NotificationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Notifications table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'NotificationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'OrigItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'OrigItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'NewItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'NewItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'OrigVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'OrigVendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailNotifications') AND c.name = 'NewVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailNotifications', @level2type = N'COLUMN', @level2name = N'NewVendorId';
GO

-- Table: DetailUploads
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailUploads') AND c.name = 'DetailUploadId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DetailUploads table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailUploads', @level2type = N'COLUMN', @level2name = N'DetailUploadId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailUploads') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailUploads', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailUploads') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailUploads', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DetailUploads') AND c.name = 'ClientFileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DetailUploads', @level2type = N'COLUMN', @level2name = N'ClientFileName';
GO

-- Table: District
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'CSRepId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CSRep table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'CSRepId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'CoopId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Coops table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'CoopId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'BAName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'BAName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'POLayoutId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POLayouts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'POLayoutId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'AccountingFormatId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to AccountingFormats table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'AccountingFormatId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'DistrictTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'DistrictTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'POUploadEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'POUploadEmail';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'ContactName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'ContactPhone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'ContactPhone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'ParentDistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'ParentDistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'AccountingDistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'AccountingDistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'StateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.District') AND c.name = 'MinimumPOAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'District', @level2type = N'COLUMN', @level2name = N'MinimumPOAmount';
GO

-- Table: DistrictCategories
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategories') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategories', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategories') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategories', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategories') AND c.name = 'OrderBookTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBookTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategories', @level2type = N'COLUMN', @level2name = N'OrderBookTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategories') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategories', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: DistrictCategoryTitles
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategoryTitles') AND c.name = 'DistrictCategoryTitleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictCategoryTitles table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategoryTitles', @level2type = N'COLUMN', @level2name = N'DistrictCategoryTitleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategoryTitles') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategoryTitles', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCategoryTitles') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCategoryTitles', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO

-- Table: DistrictCharges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCharges') AND c.name = 'DistrictChargeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictCharges table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCharges', @level2type = N'COLUMN', @level2name = N'DistrictChargeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCharges') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCharges', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCharges') AND c.name = 'ChargeTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ChargeTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCharges', @level2type = N'COLUMN', @level2name = N'ChargeTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCharges') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCharges', @level2type = N'COLUMN', @level2name = N'Amount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictCharges') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictCharges', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO

-- Table: DistrictChargesNotes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictChargesNotes') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictChargesNotes', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictChargesNotes') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictChargesNotes', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO

-- Table: DistrictContacts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'DistrictContactId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictContacts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'DistrictContactId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'DistrictContactTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictContactTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'DistrictContactTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'SalutationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Salutations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'SalutationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'FirstName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'FirstName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'MiddleName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'MiddleName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'LastName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'LastName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'Phone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContacts') AND c.name = 'FullName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContacts', @level2type = N'COLUMN', @level2name = N'FullName';
GO

-- Table: DistrictContactTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContactTypes') AND c.name = 'DistrictContactTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictContactTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContactTypes', @level2type = N'COLUMN', @level2name = N'DistrictContactTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContactTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContactTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: DistrictContinuances
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContinuances') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContinuances') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContinuances') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContinuances') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContinuances') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictContinuances') AND c.name = 'SavingsBudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictContinuances', @level2type = N'COLUMN', @level2name = N'SavingsBudgetId';
GO

-- Table: DistrictNotes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictNotes') AND c.name = 'DistrictNotesId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictNotes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotes', @level2type = N'COLUMN', @level2name = N'DistrictNotesId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictNotes') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotes', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: DistrictNotifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictNotifications') AND c.name = 'DistrictNotificationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictNotifications table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotifications', @level2type = N'COLUMN', @level2name = N'DistrictNotificationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictNotifications') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotifications', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictNotifications') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotifications', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictNotifications') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictNotifications', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: DistrictPP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictPP') AND c.name = 'DistrictPPId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictPP table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictPP', @level2type = N'COLUMN', @level2name = N'DistrictPPId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictPP') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictPP', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictPP') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictPP', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO

-- Table: DistrictProposedCharges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'ChargeTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ChargeTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'ChargeTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'Amount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'PreviousAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'PreviousAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictProposedCharges') AND c.name = 'PreviousBudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictProposedCharges', @level2type = N'COLUMN', @level2name = N'PreviousBudgetId';
GO

-- Table: DistrictReports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictReports') AND c.name = 'DistrictReportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictReports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictReports', @level2type = N'COLUMN', @level2name = N'DistrictReportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictReports') AND c.name = 'ReportName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictReports', @level2type = N'COLUMN', @level2name = N'ReportName';
GO

-- Table: DistrictTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictTypes') AND c.name = 'DistrictTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to DistrictTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictTypes', @level2type = N'COLUMN', @level2name = N'DistrictTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: DistrictVendor
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictVendor') AND c.name = 'DistrictVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictVendor', @level2type = N'COLUMN', @level2name = N'DistrictVendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictVendor') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictVendor', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictVendor') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictVendor', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DistrictVendor') AND c.name = 'VendorsAccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DistrictVendor', @level2type = N'COLUMN', @level2name = N'VendorsAccountCode';
GO

-- Table: DMSBidDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSBidDocuments') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSBidDocuments', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSBidDocuments') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSBidDocuments', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSBidDocuments') AND c.name = 'FileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSBidDocuments', @level2type = N'COLUMN', @level2name = N'FileName';
GO

-- Table: DMSSDSDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSSDSDocuments') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSSDSDocuments', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSSDSDocuments') AND c.name = 'MSDSId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSDS table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSSDSDocuments', @level2type = N'COLUMN', @level2name = N'MSDSId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSSDSDocuments') AND c.name = 'DocName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSSDSDocuments', @level2type = N'COLUMN', @level2name = N'DocName';
GO

-- Table: DMSVendorBidDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorBidDocuments') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorBidDocuments', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorBidDocuments') AND c.name = 'VendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorBidDocuments', @level2type = N'COLUMN', @level2name = N'VendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorBidDocuments') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorBidDocuments', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorBidDocuments') AND c.name = 'FileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorBidDocuments', @level2type = N'COLUMN', @level2name = N'FileName';
GO

-- Table: DMSVendorDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorDocuments') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorDocuments', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorDocuments') AND c.name = 'VendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorDocuments', @level2type = N'COLUMN', @level2name = N'VendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.DMSVendorDocuments') AND c.name = 'FileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'DMSVendorDocuments', @level2type = N'COLUMN', @level2name = N'FileName';
GO

-- Table: EmailBlast
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlast') AND c.name = 'EmailBlastId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to EmailBlast table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlast', @level2type = N'COLUMN', @level2name = N'EmailBlastId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlast') AND c.name = 'BlastName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlast', @level2type = N'COLUMN', @level2name = N'BlastName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlast') AND c.name = 'BlastDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlast', @level2type = N'COLUMN', @level2name = N'BlastDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlast') AND c.name = 'UseDefaultReadReceiptEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlast', @level2type = N'COLUMN', @level2name = N'UseDefaultReadReceiptEmail';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlast') AND c.name = 'ReadReceiptEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlast', @level2type = N'COLUMN', @level2name = N'ReadReceiptEmail';
GO

-- Table: EmailBlastAddresses08132012
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastAddresses08132012') AND c.name = 'EmailAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastAddresses08132012', @level2type = N'COLUMN', @level2name = N'EmailAddress';
GO

-- Table: EmailBlastCopy
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastCopy') AND c.name = 'EmailBlastId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to EmailBlast table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastCopy', @level2type = N'COLUMN', @level2name = N'EmailBlastId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastCopy') AND c.name = 'BlastName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastCopy', @level2type = N'COLUMN', @level2name = N'BlastName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastCopy') AND c.name = 'BlastDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastCopy', @level2type = N'COLUMN', @level2name = N'BlastDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastCopy') AND c.name = 'UseDefaultReadReceiptEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastCopy', @level2type = N'COLUMN', @level2name = N'UseDefaultReadReceiptEmail';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastCopy') AND c.name = 'ReadReceiptEmail' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastCopy', @level2type = N'COLUMN', @level2name = N'ReadReceiptEmail';
GO

-- Table: EmailBlastLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastLog') AND c.name = 'EmailBlastLogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to EmailBlastLog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastLog', @level2type = N'COLUMN', @level2name = N'EmailBlastLogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastLog') AND c.name = 'EmailBlastId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to EmailBlast table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastLog', @level2type = N'COLUMN', @level2name = N'EmailBlastId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.EmailBlastLog') AND c.name = 'ContactFullName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'EmailBlastLog', @level2type = N'COLUMN', @level2name = N'ContactFullName';
GO

-- Table: FreezeItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: FreezeItems2015
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'BudgetName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'BudgetName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'SchoolName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'SchoolName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'OrigVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'OrigVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.FreezeItems2015') AND c.name = 'OrigVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'FreezeItems2015', @level2type = N'COLUMN', @level2name = N'OrigVendorId';
GO

-- Table: HeaderWorkItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.HeaderWorkItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'HeaderWorkItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: Headings
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Headings') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Headings', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Headings') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Headings', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Headings') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Headings', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Headings') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Headings', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Headings') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Headings', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: HolidayCalendarVendor
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.HolidayCalendarVendor') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'HolidayCalendarVendor', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: ImageLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImageLog') AND c.name = 'statusCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImageLog', @level2type = N'COLUMN', @level2name = N'statusCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImageLog') AND c.name = 'writeStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImageLog', @level2type = N'COLUMN', @level2name = N'writeStatus';
GO

-- Table: ImportCatalogDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportCatalogDetail') AND c.name = 'ImportCatalogDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ImportCatalogDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportCatalogDetail', @level2type = N'COLUMN', @level2name = N'ImportCatalogDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportCatalogDetail') AND c.name = 'ImportCatalogHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportCatalogDetail', @level2type = N'COLUMN', @level2name = N'ImportCatalogHeaderId';
GO

-- Table: ImportCatalogHeader
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportCatalogHeader') AND c.name = 'ImportCatalogHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportCatalogHeader', @level2type = N'COLUMN', @level2name = N'ImportCatalogHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportCatalogHeader') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportCatalogHeader', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: ImportDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportDetail') AND c.name = 'ImportDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ImportDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportDetail', @level2type = N'COLUMN', @level2name = N'ImportDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportDetail') AND c.name = 'ImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Imports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportDetail', @level2type = N'COLUMN', @level2name = N'ImportId';
GO

-- Table: ImportMessages
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportMessages') AND c.name = 'MessageId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Messages table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportMessages', @level2type = N'COLUMN', @level2name = N'MessageId';
GO

-- Table: ImportProcesses
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ImportProcesses') AND c.name = 'ImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Imports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ImportProcesses', @level2type = N'COLUMN', @level2name = N'ImportId';
GO

-- Table: Imports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Imports') AND c.name = 'ImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Imports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Imports', @level2type = N'COLUMN', @level2name = N'ImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Imports') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Imports', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Imports') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Imports', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO

-- Table: InstructionBookContents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.InstructionBookContents') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InstructionBookContents', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.InstructionBookContents') AND c.name = 'SubReportName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InstructionBookContents', @level2type = N'COLUMN', @level2name = N'SubReportName';
GO

-- Table: InstructionBookTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.InstructionBookTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InstructionBookTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Instructions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Instructions') AND c.name = 'InstructionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Instructions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Instructions', @level2type = N'COLUMN', @level2name = N'InstructionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Instructions') AND c.name = 'SectionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Instructions', @level2type = N'COLUMN', @level2name = N'SectionName';
GO

-- Table: Invoices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Invoices') AND c.name = 'InvoiceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Invoices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Invoices', @level2type = N'COLUMN', @level2name = N'InvoiceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Invoices') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Invoices', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Invoices') AND c.name = 'InvoiceTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to InvoiceTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Invoices', @level2type = N'COLUMN', @level2name = N'InvoiceTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Invoices') AND c.name = 'DueDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Due or deadline date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Invoices', @level2type = N'COLUMN', @level2name = N'DueDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Invoices') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Invoices', @level2type = N'COLUMN', @level2name = N'Amount';
GO

-- Table: InvoiceTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.InvoiceTypes') AND c.name = 'InvoiceTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to InvoiceTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InvoiceTypes', @level2type = N'COLUMN', @level2name = N'InvoiceTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.InvoiceTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'InvoiceTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: IPQueue
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueue') AND c.name = 'IPQueueId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to IPQueue table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueue', @level2type = N'COLUMN', @level2name = N'IPQueueId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueue') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueue', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueue') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueue', @level2type = N'COLUMN', @level2name = N'Status';
GO

-- Table: IPQueueUsers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueueUsers') AND c.name = 'IPQueueUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueueUsers', @level2type = N'COLUMN', @level2name = N'IPQueueUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueueUsers') AND c.name = 'IPQueueId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to IPQueue table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueueUsers', @level2type = N'COLUMN', @level2name = N'IPQueueId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueueUsers') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueueUsers', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.IPQueueUsers') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'IPQueueUsers', @level2type = N'COLUMN', @level2name = N'Status';
GO

-- Table: ItemContractPrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemContractPrices') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemContractPrices', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemContractPrices') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemContractPrices', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemContractPrices') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemContractPrices', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO

-- Table: ItemDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemDocuments') AND c.name = 'ItemDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ItemDocuments table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemDocuments', @level2type = N'COLUMN', @level2name = N'ItemDocumentId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemDocuments') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemDocuments', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemDocuments') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemDocuments', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemDocuments') AND c.name = 'FileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemDocuments', @level2type = N'COLUMN', @level2name = N'FileName';
GO

-- Table: Items
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'BrandName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'BrandName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'ShortDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'ShortDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'KeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Keywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'KeywordId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'AlternateItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'AlternateItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'SectionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Sections table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'SectionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'RedirectedItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'RedirectedItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'FullDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'FullDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Items') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Items', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO

-- Table: ItemUpdates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemUpdates') AND c.name = 'ItemUpdateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ItemUpdates table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemUpdates', @level2type = N'COLUMN', @level2name = N'ItemUpdateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ItemUpdates') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ItemUpdates', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: jSessions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.jSessions') AND c.name = 'jSessionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to jSessions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'jSessions', @level2type = N'COLUMN', @level2name = N'jSessionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.jSessions') AND c.name = 'IPAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'jSessions', @level2type = N'COLUMN', @level2name = N'IPAddress';
GO

-- Table: Keywords
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Keywords') AND c.name = 'KeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Keywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Keywords', @level2type = N'COLUMN', @level2name = N'KeywordId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Keywords') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Keywords', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Keywords') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Keywords', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Keywords') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Keywords', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: Ledger
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Ledger') AND c.name = 'LedgerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Ledger table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Ledger', @level2type = N'COLUMN', @level2name = N'LedgerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Ledger') AND c.name = 'TransactionTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TransactionTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Ledger', @level2type = N'COLUMN', @level2name = N'TransactionTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Ledger') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Ledger', @level2type = N'COLUMN', @level2name = N'Amount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Ledger') AND c.name = 'DueDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Due or deadline date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Ledger', @level2type = N'COLUMN', @level2name = N'DueDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Ledger') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Ledger', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: LL_RepLay
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.LL_RepLay') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'LL_RepLay', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.LL_RepLay') AND c.name = 'FileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'LL_RepLay', @level2type = N'COLUMN', @level2name = N'FileName';
GO

-- Table: ManufacturerProductLines
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ManufacturerProductLines') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ManufacturerProductLines', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ManufacturerProductLines') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ManufacturerProductLines', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ManufacturerProductLines') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ManufacturerProductLines', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: Manufacturers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Manufacturers') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Manufacturers', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Manufacturers') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Manufacturers', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Manufacturers') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Manufacturers', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: MappedItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MappedItems') AND c.name = 'MappedItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MappedItems', @level2type = N'COLUMN', @level2name = N'MappedItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MappedItems') AND c.name = 'OrigItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MappedItems', @level2type = N'COLUMN', @level2name = N'OrigItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MappedItems') AND c.name = 'NewItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MappedItems', @level2type = N'COLUMN', @level2name = N'NewItemId';
GO

-- Table: Menus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Menus') AND c.name = 'MenuId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Menus table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Menus', @level2type = N'COLUMN', @level2name = N'MenuId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Menus') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Menus', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Menus') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Menus', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Messages
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Messages') AND c.name = 'MessageId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Messages table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Messages', @level2type = N'COLUMN', @level2name = N'MessageId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Messages') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Messages', @level2type = N'COLUMN', @level2name = N'Code';
GO

-- Table: Months
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Months') AND c.name = 'MonthId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Months table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Months', @level2type = N'COLUMN', @level2name = N'MonthId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Months') AND c.name = 'MonthName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Months', @level2type = N'COLUMN', @level2name = N'MonthName';
GO

-- Table: MSDS
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSDS') AND c.name = 'MSDSId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSDS table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSDS', @level2type = N'COLUMN', @level2name = N'MSDSId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSDS') AND c.name = 'AlternateDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSDS', @level2type = N'COLUMN', @level2name = N'AlternateDescription';
GO

-- Table: MSDSDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSDSDetail') AND c.name = 'RTK_CASFileId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_CASFile table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSDSDetail', @level2type = N'COLUMN', @level2name = N'RTK_CASFileId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSDSDetail') AND c.name = 'MixturePercentCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSDSDetail', @level2type = N'COLUMN', @level2name = N'MixturePercentCode';
GO

-- Table: MSRPExcelExport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSRPExcelExport') AND c.name = 'MSRPExcelExportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSRPExcelExport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPExcelExport', @level2type = N'COLUMN', @level2name = N'MSRPExcelExportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSRPExcelExport') AND c.name = 'ManufacturerName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPExcelExport', @level2type = N'COLUMN', @level2name = N'ManufacturerName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSRPExcelExport') AND c.name = 'OptionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPExcelExport', @level2type = N'COLUMN', @level2name = N'OptionName';
GO

-- Table: MSRPExcelImport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSRPExcelImport') AND c.name = 'MSRPExcelImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSRPExcelImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPExcelImport', @level2type = N'COLUMN', @level2name = N'MSRPExcelImportId';
GO

-- Table: MSRPOptions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSRPOptions') AND c.name = 'MSRPOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSRPOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPOptions', @level2type = N'COLUMN', @level2name = N'MSRPOptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.MSRPOptions') AND c.name = 'MSRPOptionName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'MSRPOptions', @level2type = N'COLUMN', @level2name = N'MSRPOptionName';
GO

-- Table: NextNumber
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.NextNumber') AND c.name = 'NextNumberId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to NextNumber table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NextNumber', @level2type = N'COLUMN', @level2name = N'NextNumberId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.NextNumber') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NextNumber', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.NextNumber') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NextNumber', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.NextNumber') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NextNumber', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO

-- Table: NotificationOptions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.NotificationOptions') AND c.name = 'NotificationOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to NotificationOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NotificationOptions', @level2type = N'COLUMN', @level2name = N'NotificationOptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.NotificationOptions') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'NotificationOptions', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: Notifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Notifications') AND c.name = 'NotificationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Notifications table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Notifications', @level2type = N'COLUMN', @level2name = N'NotificationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Notifications') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Notifications', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Notifications') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Notifications', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Notifications') AND c.name = 'EmailBlastId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to EmailBlast table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Notifications', @level2type = N'COLUMN', @level2name = N'EmailBlastId';
GO

-- Table: OBPrices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'PriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Prices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'PriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'PackedItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'PackedItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBPrices') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBPrices', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO

-- Table: OBView
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'HeadingDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'HeadingDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'ItemDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'ItemDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'PricePlanDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'PricePlanDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'VendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'VendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'TotalQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'TotalQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OBView') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OBView', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO

-- Table: Options
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Options') AND c.name = 'OptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Options table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Options', @level2type = N'COLUMN', @level2name = N'OptionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Options') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Options', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: OptionsLink
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OptionsLink') AND c.name = 'OptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Options table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OptionsLink', @level2type = N'COLUMN', @level2name = N'OptionId';
GO

-- Table: OrderBookAlwaysAdd
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookAlwaysAdd') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookAlwaysAdd', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookAlwaysAdd') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookAlwaysAdd', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO

-- Table: OrderBookDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'OrderBookDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBookDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'OrderBookDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'OrderBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBooks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'OrderBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'VendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'VendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: OrderBookDetailOld
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'OrderBookDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBookDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'OrderBookDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'OrderBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBooks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'OrderBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'VendorCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'VendorCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookDetailOld') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookDetailOld', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: OrderBookLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookLog') AND c.name = 'OrderBookLogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBookLog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookLog', @level2type = N'COLUMN', @level2name = N'OrderBookLogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookLog') AND c.name = 'OrderBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBooks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookLog', @level2type = N'COLUMN', @level2name = N'OrderBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookLog') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookLog', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookLog') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookLog', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookLog') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookLog', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: OrderBooks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'OrderBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBooks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'OrderBookId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'PricePlanDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'PricePlanDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBooks') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBooks', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: OrderBookTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookTypes') AND c.name = 'OrderBookTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBookTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookTypes', @level2type = N'COLUMN', @level2name = N'OrderBookTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.OrderBookTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'OrderBookTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Payments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Payments') AND c.name = 'PaymentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Payments table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Payments', @level2type = N'COLUMN', @level2name = N'PaymentId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Payments') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Payments', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Payments') AND c.name = 'InvoiceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Invoices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Payments', @level2type = N'COLUMN', @level2name = N'InvoiceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Payments') AND c.name = 'PaymentTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PaymentTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Payments', @level2type = N'COLUMN', @level2name = N'PaymentTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Payments') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Payments', @level2type = N'COLUMN', @level2name = N'Amount';
GO

-- Table: PaymentTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PaymentTypes') AND c.name = 'PaymentTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PaymentTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PaymentTypes', @level2type = N'COLUMN', @level2name = N'PaymentTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PaymentTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PaymentTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: PendingApprovals
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'StatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PendingApprovals') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PendingApprovals', @level2type = N'COLUMN', @level2name = N'Amount';
GO

-- Table: PO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'Amount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'DiscountAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'DiscountAmount';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PO') AND c.name = 'ShippingAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PO', @level2type = N'COLUMN', @level2name = N'ShippingAmount';
GO

-- Table: PODetailItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'PODetailItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'PODetailItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PODetailItems') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PODetailItems', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO

-- Table: POLayoutDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POLayoutDetail') AND c.name = 'POLayoutDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POLayoutDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayoutDetail', @level2type = N'COLUMN', @level2name = N'POLayoutDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POLayoutDetail') AND c.name = 'POLayoutId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POLayouts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayoutDetail', @level2type = N'COLUMN', @level2name = N'POLayoutId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POLayoutDetail') AND c.name = 'POLayoutFieldId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POLayoutFields table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayoutDetail', @level2type = N'COLUMN', @level2name = N'POLayoutFieldId';
GO

-- Table: POLayoutFields
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POLayoutFields') AND c.name = 'POLayoutFieldId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POLayoutFields table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayoutFields', @level2type = N'COLUMN', @level2name = N'POLayoutFieldId';
GO

-- Table: POLayouts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POLayouts') AND c.name = 'POLayoutId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POLayouts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayouts', @level2type = N'COLUMN', @level2name = N'POLayoutId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POLayouts') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POLayouts', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: POPageSummary
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPageSummary') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPageSummary', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPageSummary') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPageSummary', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPageSummary') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPageSummary', @level2type = N'COLUMN', @level2name = N'POId';
GO

-- Table: POPrintTaggedPOFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPrintTaggedPOFile') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPrintTaggedPOFile', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPrintTaggedPOFile') AND c.name = 'AwardsBidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPrintTaggedPOFile', @level2type = N'COLUMN', @level2name = N'AwardsBidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPrintTaggedPOFile') AND c.name = 'BudgetName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPrintTaggedPOFile', @level2type = N'COLUMN', @level2name = N'BudgetName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POPrintTaggedPOFile') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POPrintTaggedPOFile', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO

-- Table: POQueue
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueue') AND c.name = 'POQueueId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POQueue table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueue', @level2type = N'COLUMN', @level2name = N'POQueueId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueue') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueue', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueue') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueue', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueue') AND c.name = 'SendAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueue', @level2type = N'COLUMN', @level2name = N'SendAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueue') AND c.name = 'SendStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueue', @level2type = N'COLUMN', @level2name = N'SendStatus';
GO

-- Table: POQueueItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueueItems') AND c.name = 'POQueueItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueueItems', @level2type = N'COLUMN', @level2name = N'POQueueItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueueItems') AND c.name = 'POQueueId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to POQueue table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueueItems', @level2type = N'COLUMN', @level2name = N'POQueueId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueueItems') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueueItems', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POQueueItems') AND c.name = 'SendStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POQueueItems', @level2type = N'COLUMN', @level2name = N'SendStatus';
GO

-- Table: POStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POStatus') AND c.name = 'POStatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatus', @level2type = N'COLUMN', @level2name = N'POStatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POStatus') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatus', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POStatus') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatus', @level2type = N'COLUMN', @level2name = N'StatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POStatus') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatus', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: POStatusTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.POStatusTable') AND c.name = 'StatusName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'POStatusTable', @level2type = N'COLUMN', @level2name = N'StatusName';
GO

-- Table: PostCatalogDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PostCatalogDetail') AND c.name = 'PostCatalogDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PostCatalogDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PostCatalogDetail', @level2type = N'COLUMN', @level2name = N'PostCatalogDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PostCatalogDetail') AND c.name = 'PostCatalogHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PostCatalogDetail', @level2type = N'COLUMN', @level2name = N'PostCatalogHeaderId';
GO

-- Table: PostCatalogHeader
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PostCatalogHeader') AND c.name = 'PostCatalogHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PostCatalogHeader', @level2type = N'COLUMN', @level2name = N'PostCatalogHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PostCatalogHeader') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PostCatalogHeader', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: PPCatalogs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCatalogs') AND c.name = 'PPCatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PPCatalogs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCatalogs', @level2type = N'COLUMN', @level2name = N'PPCatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCatalogs') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCatalogs', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCatalogs') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCatalogs', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCatalogs') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCatalogs', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCatalogs') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCatalogs', @level2type = N'COLUMN', @level2name = N'AwardId';
GO

-- Table: PPCategory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCategory') AND c.name = 'PPCategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PPCategory table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCategory', @level2type = N'COLUMN', @level2name = N'PPCategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCategory') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCategory', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PPCategory') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PPCategory', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO

-- Table: PriceHolds
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceHolds') AND c.name = 'PriceHoldId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PriceHolds table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceHolds', @level2type = N'COLUMN', @level2name = N'PriceHoldId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceHolds') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceHolds', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceHolds') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceHolds', @level2type = N'COLUMN', @level2name = N'Quantity';
GO

-- Table: PriceListTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceListTypes') AND c.name = 'PriceListTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PriceListTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceListTypes', @level2type = N'COLUMN', @level2name = N'PriceListTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceListTypes') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceListTypes', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: PricePlans
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricePlans') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricePlans', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricePlans') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricePlans', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricePlans') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricePlans', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: PriceRanges
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceRanges') AND c.name = 'PriceRangeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PriceRanges table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceRanges', @level2type = N'COLUMN', @level2name = N'PriceRangeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceRanges') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceRanges', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceRanges') AND c.name = 'ManufacturerId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Manufacturers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceRanges', @level2type = N'COLUMN', @level2name = N'ManufacturerId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceRanges') AND c.name = 'ManufacturerProductLineId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ManufacturerProductLines table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceRanges', @level2type = N'COLUMN', @level2name = N'ManufacturerProductLineId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PriceRanges') AND c.name = 'MSRPOptionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSRPOptions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PriceRanges', @level2type = N'COLUMN', @level2name = N'MSRPOptionId';
GO

-- Table: Prices
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'PriceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Prices table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'PriceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'PackedItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'PackedItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'RedirectedItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'RedirectedItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Prices') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Prices', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: PricingAddenda
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'PricingAddendaId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricingAddenda table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'PricingAddendaId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'HeadingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Headings table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'HeadingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'KeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Keywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'KeywordId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'AwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Awards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'AwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'FullDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'FullDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'PackedItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'PackedItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingAddenda') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingAddenda', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO

-- Table: PricingConsolidatedOrderCounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingConsolidatedOrderCounts') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingConsolidatedOrderCounts', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingConsolidatedOrderCounts') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingConsolidatedOrderCounts', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: PricingMap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'MappedItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'MappedItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'PackedItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'PackedItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'PackedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'PackedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'UnitCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'UnitCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingMap') AND c.name = 'ItemDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingMap', @level2type = N'COLUMN', @level2name = N'ItemDescription';
GO

-- Table: PricingUpdate
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingUpdate') AND c.name = 'PricingUpdateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricingUpdate table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingUpdate', @level2type = N'COLUMN', @level2name = N'PricingUpdateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PricingUpdate') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PricingUpdate', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: PrintDocuments
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PrintDocuments') AND c.name = 'PrintDocumentId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PrintDocuments table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PrintDocuments', @level2type = N'COLUMN', @level2name = N'PrintDocumentId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PrintDocuments') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PrintDocuments', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PrintDocuments') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PrintDocuments', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PrintDocuments') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PrintDocuments', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.PrintDocuments') AND c.name = 'DocumentName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'PrintDocuments', @level2type = N'COLUMN', @level2name = N'DocumentName';
GO

-- Table: Printers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Printers') AND c.name = 'PrinterId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Printers table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Printers', @level2type = N'COLUMN', @level2name = N'PrinterId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Printers') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Printers', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: ProjectTasks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ProjectTasks') AND c.name = 'ProjectTasksId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ProjectTasks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ProjectTasks', @level2type = N'COLUMN', @level2name = N'ProjectTasksId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ProjectTasks') AND c.name = 'TaskDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ProjectTasks', @level2type = N'COLUMN', @level2name = N'TaskDescription';
GO

-- Table: Rates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rates') AND c.name = 'RateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Rates table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates', @level2type = N'COLUMN', @level2name = N'RateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rates') AND c.name = 'ServiceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Services table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates', @level2type = N'COLUMN', @level2name = N'ServiceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rates') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rates') AND c.name = 'BidQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates', @level2type = N'COLUMN', @level2name = N'BidQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rates') AND c.name = 'RateTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RateTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates', @level2type = N'COLUMN', @level2name = N'RateTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rates') AND c.name = 'RateUnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RateUnits table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rates', @level2type = N'COLUMN', @level2name = N'RateUnitId';
GO

-- Table: RateTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RateTypes') AND c.name = 'RateTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RateTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RateTypes', @level2type = N'COLUMN', @level2name = N'RateTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RateTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RateTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RateUnits
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RateUnits') AND c.name = 'RateUnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RateUnits table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RateUnits', @level2type = N'COLUMN', @level2name = N'RateUnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RateUnits') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RateUnits', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Receiving
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Receiving') AND c.name = 'ReceivingId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Receiving table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Receiving', @level2type = N'COLUMN', @level2name = N'ReceivingId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Receiving') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Receiving', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Receiving') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Receiving', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Receiving') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Receiving', @level2type = N'COLUMN', @level2name = N'Quantity';
GO

-- Table: ReqAudit
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ReqAudit') AND c.name = 'ReqAuditId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ReqAudit table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReqAudit', @level2type = N'COLUMN', @level2name = N'ReqAuditId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ReqAudit') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReqAudit', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ReqAudit') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReqAudit', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ReqAudit') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReqAudit', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ReqAudit') AND c.name = 'FieldName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ReqAudit', @level2type = N'COLUMN', @level2name = N'FieldName';
GO

-- Table: RequisitionChangeLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'OrigUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'OrigUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'OrigBudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'OrigBudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'OrigAccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'OrigAccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'OrigBidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'OrigBidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'NewUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'NewUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'NewBudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'NewBudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'NewAccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'NewAccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'NewBidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'NewBidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RequisitionChangeLog') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RequisitionChangeLog', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: Requisitions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'BudgetAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BudgetAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'BudgetAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'UserAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'UserAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'AccountCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'AccountCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'ApprovalId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Approvals table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'ApprovalId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'StatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'BidId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Bids table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'BidId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Requisitions') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Requisitions', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO

-- Table: ResetPasswordTracking
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ResetPasswordTracking') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ResetPasswordTracking', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ResetPasswordTracking') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ResetPasswordTracking', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ResetPasswordTracking') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ResetPasswordTracking', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ResetPasswordTracking') AND c.name = 'ResetPasswordCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ResetPasswordTracking', @level2type = N'COLUMN', @level2name = N'ResetPasswordCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ResetPasswordTracking') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ResetPasswordTracking', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Rights
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rights') AND c.name = 'RightsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Rights table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rights', @level2type = N'COLUMN', @level2name = N'RightsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rights') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rights', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Rights') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Rights', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RightsLink
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RightsLink') AND c.name = 'RightsLinkId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RightsLink table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RightsLink', @level2type = N'COLUMN', @level2name = N'RightsLinkId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RightsLink') AND c.name = 'RightsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Rights table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RightsLink', @level2type = N'COLUMN', @level2name = N'RightsId';
GO

-- Table: RTK_2010NJHSL
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_2010NJHSL') AND c.name = 'Common Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_2010NJHSL', @level2type = N'COLUMN', @level2name = N'Common Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_2010NJHSL') AND c.name = 'Chemical Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_2010NJHSL', @level2type = N'COLUMN', @level2name = N'Chemical Name';
GO

-- Table: RTK_CASFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_CASFile') AND c.name = 'RTK_CASFileId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_CASFile table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_CASFile', @level2type = N'COLUMN', @level2name = N'RTK_CASFileId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_CASFile') AND c.name = 'CASChemicalName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_CASFile', @level2type = N'COLUMN', @level2name = N'CASChemicalName';
GO

-- Table: RTK_ContainerCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ContainerCodes') AND c.name = 'ContainerCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ContainerCodes', @level2type = N'COLUMN', @level2name = N'ContainerCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ContainerCodes') AND c.name = 'ContainerAltCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ContainerCodes', @level2type = N'COLUMN', @level2name = N'ContainerAltCode';
GO

-- Table: RTK_Documents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Documents') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Documents', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Documents') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Documents', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Documents') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Documents', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Documents') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Documents', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_FactSheets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_FactSheets') AND c.name = 'CommonName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_FactSheets', @level2type = N'COLUMN', @level2name = N'CommonName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_FactSheets') AND c.name = 'ChemicalName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_FactSheets', @level2type = N'COLUMN', @level2name = N'ChemicalName';
GO

-- Table: RTK_HealthHazardCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_HealthHazardCodes') AND c.name = 'HealthHazardCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_HealthHazardCodes', @level2type = N'COLUMN', @level2name = N'HealthHazardCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_HealthHazardCodes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_HealthHazardCodes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_Inventories
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Inventories') AND c.name = 'RTK_SiteId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Sites table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Inventories', @level2type = N'COLUMN', @level2name = N'RTK_SiteId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Inventories') AND c.name = 'RTK_InventoryNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Inventories', @level2type = N'COLUMN', @level2name = N'RTK_InventoryNotes';
GO

-- Table: RTK_InventoryRangeCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_InventoryRangeCodes') AND c.name = 'RangeCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_InventoryRangeCodes', @level2type = N'COLUMN', @level2name = N'RangeCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_InventoryRangeCodes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_InventoryRangeCodes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_Items
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'RTK_ItemsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'RTK_ItemsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'LegacyCometCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'LegacyCometCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'MSDSId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSDS table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'MSDSId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Items') AND c.name = 'RTK_PurposeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Purposes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Items', @level2type = N'COLUMN', @level2name = N'RTK_PurposeId';
GO

-- Table: RTK_LegacyDistrictCodesMap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacyDistrictCodesMap') AND c.name = 'Legacy_DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacyDistrictCodesMap', @level2type = N'COLUMN', @level2name = N'Legacy_DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacyDistrictCodesMap') AND c.name = 'SQL_DistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacyDistrictCodesMap', @level2type = N'COLUMN', @level2name = N'SQL_DistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacyDistrictCodesMap') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacyDistrictCodesMap', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO

-- Table: RTK_LegacySchoolFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND c.name = 'LegacyDistrictCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile', @level2type = N'COLUMN', @level2name = N'LegacyDistrictCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND c.name = 'LegacySchoolCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile', @level2type = N'COLUMN', @level2name = N'LegacySchoolCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND c.name = 'SchoolName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile', @level2type = N'COLUMN', @level2name = N'SchoolName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND c.name = 'CityStZip' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Postal/ZIP code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile', @level2type = N'COLUMN', @level2name = N'CityStZip';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_LegacySchoolFile') AND c.name = 'RTK_SitesId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Sites table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_LegacySchoolFile', @level2type = N'COLUMN', @level2name = N'RTK_SitesId';
GO

-- Table: RTK_MixtureCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_MixtureCodes') AND c.name = 'MixtureCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_MixtureCodes', @level2type = N'COLUMN', @level2name = N'MixtureCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_MixtureCodes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_MixtureCodes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_MSDSDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_MSDSDetail') AND c.name = 'RTK_CASFileId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_CASFile table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_MSDSDetail', @level2type = N'COLUMN', @level2name = N'RTK_CASFileId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_MSDSDetail') AND c.name = 'MixturePercentCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_MSDSDetail', @level2type = N'COLUMN', @level2name = N'MixturePercentCode';
GO

-- Table: RTK_Purposes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Purposes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Purposes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_ReportItems
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'RTK_ReportItemsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_ReportItems table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'RTK_ReportItemsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'RTK_SitesId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Sites table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'RTK_SitesId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'LegacyLocnCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'LegacyLocnCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'LegacyCometItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'LegacyCometItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'MSDSId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSDS table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'MSDSId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_ReportItems') AND c.name = 'RTK_ItemsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_ReportItems', @level2type = N'COLUMN', @level2name = N'RTK_ItemsId';
GO

-- Table: RTK_Sites
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Sites') AND c.name = 'RTK_SitesId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Sites table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites', @level2type = N'COLUMN', @level2name = N'RTK_SitesId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Sites') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Sites') AND c.name = 'CoMunCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites', @level2type = N'COLUMN', @level2name = N'CoMunCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Sites') AND c.name = 'FacilityName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites', @level2type = N'COLUMN', @level2name = N'FacilityName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Sites') AND c.name = 'ChemicalInventoryStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites', @level2type = N'COLUMN', @level2name = N'ChemicalInventoryStatus';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Sites') AND c.name = 'EmergencyPhone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Sites', @level2type = N'COLUMN', @level2name = N'EmergencyPhone';
GO

-- Table: RTK_Surveys
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Surveys') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Surveys', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Surveys') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Surveys', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Surveys') AND c.name = 'FacilityName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Surveys', @level2type = N'COLUMN', @level2name = N'FacilityName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Surveys') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Surveys', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_Training
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Training') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Training', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Training') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Training', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Training') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Training', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_Training') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_Training', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_UOMCodes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_UOMCodes') AND c.name = 'UOMCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_UOMCodes', @level2type = N'COLUMN', @level2name = N'UOMCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_UOMCodes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_UOMCodes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: RTK_VendorLinks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_VendorLinks') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_VendorLinks', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_VendorLinks') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_VendorLinks', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.RTK_VendorLinks') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'RTK_VendorLinks', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: SafetyDataSheets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SafetyDataSheets') AND c.name = 'SafetyDataSheetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SafetyDataSheets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SafetyDataSheets', @level2type = N'COLUMN', @level2name = N'SafetyDataSheetId';
GO

-- Table: Salutations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Salutations') AND c.name = 'SalutationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Salutations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Salutations', @level2type = N'COLUMN', @level2name = N'SalutationId';
GO

-- Table: SaxDups
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxDups') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxDups', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxDups') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxDups', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxDups') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxDups', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: SaxNotifications
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'RepName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'RepName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'BudgetName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'BudgetName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'SchoolName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'SchoolName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'Quantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'RequestedVendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'RequestedVendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SaxNotifications') AND c.name = 'RequestedDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SaxNotifications', @level2type = N'COLUMN', @level2name = N'RequestedDescription';
GO

-- Table: ScanEvents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanEvents') AND c.name = 'ScanEventId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ScanEvents table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanEvents', @level2type = N'COLUMN', @level2name = N'ScanEventId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanEvents') AND c.name = 'ScanJobId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ScanJobs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanEvents', @level2type = N'COLUMN', @level2name = N'ScanJobId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanEvents') AND c.name = 'EventStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanEvents', @level2type = N'COLUMN', @level2name = N'EventStatus';
GO

-- Table: ScanJobs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanJobs') AND c.name = 'ScanJobId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ScanJobs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanJobs', @level2type = N'COLUMN', @level2name = N'ScanJobId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanJobs') AND c.name = 'CaptureName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanJobs', @level2type = N'COLUMN', @level2name = N'CaptureName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanJobs') AND c.name = 'CabinetName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanJobs', @level2type = N'COLUMN', @level2name = N'CabinetName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScanJobs') AND c.name = 'CatalogName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScanJobs', @level2type = N'COLUMN', @level2name = N'CatalogName';
GO

-- Table: ScannerZones
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScannerZones') AND c.name = 'ScannerZoneId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ScannerZones table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScannerZones', @level2type = N'COLUMN', @level2name = N'ScannerZoneId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScannerZones') AND c.name = 'ScanJobId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ScanJobs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScannerZones', @level2type = N'COLUMN', @level2name = N'ScanJobId';
GO

-- Table: ScheduledTask
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScheduledTask') AND c.name = 'TaskName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduledTask', @level2type = N'COLUMN', @level2name = N'TaskName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScheduledTask') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduledTask', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScheduledTask') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduledTask', @level2type = N'COLUMN', @level2name = N'Status';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScheduledTask') AND c.name = 'CreatedBy' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User who created the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduledTask', @level2type = N'COLUMN', @level2name = N'CreatedBy';
GO

-- Table: ScheduleTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScheduleTypes') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduleTypes', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ScheduleTypes') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ScheduleTypes', @level2type = N'COLUMN', @level2name = N'StateId';
GO

-- Table: School
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.School') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.School') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.School') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.School') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.School') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.School') AND c.name = 'LocationCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'School', @level2type = N'COLUMN', @level2name = N'LocationCode';
GO

-- Table: SDS_Rpt_Bridge
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDS_Rpt_Bridge') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDS_Rpt_Bridge', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: SDSDocs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSDocs') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSDocs', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSDocs') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSDocs', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSDocs') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSDocs', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSDocs') AND c.name = 'MSDSId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to MSDS table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSDocs', @level2type = N'COLUMN', @level2name = N'MSDSId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSDocs') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSDocs', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: SDSLog
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSLog') AND c.name = 'statusCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSLog', @level2type = N'COLUMN', @level2name = N'statusCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSLog') AND c.name = 'writeStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSLog', @level2type = N'COLUMN', @level2name = N'writeStatus';
GO

-- Table: SDSResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSResults') AND c.name = 'SDSResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SDSResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSResults', @level2type = N'COLUMN', @level2name = N'SDSResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSResults') AND c.name = 'SafetyDataSheetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SafetyDataSheets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSResults', @level2type = N'COLUMN', @level2name = N'SafetyDataSheetId';
GO

-- Table: SDSSyncStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSSyncStatus') AND c.name = 'SafetyDataSheetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SafetyDataSheets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSSyncStatus', @level2type = N'COLUMN', @level2name = N'SafetyDataSheetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSSyncStatus') AND c.name = 'SyncStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSSyncStatus', @level2type = N'COLUMN', @level2name = N'SyncStatus';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SDSSyncStatus') AND c.name = 'RequisitionSyncStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SDSSyncStatus', @level2type = N'COLUMN', @level2name = N'RequisitionSyncStatus';
GO

-- Table: SearchKeywords
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SearchKeywords') AND c.name = 'SearchKeywordId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SearchKeywords table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchKeywords', @level2type = N'COLUMN', @level2name = N'SearchKeywordId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SearchKeywords') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchKeywords', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SearchKeywords') AND c.name = 'CrossRefId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CrossRefs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchKeywords', @level2type = N'COLUMN', @level2name = N'CrossRefId';
GO

-- Table: SearchSets
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SearchSets') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchSets', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SearchSets') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SearchSets', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: Sections
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sections') AND c.name = 'SectionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Sections table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sections', @level2type = N'COLUMN', @level2name = N'SectionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sections') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sections', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sections') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sections', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: SecurityKeys
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityKeys') AND c.name = 'KeyName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityKeys', @level2type = N'COLUMN', @level2name = N'KeyName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityKeys') AND c.name = 'KeyDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityKeys', @level2type = N'COLUMN', @level2name = N'KeyDescription';
GO

-- Table: SecurityRoles
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityRoles') AND c.name = 'SecurityRoleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SecurityRoles table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoles', @level2type = N'COLUMN', @level2name = N'SecurityRoleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityRoles') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoles', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: SecurityRoleUsers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityRoleUsers') AND c.name = 'SecurityRoleUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoleUsers', @level2type = N'COLUMN', @level2name = N'SecurityRoleUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityRoleUsers') AND c.name = 'SecurityRoleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SecurityRoles table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoleUsers', @level2type = N'COLUMN', @level2name = N'SecurityRoleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SecurityRoleUsers') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SecurityRoleUsers', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: Services
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Services') AND c.name = 'ServiceId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Services table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services', @level2type = N'COLUMN', @level2name = N'ServiceId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Services') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services', @level2type = N'COLUMN', @level2name = N'TradeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Services') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Services') AND c.name = 'BidQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services', @level2type = N'COLUMN', @level2name = N'BidQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Services') AND c.name = 'RateTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RateTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services', @level2type = N'COLUMN', @level2name = N'RateTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Services') AND c.name = 'RateUnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RateUnits table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Services', @level2type = N'COLUMN', @level2name = N'RateUnitId';
GO

-- Table: SessionCmds
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionCmds') AND c.name = 'SessionCmdId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SessionCmds table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionCmds', @level2type = N'COLUMN', @level2name = N'SessionCmdId';
GO

-- Table: SessionTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'CSRepId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CSRep table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'CSRepId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'RepUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'RepUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'TempUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'TempUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'CurrentBudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'CurrentBudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'NextBudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'NextBudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SessionTable') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SessionTable', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: ShipLocations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'ZipCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Postal/ZIP code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'ZipCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'Phone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'LocationCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'LocationCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShipLocations') AND c.name = 'RTK_SitesId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to RTK_Sites table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShipLocations', @level2type = N'COLUMN', @level2name = N'RTK_SitesId';
GO

-- Table: ShippingCosts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingCosts') AND c.name = 'ShippingCostId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ShippingCosts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingCosts', @level2type = N'COLUMN', @level2name = N'ShippingCostId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingCosts') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingCosts', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingCosts') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingCosts', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingCosts') AND c.name = 'ShippingRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ShippingRequests table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingCosts', @level2type = N'COLUMN', @level2name = N'ShippingRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingCosts') AND c.name = 'Quantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingCosts', @level2type = N'COLUMN', @level2name = N'Quantity';
GO

-- Table: ShippingRequests
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingRequests') AND c.name = 'ShippingRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ShippingRequests table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingRequests', @level2type = N'COLUMN', @level2name = N'ShippingRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingRequests') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingRequests', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingRequests') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingRequests', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingRequests') AND c.name = 'RequestStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingRequests', @level2type = N'COLUMN', @level2name = N'RequestStatus';
GO

-- Table: ShippingVendor
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingVendor') AND c.name = 'ShippingVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingVendor', @level2type = N'COLUMN', @level2name = N'ShippingVendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingVendor') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingVendor', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.ShippingVendor') AND c.name = 'ShippingCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'ShippingVendor', @level2type = N'COLUMN', @level2name = N'ShippingCode';
GO

-- Table: SSOLoginTracking
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SSOLoginTracking') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SSOLoginTracking', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SSOLoginTracking') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SSOLoginTracking', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: States
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.States') AND c.name = 'StateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to States table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'States', @level2type = N'COLUMN', @level2name = N'StateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.States') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'States', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: StatusTable
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.StatusTable') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'StatusTable', @level2type = N'COLUMN', @level2name = N'StatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.StatusTable') AND c.name = 'StatusCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'StatusTable', @level2type = N'COLUMN', @level2name = N'StatusCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.StatusTable') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'StatusTable', @level2type = N'COLUMN', @level2name = N'Name';
GO

-- Table: Sulphite
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sulphite') AND c.name = 'SulphiteId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Sulphite table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sulphite', @level2type = N'COLUMN', @level2name = N'SulphiteId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sulphite') AND c.name = 'VendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sulphite', @level2type = N'COLUMN', @level2name = N'VendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sulphite') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sulphite', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Sulphite') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Sulphite', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: SulphiteDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteDetail') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteDetail', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteDetail') AND c.name = 'vendorItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteDetail', @level2type = N'COLUMN', @level2name = N'vendorItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteDetail') AND c.name = 'ItemCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteDetail', @level2type = N'COLUMN', @level2name = N'ItemCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteDetail') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteDetail', @level2type = N'COLUMN', @level2name = N'ItemId';
GO

-- Table: SulphiteImport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteImport') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteImport', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: SulphiteUsers
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteUsers') AND c.name = 'SulphiteUserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteUsers', @level2type = N'COLUMN', @level2name = N'SulphiteUserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.SulphiteUsers') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'SulphiteUsers', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: Suppression
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Suppression') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Suppression', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Suppression') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Suppression', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Suppression') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Suppression', @level2type = N'COLUMN', @level2name = N'Phone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Suppression') AND c.name = 'CreatedBy' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'User who created the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Suppression', @level2type = N'COLUMN', @level2name = N'CreatedBy';
GO

-- Table: TableOfContents
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TableOfContents') AND c.name = 'OrderBookId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to OrderBooks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TableOfContents', @level2type = N'COLUMN', @level2name = N'OrderBookId';
GO

-- Table: TagSet_
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TagSet_') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TagSet_', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: TaskEvent
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskEvent') AND c.name = 'TaskEventId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TaskEvent table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskEvent', @level2type = N'COLUMN', @level2name = N'TaskEventId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskEvent') AND c.name = 'ProjectTaskId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ProjectTasks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskEvent', @level2type = N'COLUMN', @level2name = N'ProjectTaskId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskEvent') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskEvent', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskEvent') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskEvent', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskEvent') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskEvent', @level2type = N'COLUMN', @level2name = N'UserId';
GO

-- Table: TaskSchedule
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskSchedule') AND c.name = 'TaskScheduleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TaskSchedule table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule', @level2type = N'COLUMN', @level2name = N'TaskScheduleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskSchedule') AND c.name = 'ProjectTasksId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ProjectTasks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule', @level2type = N'COLUMN', @level2name = N'ProjectTasksId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskSchedule') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskSchedule') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskSchedule') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TaskSchedule') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TaskSchedule', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO

-- Table: TempIrvingtonWincap
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TempIrvingtonWincap') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TempIrvingtonWincap', @level2type = N'COLUMN', @level2name = N'Description';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TempIrvingtonWincap') AND c.name = 'Invoice Address' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TempIrvingtonWincap', @level2type = N'COLUMN', @level2name = N'Invoice Address';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TempIrvingtonWincap') AND c.name = 'Shipping Address' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TempIrvingtonWincap', @level2type = N'COLUMN', @level2name = N'Shipping Address';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TempIrvingtonWincap') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TempIrvingtonWincap', @level2type = N'COLUMN', @level2name = N'Email';
GO

-- Table: TM_UOM
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TM_UOM') AND c.name = 'TM_UOMId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TM_UOM table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TM_UOM', @level2type = N'COLUMN', @level2name = N'TM_UOMId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TM_UOM') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TM_UOM', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: TMAwards
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMAwards') AND c.name = 'TMAwardId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMAwards table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMAwards', @level2type = N'COLUMN', @level2name = N'TMAwardId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMAwards') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMAwards', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMAwards') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMAwards', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMAwards') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMAwards', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMAwards') AND c.name = 'AwardAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMAwards', @level2type = N'COLUMN', @level2name = N'AwardAmount';
GO

-- Table: TMImport
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport') AND c.name = 'TMImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport', @level2type = N'COLUMN', @level2name = N'TMImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: TMImport1
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport1') AND c.name = 'TMImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport1', @level2type = N'COLUMN', @level2name = N'TMImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport1') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport1', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport1') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport1', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport1') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport1', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: TMImport2
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport2') AND c.name = 'TMImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport2', @level2type = N'COLUMN', @level2name = N'TMImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport2') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport2', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport2') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport2', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport2') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport2', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: TMImport3
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport3') AND c.name = 'TMImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport3', @level2type = N'COLUMN', @level2name = N'TMImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport3') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport3', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport3') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport3', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport3') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport3', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: TMImport5
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport5') AND c.name = 'TMImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport5', @level2type = N'COLUMN', @level2name = N'TMImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport5') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport5', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport5') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport5', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport5') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport5', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: TMImport6
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport6') AND c.name = 'TMImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMImport table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport6', @level2type = N'COLUMN', @level2name = N'TMImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport6') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport6', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport6') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport6', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMImport6') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMImport6', @level2type = N'COLUMN', @level2name = N'TradeId';
GO

-- Table: TmpTaskSchedule
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TmpTaskSchedule') AND c.name = 'TmpTaskScheduleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TmpTaskSchedule table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpTaskSchedule', @level2type = N'COLUMN', @level2name = N'TmpTaskScheduleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TmpTaskSchedule') AND c.name = 'ProjectTasksId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to ProjectTasks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpTaskSchedule', @level2type = N'COLUMN', @level2name = N'ProjectTasksId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TmpTaskSchedule') AND c.name = 'TaskDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpTaskSchedule', @level2type = N'COLUMN', @level2name = N'TaskDescription';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TmpTaskSchedule') AND c.name = 'StartDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective start date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpTaskSchedule', @level2type = N'COLUMN', @level2name = N'StartDate';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TmpTaskSchedule') AND c.name = 'EndDate' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Effective end date', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TmpTaskSchedule', @level2type = N'COLUMN', @level2name = N'EndDate';
GO

-- Table: TMSurvey
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurvey') AND c.name = 'TMSurveyId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMSurvey table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurvey', @level2type = N'COLUMN', @level2name = N'TMSurveyId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurvey') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurvey', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurvey') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurvey', @level2type = N'COLUMN', @level2name = N'Email';
GO

-- Table: TMSurveyNewTrades
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewTrades') AND c.name = 'TMSurveyNewTradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMSurveyNewTrades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewTrades', @level2type = N'COLUMN', @level2name = N'TMSurveyNewTradeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewTrades') AND c.name = 'TMSurveyId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMSurvey table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewTrades', @level2type = N'COLUMN', @level2name = N'TMSurveyId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewTrades') AND c.name = 'TradeName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewTrades', @level2type = N'COLUMN', @level2name = N'TradeName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewTrades') AND c.name = 'TradeDescription' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewTrades', @level2type = N'COLUMN', @level2name = N'TradeDescription';
GO

-- Table: TMSurveyNewVendors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'TMSurveyNewVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'TMSurveyNewVendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'TMSurveyId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMSurvey table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'TMSurveyId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'TradeName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'TradeName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'ContactName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyNewVendors') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyNewVendors', @level2type = N'COLUMN', @level2name = N'Phone';
GO

-- Table: TMSurveyResults
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyResults') AND c.name = 'TMSurveyResultId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMSurveyResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyResults', @level2type = N'COLUMN', @level2name = N'TMSurveyResultId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyResults') AND c.name = 'TMSurveyId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TMSurvey table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyResults', @level2type = N'COLUMN', @level2name = N'TMSurveyId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMSurveyResults') AND c.name = 'TMVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMSurveyResults', @level2type = N'COLUMN', @level2name = N'TMVendorId';
GO

-- Table: TMVendors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMVendors') AND c.name = 'TMVendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMVendors', @level2type = N'COLUMN', @level2name = N'TMVendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMVendors') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMVendors', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMVendors') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMVendors', @level2type = N'COLUMN', @level2name = N'VendorName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMVendors') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMVendors', @level2type = N'COLUMN', @level2name = N'TradeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TMVendors') AND c.name = 'BidTradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidTrades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TMVendors', @level2type = N'COLUMN', @level2name = N'BidTradeId';
GO

-- Table: TopUOM
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TopUOM') AND c.name = 'TopUOMId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TopUOM table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TopUOM', @level2type = N'COLUMN', @level2name = N'TopUOMId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TopUOM') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TopUOM', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TopUOM') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TopUOM', @level2type = N'COLUMN', @level2name = N'UnitId';
GO

-- Table: Trades
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Trades') AND c.name = 'TradeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Trades table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Trades', @level2type = N'COLUMN', @level2name = N'TradeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Trades') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Trades', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: TransactionTypes
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TransactionTypes') AND c.name = 'TransactionTypeId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to TransactionTypes table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TransactionTypes', @level2type = N'COLUMN', @level2name = N'TransactionTypeId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.TransactionTypes') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'TransactionTypes', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: Units
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Units') AND c.name = 'UnitId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Units table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Units', @level2type = N'COLUMN', @level2name = N'UnitId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Units') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Units', @level2type = N'COLUMN', @level2name = N'Code';
GO

-- Table: UNSPSCs
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UNSPSCs') AND c.name = 'UNSPSCId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UNSPSCs table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UNSPSCs', @level2type = N'COLUMN', @level2name = N'UNSPSCId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UNSPSCs') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UNSPSCs', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UNSPSCs') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UNSPSCs', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: UnsubscriptionEmail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UnsubscriptionEmail') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UnsubscriptionEmail', @level2type = N'COLUMN', @level2name = N'Id';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UnsubscriptionEmail') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UnsubscriptionEmail', @level2type = N'COLUMN', @level2name = N'Email';
GO

-- Table: UserAccounts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserAccounts') AND c.name = 'UserAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts', @level2type = N'COLUMN', @level2name = N'UserAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserAccounts') AND c.name = 'AccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Accounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts', @level2type = N'COLUMN', @level2name = N'AccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserAccounts') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserAccounts') AND c.name = 'BudgetAccountId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BudgetAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts', @level2type = N'COLUMN', @level2name = N'BudgetAccountId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserAccounts') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserAccounts') AND c.name = 'AllocationAmount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserAccounts', @level2type = N'COLUMN', @level2name = N'AllocationAmount';
GO

-- Table: UserCategory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserCategory') AND c.name = 'UserCategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to UserCategory table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserCategory', @level2type = N'COLUMN', @level2name = N'UserCategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserCategory') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserCategory', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserCategory') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserCategory', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO

-- Table: UserImports
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserImports') AND c.name = 'Account Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserImports', @level2type = N'COLUMN', @level2name = N'Account Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserImports') AND c.name = 'Amount' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Monetary amount', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserImports', @level2type = N'COLUMN', @level2name = N'Amount';
GO

-- Table: Users
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'SchoolId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to School table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'SchoolId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'UserName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'UserName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'DistrictAcctgCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'DistrictAcctgCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'Email' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Email address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'Email';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'SecurityRoleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to SecurityRoles table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'SecurityRoleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'FirstName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'FirstName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'LastName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'LastName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Users') AND c.name = 'ResetPasswordCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Users', @level2type = N'COLUMN', @level2name = N'ResetPasswordCode';
GO

-- Table: UserTrees
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserTrees') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserTrees', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserTrees') AND c.name = 'UserId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Users/UserAccounts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserTrees', @level2type = N'COLUMN', @level2name = N'UserId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.UserTrees') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'UserTrees', @level2type = N'COLUMN', @level2name = N'Status';
GO

-- Table: VendorCatalogNote
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCatalogNote') AND c.name = 'VendorCatalogNoteId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorCatalogNote table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCatalogNote', @level2type = N'COLUMN', @level2name = N'VendorCatalogNoteId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCatalogNote') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCatalogNote', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCatalogNote') AND c.name = 'CatalogId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Catalog table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCatalogNote', @level2type = N'COLUMN', @level2name = N'CatalogId';
GO

-- Table: VendorCategory
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategory') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategory', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategory') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategory', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategory') AND c.name = 'VendorName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategory', @level2type = N'COLUMN', @level2name = N'VendorName';
GO

-- Table: VendorCategoryPP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategoryPP') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategoryPP', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategoryPP') AND c.name = 'CategoryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Category table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategoryPP', @level2type = N'COLUMN', @level2name = N'CategoryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategoryPP') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategoryPP', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCategoryPP') AND c.name = 'PricePlanId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PricePlans table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCategoryPP', @level2type = N'COLUMN', @level2name = N'PricePlanId';
GO

-- Table: VendorCertificates
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCertificates') AND c.name = 'VendorCertificateId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorCertificates table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCertificates', @level2type = N'COLUMN', @level2name = N'VendorCertificateId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCertificates') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCertificates', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorCertificates') AND c.name = 'CertificateAuthorityId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CertificateAuthority table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorCertificates', @level2type = N'COLUMN', @level2name = N'CertificateAuthorityId';
GO

-- Table: VendorContacts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'VendorContactId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorContacts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'VendorContactId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'SalutationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Salutations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'SalutationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'FirstName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'FirstName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'LastName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'LastName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'Phone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorContacts') AND c.name = 'FullName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorContacts', @level2type = N'COLUMN', @level2name = N'FullName';
GO

-- Table: VendorDeliveryRule
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDeliveryRule') AND c.name = 'VendorDeliveryRuleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorDeliveryRule table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDeliveryRule', @level2type = N'COLUMN', @level2name = N'VendorDeliveryRuleId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDeliveryRule') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDeliveryRule', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDeliveryRule') AND c.name = 'Description' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Text description of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDeliveryRule', @level2type = N'COLUMN', @level2name = N'Description';
GO

-- Table: VendorDocRequest
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'VendorDocRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorDocRequest table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'VendorDocRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'EmailAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'EmailAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'EmailCCAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'EmailCCAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'VendorDocRequestNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'VendorDocRequestNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequest') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequest', @level2type = N'COLUMN', @level2name = N'ContactName';
GO

-- Table: VendorDocRequestDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'VendorDocRequestDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorDocRequestDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'VendorDocRequestDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'BidHeaderCheckListId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidHeaderCheckList table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderCheckListId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'VendorDocRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorDocRequest table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'VendorDocRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestDetail') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestDetail', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO

-- Table: VendorDocRequestStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestStatus') AND c.name = 'VendorDocRequestStatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestStatus', @level2type = N'COLUMN', @level2name = N'VendorDocRequestStatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestStatus') AND c.name = 'VendorDocRequestId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorDocRequest table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestStatus', @level2type = N'COLUMN', @level2name = N'VendorDocRequestId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorDocRequestStatus') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorDocRequestStatus', @level2type = N'COLUMN', @level2name = N'StatusId';
GO

-- Table: VendorLocations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorLocations') AND c.name = 'VendorLocationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorLocations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorLocations', @level2type = N'COLUMN', @level2name = N'VendorLocationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorLocations') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorLocations', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorLocations') AND c.name = 'LocationCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorLocations', @level2type = N'COLUMN', @level2name = N'LocationCode';
GO

-- Table: VendorOrders
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorOrders') AND c.name = 'VendorOrderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorOrders table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorOrders', @level2type = N'COLUMN', @level2name = N'VendorOrderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorOrders') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorOrders', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorOrders') AND c.name = 'POId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to PO table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorOrders', @level2type = N'COLUMN', @level2name = N'POId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorOrders') AND c.name = 'VendorStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorOrders', @level2type = N'COLUMN', @level2name = N'VendorStatus';
GO

-- Table: VendorQuery
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'VendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'VendorQueryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'EmailAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'EmailAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'EmailCCAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'EmailCCAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'VendorQueryNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'VendorQueryNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQuery') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQuery', @level2type = N'COLUMN', @level2name = N'ContactName';
GO

-- Table: VendorQueryDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'VendorQueryDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'VendorQueryDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'BidResultsId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidResults table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'BidResultsId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'VendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'VendorQueryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'ItemQueryNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'ItemQueryNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryDetail') AND c.name = 'CommonVendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to CommonVendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryDetail', @level2type = N'COLUMN', @level2name = N'CommonVendorQueryId';
GO

-- Table: VendorQueryMSRP
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'VendorQueryMSRPId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryMSRP table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'VendorQueryMSRPId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'EmailAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'EmailAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'EmailCCAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'EmailCCAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'VendorQueryMSRPNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'VendorQueryMSRPNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRP') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRP', @level2type = N'COLUMN', @level2name = N'ContactName';
GO

-- Table: VendorQueryMSRPDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND c.name = 'VendorQueryMSRPDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryMSRPDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail', @level2type = N'COLUMN', @level2name = N'VendorQueryMSRPDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND c.name = 'VendorQueryMSRPId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryMSRP table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail', @level2type = N'COLUMN', @level2name = N'VendorQueryMSRPId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND c.name = 'MSRPQueryNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail', @level2type = N'COLUMN', @level2name = N'MSRPQueryNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPDetail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPDetail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: VendorQueryMSRPStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPStatus') AND c.name = 'VendorQueryMSRPStatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPStatus', @level2type = N'COLUMN', @level2name = N'VendorQueryMSRPStatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPStatus') AND c.name = 'VendorQueryMSRPId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryMSRP table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPStatus', @level2type = N'COLUMN', @level2name = N'VendorQueryMSRPId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryMSRPStatus') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryMSRPStatus', @level2type = N'COLUMN', @level2name = N'StatusId';
GO

-- Table: VendorQueryStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryStatus') AND c.name = 'VendorQueryStatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryStatus', @level2type = N'COLUMN', @level2name = N'VendorQueryStatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryStatus') AND c.name = 'VendorQueryId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQuery table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryStatus', @level2type = N'COLUMN', @level2name = N'VendorQueryId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryStatus') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryStatus', @level2type = N'COLUMN', @level2name = N'StatusId';
GO

-- Table: VendorQueryTandM
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'VendorQueryTandMId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryTandM table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'VendorQueryTandMId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'EmailAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'EmailAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'EmailCCAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'EmailCCAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'VendorQueryTandMNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'VendorQueryTandMNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandM') AND c.name = 'ContactName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandM', @level2type = N'COLUMN', @level2name = N'ContactName';
GO

-- Table: VendorQueryTandMDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND c.name = 'VendorQueryTandMDetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryTandMDetail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail', @level2type = N'COLUMN', @level2name = N'VendorQueryTandMDetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND c.name = 'BidHeaderId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to parent header record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail', @level2type = N'COLUMN', @level2name = N'BidHeaderId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND c.name = 'BidImportId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to BidImports table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail', @level2type = N'COLUMN', @level2name = N'BidImportId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND c.name = 'VendorQueryTandMId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryTandM table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail', @level2type = N'COLUMN', @level2name = N'VendorQueryTandMId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND c.name = 'TandMQueryNotes' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Additional notes or comments', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail', @level2type = N'COLUMN', @level2name = N'TandMQueryNotes';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMDetail') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMDetail', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: VendorQueryTandMStatus
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMStatus') AND c.name = 'VendorQueryTandMStatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMStatus', @level2type = N'COLUMN', @level2name = N'VendorQueryTandMStatusId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMStatus') AND c.name = 'VendorQueryTandMId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorQueryTandM table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMStatus', @level2type = N'COLUMN', @level2name = N'VendorQueryTandMId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorQueryTandMStatus') AND c.name = 'StatusId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to status lookup', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorQueryTandMStatus', @level2type = N'COLUMN', @level2name = N'StatusId';
GO

-- Table: Vendors
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'Code' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'Code';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'City' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'City name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'City';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'State' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'State/province code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'State';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'ZipCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Postal/ZIP code', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'ZipCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'Phone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'Phone';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'HostUserName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'HostUserName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'cXMLAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'cXMLAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.Vendors') AND c.name = 'VendorDeliveryRuleId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorDeliveryRule table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'Vendors', @level2type = N'COLUMN', @level2name = N'VendorDeliveryRuleId';
GO

-- Table: VendorSessions
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorSessions') AND c.name = 'VendorSessionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VendorSessions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorSessions', @level2type = N'COLUMN', @level2name = N'VendorSessionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorSessions') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorSessions', @level2type = N'COLUMN', @level2name = N'VendorId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorSessions') AND c.name = 'UserName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorSessions', @level2type = N'COLUMN', @level2name = N'UserName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorSessions') AND c.name = 'IPAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorSessions', @level2type = N'COLUMN', @level2name = N'IPAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorSessions') AND c.name = 'VPORegistrationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VPORegistrations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorSessions', @level2type = N'COLUMN', @level2name = N'VPORegistrationId';
GO

-- Table: VendorUploads
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorUploads') AND c.name = 'FileName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorUploads', @level2type = N'COLUMN', @level2name = N'FileName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VendorUploads') AND c.name = 'Status' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VendorUploads', @level2type = N'COLUMN', @level2name = N'Status';
GO

-- Table: VPOLoginAttempts
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOLoginAttempts') AND c.name = 'VPOLoginAttemptId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VPOLoginAttempts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOLoginAttempts', @level2type = N'COLUMN', @level2name = N'VPOLoginAttemptId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOLoginAttempts') AND c.name = 'VPOUserCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOLoginAttempts', @level2type = N'COLUMN', @level2name = N'VPOUserCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOLoginAttempts') AND c.name = 'VPORegistrationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VPORegistrations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOLoginAttempts', @level2type = N'COLUMN', @level2name = N'VPORegistrationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOLoginAttempts') AND c.name = 'IPAddress' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Street address', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOLoginAttempts', @level2type = N'COLUMN', @level2name = N'IPAddress';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOLoginAttempts') AND c.name = 'LoginStatus' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Current status of the record', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOLoginAttempts', @level2type = N'COLUMN', @level2name = N'LoginStatus';
GO

-- Table: VPORegistrations
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPORegistrations') AND c.name = 'VPORegistrationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VPORegistrations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPORegistrations', @level2type = N'COLUMN', @level2name = N'VPORegistrationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPORegistrations') AND c.name = 'VPOUserCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPORegistrations', @level2type = N'COLUMN', @level2name = N'VPOUserCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPORegistrations') AND c.name = 'VPOName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPORegistrations', @level2type = N'COLUMN', @level2name = N'VPOName';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPORegistrations') AND c.name = 'VPOPhone' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Phone number', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPORegistrations', @level2type = N'COLUMN', @level2name = N'VPOPhone';
GO

-- Table: VPOVendorLinks
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOVendorLinks') AND c.name = 'VPOVendorLinkId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VPOVendorLinks table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOVendorLinks', @level2type = N'COLUMN', @level2name = N'VPOVendorLinkId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOVendorLinks') AND c.name = 'VPORegistrationId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to VPORegistrations table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOVendorLinks', @level2type = N'COLUMN', @level2name = N'VPORegistrationId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.VPOVendorLinks') AND c.name = 'VendorId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Vendors table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'VPOVendorLinks', @level2type = N'COLUMN', @level2name = N'VendorId';
GO

-- Table: WizHelpFile
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.WizHelpFile') AND c.name = 'Id' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Primary key identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'WizHelpFile', @level2type = N'COLUMN', @level2name = N'Id';
GO

-- Table: YearlyTotals
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.YearlyTotals') AND c.name = 'BudgetId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Budgets table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'YearlyTotals', @level2type = N'COLUMN', @level2name = N'BudgetId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.YearlyTotals') AND c.name = 'Name' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'YearlyTotals', @level2type = N'COLUMN', @level2name = N'Name';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.YearlyTotals') AND c.name = 'DistrictId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Districts table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'YearlyTotals', @level2type = N'COLUMN', @level2name = N'DistrictId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.YearlyTotals') AND c.name = 'DistrictName' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Display name', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'YearlyTotals', @level2type = N'COLUMN', @level2name = N'DistrictName';
GO

-- Table: z4zbBidFix
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbBidFix') AND c.name = 'PackedCode' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Short code or identifier', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix', @level2type = N'COLUMN', @level2name = N'PackedCode';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbBidFix') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbBidFix') AND c.name = 'z4ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix', @level2type = N'COLUMN', @level2name = N'z4ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbBidFix') AND c.name = 'z4BidQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix', @level2type = N'COLUMN', @level2name = N'z4BidQuantity';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbBidFix') AND c.name = 'zbItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix', @level2type = N'COLUMN', @level2name = N'zbItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbBidFix') AND c.name = 'zbBidQuantity' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Numeric quantity', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbBidFix', @level2type = N'COLUMN', @level2name = N'zbBidQuantity';
GO

-- Table: z4zbReqDetail
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbReqDetail') AND c.name = 'RequisitionId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Requisitions table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail', @level2type = N'COLUMN', @level2name = N'RequisitionId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbReqDetail') AND c.name = 'DetailId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Detail table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail', @level2type = N'COLUMN', @level2name = N'DetailId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbReqDetail') AND c.name = 'ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail', @level2type = N'COLUMN', @level2name = N'ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbReqDetail') AND c.name = 'BidItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail', @level2type = N'COLUMN', @level2name = N'BidItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbReqDetail') AND c.name = 'z4ItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail', @level2type = N'COLUMN', @level2name = N'z4ItemId';
GO
IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('dbo.z4zbReqDetail') AND c.name = 'zbItemId' AND ep.name = 'MS_Description')
    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'Foreign key to Items table', @level0type = N'SCHEMA', @level0name = N'dbo', @level1type = N'TABLE', @level1name = N'z4zbReqDetail', @level2type = N'COLUMN', @level2name = N'zbItemId';
GO
