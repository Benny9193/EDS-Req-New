# EDS Database Data Dictionary

Generated: 2026-03-27 12:42:28

---

## Summary

| Metric | Count |
|--------|-------|
| Tables | 439 |
| Table Columns | 4644 |
| Views | 475 |
| View Columns | 6866 |
| Tables with Primary Keys | 345 |
| Foreign Key Relationships | 31 |
| Indexes | 1,117 |

### Tables Without Primary Keys (94)

| Schema | Table | Rows |
|--------|-------|------|
| EDSIQWebUser | migratorversions | 0 |
| archive | Approvals | 3,517,361 |
| archive | ApprovalsHistory | 447,389 |
| archive | Awards | 143,977 |
| archive | BatchDetail | 4,060,286 |
| archive | BidHeaderCheckList | 4,521 |
| archive | BidHeaderDetail | 26,252,593 |
| archive | BidHeaderDocument | 11,787 |
| archive | BidHeaderDocuments | 0 |
| archive | BidHeaders | 3,395 |
| archive | BidImports | 42,011 |
| archive | BidMSRPResults | 10,848 |
| archive | BidMappedItems | 0 |
| archive | BidReawards | 0 |
| archive | BidRequestItems | 5,704,577 |
| archive | BidRequestManufacturer | 0 |
| archive | BidRequestOptions | 0 |
| archive | BidRequestPriceRanges | 0 |
| archive | BidResults | 30,585,282 |
| archive | BidTrades | 119 |
| archive | Bids | 172,256 |
| archive | Catalog | 2,422 |
| archive | DMSBidDocuments | 0 |
| archive | DMSVendorBidDocuments | 0 |
| archive | Detail | 25,480,018 |
| archive | DetailHold | 0 |
| archive | DetailMatch | 1,499 |
| archive | FreezeItems | 0 |
| archive | ItemContractPrices | 0 |
| archive | OrderBooks | 692 |
| archive | PO | 1,300,617 |
| archive | PODetailItems | 22,905,929 |
| archive | POTempDetails | 0 |
| archive | Prices | 0 |
| archive | PricingConsolidatedOrderCounts | 0 |
| archive | PricingMap | 0 |
| archive | PricingUpdate | 0 |
| archive | RequisitionChangeLog | 1,936,897 |
| archive | Requisitions | 1,433,904 |
| archive | TMAwards | 29,335 |
| archive | UserAccounts | 2,704,140 |
| archive | UserAccountsUserAccountId_CrossMapping | 2,704,140 |
| archive | VendorDocRequest | 0 |
| archive | VendorDocRequestDetail | 0 |
| archive | VendorQuery | 4,057 |
| archive | VendorQueryDetail | 39,321 |
| archive | VendorQueryMSRP | 0 |
| archive | VendorQueryMSRPDetail | 0 |
| archive | VendorQueryTandM | 7 |
| archive | VendorQueryTandMDetail | 0 |
| archive | allitems | 0 |
| archive | cxmlSession | 50,022 |
| dbo | BidRequestItemMergeActions_Saved_101521 | 27,298 |
| dbo | CatList | 155,059 |
| dbo | CommonMSRPVendorQuery | 4 |
| dbo | CommonTandMVendorQuery | 22 |
| dbo | CommonVendorQuery | 43 |
| dbo | DetailHold | 1 |
| dbo | DetailMatch | 103,534 |
| dbo | DistrictProposedCharges | 12,015 |
| dbo | EmailBlastAddresses08132012 | 271 |
| dbo | FreezeItems2015 | 105,203 |
| dbo | HeaderWorkItems | 491,824 |
| dbo | Notifications | 720 |
| dbo | OBPrices | 0 |
| dbo | POTemp | 37 |
| dbo | POTempDetails | 4,014 |
| dbo | RTK_2010NJHSL | 3,322 |
| dbo | ResetPasswordTracking | 105,046 |
| dbo | SDS_Rpt_Bridge | 100 |
| dbo | SSOLoginTracking | 156,019 |
| dbo | SaxDups | 31,171 |
| dbo | SaxNotifications | 78 |
| dbo | SulphiteDetail | 6,280 |
| dbo | SulphiteImport | 49 |
| dbo | TMImport1 | 1,885 |
| dbo | TMImport2 | 147 |
| dbo | TMImport3 | 833 |
| dbo | TMImport5 | 2,889 |
| dbo | TMImport6 | 2,134 |
| dbo | TagFilePos_ | 2,259 |
| dbo | TagFile_ | 6,235 |
| dbo | TagSet_ | 0 |
| dbo | TempIrvingtonWincap | 860 |
| dbo | TmpLog | 461 |
| dbo | UserImports | 328 |
| dbo | VendorDeliveryRule | 1 |
| dbo | VendorPOtags | 0 |
| dbo | WizHelpFile | 0 |
| dbo | YearlyTotals | 10,432 |
| dbo | allitems | 6,276,768 |
| dbo | dchtest | 1,192 |
| dbo | z4zbBidFix | 0 |
| dbo | z4zbReqDetail | 0 |

---

## Table of Contents

### Schema: EDSIQWebUser

- [TableOfContents](#edsiqwebuser-tableofcontents)
- [UnsubscriptionEmail](#edsiqwebuser-unsubscriptionemail)
- [migratorversions](#edsiqwebuser-migratorversions)

### Schema: EDSWebRpts

- [REPMAN_GROUPS](#edswebrpts-repman-groups)
- [REPMAN_REPORTS](#edswebrpts-repman-reports)

### Schema: archive

- [Approvals](#archive-approvals)
- [ApprovalsHistory](#archive-approvalshistory)
- [Awards](#archive-awards)
- [BatchDetail](#archive-batchdetail)
- [BidHeaderCheckList](#archive-bidheaderchecklist)
- [BidHeaderDetail](#archive-bidheaderdetail)
- [BidHeaderDocument](#archive-bidheaderdocument)
- [BidHeaderDocuments](#archive-bidheaderdocuments)
- [BidHeaders](#archive-bidheaders)
- [BidImports](#archive-bidimports)
- [BidMSRPResults](#archive-bidmsrpresults)
- [BidMappedItems](#archive-bidmappeditems)
- [BidReawards](#archive-bidreawards)
- [BidRequestItems](#archive-bidrequestitems)
- [BidRequestManufacturer](#archive-bidrequestmanufacturer)
- [BidRequestOptions](#archive-bidrequestoptions)
- [BidRequestPriceRanges](#archive-bidrequestpriceranges)
- [BidResults](#archive-bidresults)
- [BidTrades](#archive-bidtrades)
- [Bids](#archive-bids)
- [Catalog](#archive-catalog)
- [DMSBidDocuments](#archive-dmsbiddocuments)
- [DMSVendorBidDocuments](#archive-dmsvendorbiddocuments)
- [Detail](#archive-detail)
- [DetailHold](#archive-detailhold)
- [DetailMatch](#archive-detailmatch)
- [FreezeItems](#archive-freezeitems)
- [ItemContractPrices](#archive-itemcontractprices)
- [OrderBooks](#archive-orderbooks)
- [PO](#archive-po)
- [PODetailItems](#archive-podetailitems)
- [POTempDetails](#archive-potempdetails)
- [Prices](#archive-prices)
- [PricingConsolidatedOrderCounts](#archive-pricingconsolidatedordercounts)
- [PricingMap](#archive-pricingmap)
- [PricingUpdate](#archive-pricingupdate)
- [RequisitionChangeLog](#archive-requisitionchangelog)
- [Requisitions](#archive-requisitions)
- [TMAwards](#archive-tmawards)
- [UserAccounts](#archive-useraccounts)
- [UserAccountsUserAccountId_CrossMapping](#archive-useraccountsuseraccountid-crossmapping)
- [VendorDocRequest](#archive-vendordocrequest)
- [VendorDocRequestDetail](#archive-vendordocrequestdetail)
- [VendorQuery](#archive-vendorquery)
- [VendorQueryDetail](#archive-vendorquerydetail)
- [VendorQueryMSRP](#archive-vendorquerymsrp)
- [VendorQueryMSRPDetail](#archive-vendorquerymsrpdetail)
- [VendorQueryTandM](#archive-vendorquerytandm)
- [VendorQueryTandMDetail](#archive-vendorquerytandmdetail)
- [allitems](#archive-allitems)
- [cxmlSession](#archive-cxmlsession)

### Schema: dbo

- [AccountSeparators](#dbo-accountseparators)
- [AccountingDetail](#dbo-accountingdetail)
- [AccountingFormats](#dbo-accountingformats)
- [AccountingUserFields](#dbo-accountinguserfields)
- [Accounts](#dbo-accounts)
- [AddendumItems](#dbo-addendumitems)
- [Alerts](#dbo-alerts)
- [AnswerTypes](#dbo-answertypes)
- [ApprovalLevels](#dbo-approvallevels)
- [Approvals](#dbo-approvals)
- [ApprovalsHistory](#dbo-approvalshistory)
- [Audit](#dbo-audit)
- [AwardTypes](#dbo-awardtypes)
- [Awardings](#dbo-awardings)
- [Awards](#dbo-awards)
- [AwardsCatalogList](#dbo-awardscataloglist)
- [BatchBook](#dbo-batchbook)
- [BatchDetail](#dbo-batchdetail)
- [BatchDetailInserts](#dbo-batchdetailinserts)
- [Batches](#dbo-batches)
- [BidAnswers](#dbo-bidanswers)
- [BidAnswersJournal](#dbo-bidanswersjournal)
- [BidCalendar](#dbo-bidcalendar)
- [BidDocument](#dbo-biddocument)
- [BidDocumentTypes](#dbo-biddocumenttypes)
- [BidHeaderCheckList](#dbo-bidheaderchecklist)
- [BidHeaderDetail](#dbo-bidheaderdetail)
- [BidHeaderDetail_Orig](#dbo-bidheaderdetail-orig)
- [BidHeaderDocument](#dbo-bidheaderdocument)
- [BidHeaderDocuments](#dbo-bidheaderdocuments)
- [BidHeaders](#dbo-bidheaders)
- [BidImportCatalogList](#dbo-bidimportcataloglist)
- [BidImportCounties](#dbo-bidimportcounties)
- [BidImports](#dbo-bidimports)
- [BidItems](#dbo-biditems)
- [BidItems_Old](#dbo-biditems-old)
- [BidMSRPResultPrices](#dbo-bidmsrpresultprices)
- [BidMSRPResults](#dbo-bidmsrpresults)
- [BidMSRPResultsProductLines](#dbo-bidmsrpresultsproductlines)
- [BidManagers](#dbo-bidmanagers)
- [BidManufacturers](#dbo-bidmanufacturers)
- [BidMappedItems](#dbo-bidmappeditems)
- [BidMgrConfiguration](#dbo-bidmgrconfiguration)
- [BidMgrTagFile](#dbo-bidmgrtagfile)
- [BidPackage](#dbo-bidpackage)
- [BidPackageDocument](#dbo-bidpackagedocument)
- [BidProductLinePrices](#dbo-bidproductlineprices)
- [BidProductLines](#dbo-bidproductlines)
- [BidQuestions](#dbo-bidquestions)
- [BidReawards](#dbo-bidreawards)
- [BidRequestItemMergeActions](#dbo-bidrequestitemmergeactions)
- [BidRequestItemMergeActions_Orig](#dbo-bidrequestitemmergeactions-orig)
- [BidRequestItemMergeActions_Saved_101521](#dbo-bidrequestitemmergeactions-saved-101521)
- [BidRequestItems](#dbo-bidrequestitems)
- [BidRequestItems_Orig](#dbo-bidrequestitems-orig)
- [BidRequestManufacturer](#dbo-bidrequestmanufacturer)
- [BidRequestOptions](#dbo-bidrequestoptions)
- [BidRequestPriceRanges](#dbo-bidrequestpriceranges)
- [BidRequestProductLines](#dbo-bidrequestproductlines)
- [BidResponses](#dbo-bidresponses)
- [BidResultChanges](#dbo-bidresultchanges)
- [BidResults](#dbo-bidresults)
- [BidResultsChangeLog](#dbo-bidresultschangelog)
- [BidResults_Orig](#dbo-bidresults-orig)
- [BidTradeCounties](#dbo-bidtradecounties)
- [BidTrades](#dbo-bidtrades)
- [BidTypes](#dbo-bidtypes)
- [BidderCheckList](#dbo-bidderchecklist)
- [BidderCheckListPkgDetail](#dbo-bidderchecklistpkgdetail)
- [BidderCheckListPkgHeader](#dbo-bidderchecklistpkgheader)
- [Bids](#dbo-bids)
- [BidsCatalogList](#dbo-bidscataloglist)
- [BookTypes](#dbo-booktypes)
- [BudgetAccounts](#dbo-budgetaccounts)
- [Budgets](#dbo-budgets)
- [CSCommands](#dbo-cscommands)
- [CSMessageFiles](#dbo-csmessagefiles)
- [CSMessages](#dbo-csmessages)
- [CSRep](#dbo-csrep)
- [CXmlSession](#dbo-cxmlsession)
- [CalDistricts](#dbo-caldistricts)
- [CalendarDates](#dbo-calendardates)
- [CalendarIB](#dbo-calendarib)
- [CalendarItems](#dbo-calendaritems)
- [CalendarTypes](#dbo-calendartypes)
- [Calendars](#dbo-calendars)
- [Carolina Living Items](#dbo-carolina-living-items)
- [CatList](#dbo-catlist)
- [Catalog](#dbo-catalog)
- [CatalogImportFields](#dbo-catalogimportfields)
- [CatalogImportMap](#dbo-catalogimportmap)
- [CatalogPricing](#dbo-catalogpricing)
- [CatalogRequest](#dbo-catalogrequest)
- [CatalogRequestDetail](#dbo-catalogrequestdetail)
- [CatalogRequestStatus](#dbo-catalogrequeststatus)
- [CatalogText](#dbo-catalogtext)
- [CatalogTextParts](#dbo-catalogtextparts)
- [Category](#dbo-category)
- [CertificateAuthority](#dbo-certificateauthority)
- [ChargeTypes](#dbo-chargetypes)
- [CommonMSRPVendorQuery](#dbo-commonmsrpvendorquery)
- [CommonTandMVendorQuery](#dbo-commontandmvendorquery)
- [CommonVendorQuery](#dbo-commonvendorquery)
- [CommonVendorQueryAnswer](#dbo-commonvendorqueryanswer)
- [ContractTypes](#dbo-contracttypes)
- [Control](#dbo-control)
- [Coops](#dbo-coops)
- [CopyRequests](#dbo-copyrequests)
- [Counties](#dbo-counties)
- [CoverView](#dbo-coverview)
- [CrossRefs](#dbo-crossrefs)
- [DMSBidDocuments](#dbo-dmsbiddocuments)
- [DMSSDSDocuments](#dbo-dmssdsdocuments)
- [DMSVendorBidDocuments](#dbo-dmsvendorbiddocuments)
- [DMSVendorDocuments](#dbo-dmsvendordocuments)
- [DebugMsgs](#dbo-debugmsgs)
- [DebugMsgs_Orig](#dbo-debugmsgs-orig)
- [Detail](#dbo-detail)
- [DetailChangeLog](#dbo-detailchangelog)
- [DetailChanges](#dbo-detailchanges)
- [DetailHold](#dbo-detailhold)
- [DetailMatch](#dbo-detailmatch)
- [DetailNotifications](#dbo-detailnotifications)
- [DetailUploads](#dbo-detailuploads)
- [District](#dbo-district)
- [DistrictCategories](#dbo-districtcategories)
- [DistrictCategoryTitles](#dbo-districtcategorytitles)
- [DistrictCharges](#dbo-districtcharges)
- [DistrictChargesNotes](#dbo-districtchargesnotes)
- [DistrictContactTypes](#dbo-districtcontacttypes)
- [DistrictContacts](#dbo-districtcontacts)
- [DistrictContinuances](#dbo-districtcontinuances)
- [DistrictNoteType](#dbo-districtnotetype)
- [DistrictNotes](#dbo-districtnotes)
- [DistrictNotifications](#dbo-districtnotifications)
- [DistrictPP](#dbo-districtpp)
- [DistrictProposedCharges](#dbo-districtproposedcharges)
- [DistrictReports](#dbo-districtreports)
- [DistrictTypes](#dbo-districttypes)
- [DistrictVendor](#dbo-districtvendor)
- [EmailBlast](#dbo-emailblast)
- [EmailBlastAddresses08132012](#dbo-emailblastaddresses08132012)
- [EmailBlastCopy](#dbo-emailblastcopy)
- [EmailBlastLog](#dbo-emailblastlog)
- [FreezeItems](#dbo-freezeitems)
- [FreezeItems2015](#dbo-freezeitems2015)
- [HeaderWorkItems](#dbo-headerworkitems)
- [Headings](#dbo-headings)
- [HolidayCalendar](#dbo-holidaycalendar)
- [HolidayCalendarVendor](#dbo-holidaycalendarvendor)
- [IPQueue](#dbo-ipqueue)
- [IPQueueUsers](#dbo-ipqueueusers)
- [ImageErrors](#dbo-imageerrors)
- [ImageLog](#dbo-imagelog)
- [Images](#dbo-images)
- [ImportCatalogDetail](#dbo-importcatalogdetail)
- [ImportCatalogHeader](#dbo-importcatalogheader)
- [ImportDetail](#dbo-importdetail)
- [ImportMessages](#dbo-importmessages)
- [ImportProcesses](#dbo-importprocesses)
- [Imports](#dbo-imports)
- [InstructionBookContents](#dbo-instructionbookcontents)
- [InstructionBookTypes](#dbo-instructionbooktypes)
- [Instructions](#dbo-instructions)
- [InvoiceTypes](#dbo-invoicetypes)
- [Invoices](#dbo-invoices)
- [ItemContractPrices](#dbo-itemcontractprices)
- [ItemDocuments](#dbo-itemdocuments)
- [ItemUpdates](#dbo-itemupdates)
- [Items](#dbo-items)
- [Keywords](#dbo-keywords)
- [LL_RepArea](#dbo-ll-reparea)
- [LL_RepLay](#dbo-ll-replay)
- [Ledger](#dbo-ledger)
- [MSDS](#dbo-msds)
- [MSDSDetail](#dbo-msdsdetail)
- [MSRPExcelExport](#dbo-msrpexcelexport)
- [MSRPExcelImport](#dbo-msrpexcelimport)
- [MSRPOptions](#dbo-msrpoptions)
- [ManufacturerProductLines](#dbo-manufacturerproductlines)
- [Manufacturers](#dbo-manufacturers)
- [MappedItems](#dbo-mappeditems)
- [Menus](#dbo-menus)
- [Messages](#dbo-messages)
- [Months](#dbo-months)
- [NextNumber](#dbo-nextnumber)
- [NotificationOptions](#dbo-notificationoptions)
- [Notifications](#dbo-notifications)
- [OBPrices](#dbo-obprices)
- [OBView](#dbo-obview)
- [Options](#dbo-options)
- [OptionsLink](#dbo-optionslink)
- [OrderBookAlwaysAdd](#dbo-orderbookalwaysadd)
- [OrderBookDetail](#dbo-orderbookdetail)
- [OrderBookDetailOld](#dbo-orderbookdetailold)
- [OrderBookLog](#dbo-orderbooklog)
- [OrderBookTypes](#dbo-orderbooktypes)
- [OrderBooks](#dbo-orderbooks)
- [PO](#dbo-po)
- [PODetailItems](#dbo-podetailitems)
- [POIDTable](#dbo-poidtable)
- [POLayoutDetail](#dbo-polayoutdetail)
- [POLayoutFields](#dbo-polayoutfields)
- [POLayouts](#dbo-polayouts)
- [POPageSummary](#dbo-popagesummary)
- [POPrintTaggedPOFile](#dbo-poprinttaggedpofile)
- [POQueue](#dbo-poqueue)
- [POQueueItems](#dbo-poqueueitems)
- [POStatus](#dbo-postatus)
- [POStatusTable](#dbo-postatustable)
- [POTemp](#dbo-potemp)
- [POTempDetails](#dbo-potempdetails)
- [PPCatalogs](#dbo-ppcatalogs)
- [PPCategory](#dbo-ppcategory)
- [PaymentTypes](#dbo-paymenttypes)
- [Payments](#dbo-payments)
- [PendingApprovals](#dbo-pendingapprovals)
- [PostCatalogDetail](#dbo-postcatalogdetail)
- [PostCatalogHeader](#dbo-postcatalogheader)
- [PriceHolds](#dbo-priceholds)
- [PriceListTypes](#dbo-pricelisttypes)
- [PricePlans](#dbo-priceplans)
- [PriceRanges](#dbo-priceranges)
- [Prices](#dbo-prices)
- [PricingAddenda](#dbo-pricingaddenda)
- [PricingConsolidatedOrderCounts](#dbo-pricingconsolidatedordercounts)
- [PricingMap](#dbo-pricingmap)
- [PricingUpdate](#dbo-pricingupdate)
- [PrintDocuments](#dbo-printdocuments)
- [Printers](#dbo-printers)
- [ProductVerificationResults](#dbo-productverificationresults)
- [ProjectTasks](#dbo-projecttasks)
- [QuestionnaireResponses](#dbo-questionnaireresponses)
- [RTK_2010NJHSL](#dbo-rtk-2010njhsl)
- [RTK_CASFile](#dbo-rtk-casfile)
- [RTK_ContainerCodes](#dbo-rtk-containercodes)
- [RTK_Documents](#dbo-rtk-documents)
- [RTK_FactSheets](#dbo-rtk-factsheets)
- [RTK_HealthHazardCodes](#dbo-rtk-healthhazardcodes)
- [RTK_Inventories](#dbo-rtk-inventories)
- [RTK_InventoryRangeCodes](#dbo-rtk-inventoryrangecodes)
- [RTK_Items](#dbo-rtk-items)
- [RTK_LegacyDistrictCodesMap](#dbo-rtk-legacydistrictcodesmap)
- [RTK_LegacySchoolFile](#dbo-rtk-legacyschoolfile)
- [RTK_MSDSDetail](#dbo-rtk-msdsdetail)
- [RTK_MixtureCodes](#dbo-rtk-mixturecodes)
- [RTK_Purposes](#dbo-rtk-purposes)
- [RTK_ReportItems](#dbo-rtk-reportitems)
- [RTK_Sites](#dbo-rtk-sites)
- [RTK_Surveys](#dbo-rtk-surveys)
- [RTK_Training](#dbo-rtk-training)
- [RTK_UOMCodes](#dbo-rtk-uomcodes)
- [RTK_VendorLinks](#dbo-rtk-vendorlinks)
- [RateTypes](#dbo-ratetypes)
- [RateUnits](#dbo-rateunits)
- [Rates](#dbo-rates)
- [Receiving](#dbo-receiving)
- [ReportSession](#dbo-reportsession)
- [ReportSessionLinks](#dbo-reportsessionlinks)
- [ReqAudit](#dbo-reqaudit)
- [RequisitionChangeLog](#dbo-requisitionchangelog)
- [RequisitionNoteEmails](#dbo-requisitionnoteemails)
- [RequisitionNotes](#dbo-requisitionnotes)
- [Requisitions](#dbo-requisitions)
- [ResetPasswordTracking](#dbo-resetpasswordtracking)
- [Rights](#dbo-rights)
- [RightsLink](#dbo-rightslink)
- [SDSDocs](#dbo-sdsdocs)
- [SDSErrors](#dbo-sdserrors)
- [SDSLog](#dbo-sdslog)
- [SDSResults](#dbo-sdsresults)
- [SDSSyncStatus](#dbo-sdssyncstatus)
- [SDS_Rpt_Bridge](#dbo-sds-rpt-bridge)
- [SDSs](#dbo-sdss)
- [SSOLoginTracking](#dbo-ssologintracking)
- [SafetyDataSheets](#dbo-safetydatasheets)
- [Salutations](#dbo-salutations)
- [SaxDups](#dbo-saxdups)
- [SaxNotifications](#dbo-saxnotifications)
- [ScanEvents](#dbo-scanevents)
- [ScanJobs](#dbo-scanjobs)
- [ScannerZones](#dbo-scannerzones)
- [ScheduleTypes](#dbo-scheduletypes)
- [ScheduledTask](#dbo-scheduledtask)
- [School](#dbo-school)
- [SearchKeywords](#dbo-searchkeywords)
- [SearchSets](#dbo-searchsets)
- [Sections](#dbo-sections)
- [SecurityKeys](#dbo-securitykeys)
- [SecurityRoleKeys](#dbo-securityrolekeys)
- [SecurityRoleUsers](#dbo-securityroleusers)
- [SecurityRoles](#dbo-securityroles)
- [Services](#dbo-services)
- [SessionCmds](#dbo-sessioncmds)
- [SessionTable](#dbo-sessiontable)
- [ShipLocations](#dbo-shiplocations)
- [ShippingCosts](#dbo-shippingcosts)
- [ShippingRequests](#dbo-shippingrequests)
- [ShippingVendor](#dbo-shippingvendor)
- [States](#dbo-states)
- [StatusTable](#dbo-statustable)
- [Sulphite](#dbo-sulphite)
- [SulphiteDetail](#dbo-sulphitedetail)
- [SulphiteImport](#dbo-sulphiteimport)
- [SulphiteUsers](#dbo-sulphiteusers)
- [Suppression](#dbo-suppression)
- [TAGFILEP](#dbo-tagfilep)
- [TMAwards](#dbo-tmawards)
- [TMImport](#dbo-tmimport)
- [TMImport1](#dbo-tmimport1)
- [TMImport2](#dbo-tmimport2)
- [TMImport3](#dbo-tmimport3)
- [TMImport5](#dbo-tmimport5)
- [TMImport6](#dbo-tmimport6)
- [TMSurvey](#dbo-tmsurvey)
- [TMSurveyNewTrades](#dbo-tmsurveynewtrades)
- [TMSurveyNewVendors](#dbo-tmsurveynewvendors)
- [TMSurveyResults](#dbo-tmsurveyresults)
- [TMVendors](#dbo-tmvendors)
- [TM_UOM](#dbo-tm-uom)
- [TableOfContents](#dbo-tableofcontents)
- [TagFilePos_](#dbo-tagfilepos-)
- [TagFile_](#dbo-tagfile-)
- [TagSet_](#dbo-tagset-)
- [TaskEvent](#dbo-taskevent)
- [TaskSchedule](#dbo-taskschedule)
- [TempIrvingtonWincap](#dbo-tempirvingtonwincap)
- [TmpLog](#dbo-tmplog)
- [TmpTaskSchedule](#dbo-tmptaskschedule)
- [TopUOM](#dbo-topuom)
- [Trades](#dbo-trades)
- [TransactionLogCF](#dbo-transactionlogcf)
- [TransactionLog_HISTORY](#dbo-transactionlog-history)
- [TransactionTypes](#dbo-transactiontypes)
- [TransmitLog](#dbo-transmitlog)
- [UNSPSCs](#dbo-unspscs)
- [Units](#dbo-units)
- [UnsubscriptionEmail](#dbo-unsubscriptionemail)
- [UserAccounts](#dbo-useraccounts)
- [UserAdminLog](#dbo-useradminlog)
- [UserCategory](#dbo-usercategory)
- [UserImports](#dbo-userimports)
- [UserTrees](#dbo-usertrees)
- [Users](#dbo-users)
- [VPOLoginAttempts](#dbo-vpologinattempts)
- [VPORegistrations](#dbo-vporegistrations)
- [VPOVendorLinks](#dbo-vpovendorlinks)
- [VendorCatalogNote](#dbo-vendorcatalognote)
- [VendorCategory](#dbo-vendorcategory)
- [VendorCategoryPP](#dbo-vendorcategorypp)
- [VendorCertificates](#dbo-vendorcertificates)
- [VendorContacts](#dbo-vendorcontacts)
- [VendorDeliveryRule](#dbo-vendordeliveryrule)
- [VendorDocRequest](#dbo-vendordocrequest)
- [VendorDocRequestDetail](#dbo-vendordocrequestdetail)
- [VendorDocRequestStatus](#dbo-vendordocrequeststatus)
- [VendorLocations](#dbo-vendorlocations)
- [VendorLogoDisplays](#dbo-vendorlogodisplays)
- [VendorOrders](#dbo-vendororders)
- [VendorOverrideMessages](#dbo-vendoroverridemessages)
- [VendorPOtags](#dbo-vendorpotags)
- [VendorQuery](#dbo-vendorquery)
- [VendorQueryDetail](#dbo-vendorquerydetail)
- [VendorQueryMSRP](#dbo-vendorquerymsrp)
- [VendorQueryMSRPDetail](#dbo-vendorquerymsrpdetail)
- [VendorQueryMSRPStatus](#dbo-vendorquerymsrpstatus)
- [VendorQueryStatus](#dbo-vendorquerystatus)
- [VendorQueryTandM](#dbo-vendorquerytandm)
- [VendorQueryTandMDetail](#dbo-vendorquerytandmdetail)
- [VendorQueryTandMStatus](#dbo-vendorquerytandmstatus)
- [VendorSessions](#dbo-vendorsessions)
- [VendorUploads](#dbo-vendoruploads)
- [Vendors](#dbo-vendors)
- [WizHelpFile](#dbo-wizhelpfile)
- [YearlyTotals](#dbo-yearlytotals)
- [additems](#dbo-additems)
- [allitems](#dbo-allitems)
- [dchtest](#dbo-dchtest)
- [dtproperties](#dbo-dtproperties)
- [jSessions](#dbo-jsessions)
- [sysdiagrams](#dbo-sysdiagrams)
- [z4zbBidFix](#dbo-z4zbbidfix)
- [z4zbReqDetail](#dbo-z4zbreqdetail)

---

## Tables

### allitems {archive-allitems}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 19:42:35.343000 |
| **Modified** | 2021-11-06 19:42:35.343000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderId | int | Yes |  |  |
| 2 | ItemId | int | Yes |  |  |
| 3 | ItemCode | varchar(50) | Yes |  |  |
| 4 | Description | varchar(2311) | Yes |  |  |
| 5 | UnitCode | varchar(20) | Yes |  |  |
| 6 | VendorItemCode | varchar(50) | Yes |  |  |
| 7 | Alternate | varchar(512) | Yes |  |  |
| 8 | BidPrice | money | Yes |  |  |
| 9 | VendorId | int | Yes |  |  |
| 10 | BidItemId | int | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | CrossRefId | int | Yes |  |  |
| 13 | PricePlanId | int | Yes |  |  |
| 14 | CategoryId | int | Yes |  |  |
| 15 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 16 | ItemBidType | varchar(50) | Yes |  |  |
| 17 | TotalOrdered | int | Yes |  |  |
| 18 | TotalBid | int | Yes |  |  |
| 19 | SysId | int | No |  |  |

### Approvals {archive-approvals}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 3,517,361 |
| **Created** | 2021-11-07 10:33:51.403000 |
| **Modified** | 2021-11-07 10:33:51.403000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ApprovalId | int | No |  |  |
| 2 | ApprovalById | int | Yes |  |  |
| 3 | Level | tinyint | Yes |  |  |
| 4 | StatusId | int | Yes |  |  |
| 5 | RequisitionId | int | Yes |  |  |
| 6 | ApprovalDate | datetime | Yes |  |  |
| 7 | ApproverId | int | Yes |  |  |
| 8 | rowguid | uniqueidentifier | No |  |  |

### ApprovalsHistory {archive-approvalshistory}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 447,389 |
| **Created** | 2021-11-07 10:49:03.327000 |
| **Modified** | 2021-11-07 10:49:03.327000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ApprovalId | int | No |  |  |
| 2 | ApprovalById | int | Yes |  |  |
| 3 | Level | tinyint | Yes |  |  |
| 4 | StatusId | int | Yes |  |  |
| 5 | RequisitionId | int | Yes |  |  |
| 6 | ApprovalDate | datetime | Yes |  |  |
| 7 | ApproverId | int | Yes |  |  |
| 8 | rowguid | uniqueidentifier | No |  |  |

### Awards {archive-awards}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 143,977 |
| **Created** | 2021-11-06 18:57:07.747000 |
| **Modified** | 2021-11-06 18:57:07.747000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AwardId | int | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidId | int | Yes |  |  |
| 4 | VendorId | int | Yes |  |  |
| 5 | PricePlanId | int | Yes |  |  |
| 6 | CategoryId | int | Yes |  |  |
| 7 | BidStartDate | datetime | Yes |  |  |
| 8 | BidEndDate | datetime | Yes |  |  |
| 9 | VendorBidNumber | varchar(50) | Yes |  |  |
| 10 | Description | varchar(511) | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | DiscountRate | decimal(9,5) | Yes |  |  |
| 13 | ItemsBid | int | Yes |  |  |
| 14 | AmountBid | money | Yes |  |  |
| 15 | BidDiscountRate | decimal(9,5) | Yes |  |  |
| 16 | StateContractDiscount | decimal(9,5) | Yes |  |  |
| 17 | UseGrossPrices | int | Yes |  |  |
| 18 | BidHeaderId | int | Yes |  |  |
| 19 | DateModified | datetime | Yes |  |  |
| 20 | BidImportId | int | Yes |  |  |
| 21 | rowguid | uniqueidentifier | No |  |  |

### BatchDetail {archive-batchdetail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 4,060,286 |
| **Created** | 2021-11-06 19:48:12.303000 |
| **Modified** | 2021-11-06 19:48:12.303000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BatchDetailId | int | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BatchBookId | int | Yes |  |  |
| 4 | BatchId | int | No |  |  |
| 5 | RecordNumber | int | Yes |  |  |
| 6 | Type | char(1) | Yes |  |  |
| 7 | DistrictCode | char(2) | Yes |  |  |
| 8 | Category | char(1) | Yes |  |  |
| 9 | CometId | char(5) | Yes |  |  |
| 10 | BookAmount | char(10) | Yes |  |  |
| 11 | ItemCode | char(20) | Yes |  |  |
| 12 | Quantity | char(6) | Yes |  |  |
| 13 | OrigType | char(1) | Yes |  |  |
| 14 | OrigDistrictCode | char(2) | Yes |  |  |
| 15 | OrigCategory | char(1) | Yes |  |  |
| 16 | OrigCometCode | char(5) | Yes |  |  |
| 17 | OrigItemCode | char(15) | Yes |  |  |
| 18 | OrigQuantity | char(6) | Yes |  |  |
| 19 | ErrorField | tinyint | Yes |  |  |
| 20 | DistrictId | int | Yes |  |  |
| 21 | CategoryId | int | Yes |  |  |
| 22 | UserId | int | Yes |  |  |
| 23 | ItemId | int | Yes |  |  |
| 24 | BidPrice | money | Yes |  |  |
| 25 | Qty | int | Yes |  |  |
| 26 | Total | money | Yes |  |  |
| 27 | DetailId | int | Yes |  |  |
| 28 | SourceId | int | Yes |  |  |
| 29 | Modified | datetime | Yes |  |  |
| 30 | ModifiedBy | int | Yes |  |  |
| 31 | PackedCode | varchar(16) | Yes |  |  |
| 32 | Location | char(1) | Yes |  |  |
| 33 | OrigBookAmount | char(10) | Yes |  |  |
| 34 | BatchFileName | varchar(16) | Yes |  |  |
| 35 | BidHeaderId | int | Yes |  |  |
| 36 | PreviousCategory | char(1) | Yes |  |  |
| 37 | PackComplete | tinyint | Yes |  |  |

### BidHeaderCheckList {archive-bidheaderchecklist}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 4,521 |
| **Created** | 2021-11-06 19:53:51.320000 |
| **Modified** | 2021-11-06 19:53:51.320000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderCheckListId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidderCheckListId | int | Yes |  |  |
| 4 | DisplaySequence | int | Yes |  |  |

### BidHeaderDetail {archive-bidheaderdetail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 26,252,593 |
| **Created** | 2021-11-06 19:54:18.173000 |
| **Modified** | 2021-11-06 19:54:18.173000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDetailId | bigint | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | BidRequestItemId | int | Yes |  |  |
| 5 | Quantity | int | Yes |  |  |
| 6 | DateAdded | datetime | Yes |  |  |
| 7 | BidHeaderKey | int | Yes |  |  |

### BidHeaderDocument {archive-bidheaderdocument}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 11,787 |
| **Created** | 2021-11-06 20:19:42.700000 |
| **Modified** | 2021-11-06 20:19:42.700000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDocumentId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidDocumentId | int | Yes |  |  |
| 4 | DisplaySequence | int | Yes |  |  |

### BidHeaderDocuments {archive-bidheaderdocuments}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:21:19.420000 |
| **Modified** | 2021-11-06 20:21:19.420000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDocumentId | int | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | DocumentDate | datetime | Yes |  |  |
| 4 | DocumentTitle | varchar(255) | No |  |  |
| 5 | DocumentFile | varchar(255) | Yes |  |  |
| 6 | DocumentData | text | Yes |  |  |
| 7 | DisplaySeq | int | Yes |  |  |

### BidHeaders {archive-bidheaders}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 3,395 |
| **Created** | 2021-11-06 18:44:02.383000 |
| **Modified** | 2021-11-06 19:47:05.487000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderId | int | Yes |  |  |
| 2 | BidDate | datetime | Yes |  |  |
| 3 | BidAwardDate | datetime | Yes |  |  |
| 4 | EffectiveUntil | datetime | Yes |  |  |

### BidImports {archive-bidimports}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 42,011 |
| **Created** | 2021-11-06 20:21:29.380000 |
| **Modified** | 2024-06-21 21:34:15.083000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidImportId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | VendorId | int | Yes |  |  |
| 5 | BidItemDiscountRate | decimal(9,5) | Yes |  |  |
| 6 | CatalogId | int | Yes |  |  |
| 7 | CatalogDiscountRate | decimal(9,5) | Yes |  |  |
| 8 | VendorBidNumber | varchar(50) | Yes |  |  |
| 9 | ItemsBid | int | Yes |  |  |
| 10 | AmountBid | money | Yes |  |  |
| 11 | MinimumOrder | money | Yes |  |  |
| 12 | FreeDeliveryMinimum | money | Yes |  |  |
| 13 | Status | varchar(50) | Yes |  |  |
| 14 | Comments | varchar(1024) | Yes |  |  |
| 15 | DateModified | datetime | Yes |  |  |
| 16 | StateContractDiscount | decimal(9,5) | Yes |  |  |
| 17 | AdditionalHandlingAmount | money | Yes |  |  |
| 18 | FreeHandlingAmount | money | Yes |  |  |
| 19 | FreeHandlingStart | datetime | Yes |  |  |
| 20 | FreeHandlingEnd | datetime | Yes |  |  |
| 21 | UseVendorContactInfo | tinyint | Yes |  |  |
| 22 | ContactEmail | varchar(255) | Yes |  |  |
| 23 | ContactName | varchar(50) | Yes |  |  |
| 24 | ContactPhone | varchar(20) | Yes |  |  |
| 25 | ContactFax | varchar(20) | Yes |  |  |
| 26 | POVendorContactId | int | Yes |  |  |
| 27 | VendorBidId | int | Yes |  |  |
| 28 | BidVendorContactId | int | Yes |  |  |
| 29 | WebsiteLink | varchar(255) | Yes |  |  |
| 30 | CatalogDiscountComments | varchar(512) | Yes |  |  |
| 31 | BidHeaderKey | int | Yes |  |  |

### BidMappedItems {archive-bidmappeditems}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:22:11 |
| **Modified** | 2021-11-06 20:22:11 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMappedItemId | uniqueidentifier | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | OrigItemId | int | No |  |  |
| 4 | NewItemId | int | No |  |  |
| 5 | ReasonCode | varchar(20) | Yes |  |  |
| 6 | MapDate | datetime | No |  |  |

### BidMSRPResults {archive-bidmsrpresults}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 10,848 |
| **Created** | 2021-11-06 20:22:11.033000 |
| **Modified** | 2021-11-06 20:22:11.033000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMSRPResultsId | int | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidHeaderId | int | No |  |  |
| 4 | BidImportId | int | No |  |  |
| 5 | ManufacturerId | int | Yes |  |  |
| 6 | DiscountRate | decimal(9,5) | Yes |  |  |
| 7 | Modified | datetime | No |  |  |
| 8 | DiscountRateString | char(10) | Yes |  |  |
| 9 | WriteInFlag | tinyint | Yes |  |  |
| 10 | WriteInManufacturer | varchar(100) | Yes |  |  |
| 11 | VendorNotes | varchar(1000) | Yes |  |  |
| 12 | BidRequestManufacturerId | int | Yes |  |  |
| 13 | WinningBidOverride | tinyint | Yes |  |  |
| 14 | PriceListTypeId | int | Yes |  |  |
| 15 | AuthorizationLetter | tinyint | Yes |  |  |
| 16 | SubmittedExcel | tinyint | Yes |  |  |
| 17 | ProductCatalog | tinyint | Yes |  |  |
| 18 | TotalAward | tinyint | Yes |  |  |
| 19 | VendorPriceFile | tinyint | Yes |  |  |
| 20 | TotalAwardDiscount | decimal(9,5) | Yes |  |  |
| 21 | TotalAwardString | varchar(20) | Yes |  |  |
| 22 | ExcelFileApproved | tinyint | Yes |  |  |
| 23 | BidHeaderKey | int | Yes |  |  |

### BidReawards {archive-bidreawards}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:22:11.387000 |
| **Modified** | 2021-11-06 20:22:11.387000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidReawardId | int | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ReawardDate | datetime | No |  |  |
| 4 | EffectiveFrom | datetime | No |  |  |
| 5 | EffectiveUntil | datetime | No |  |  |
| 6 | Comments | varchar(4096) | Yes |  |  |

### BidRequestItems {archive-bidrequestitems}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 5,704,577 |
| **Created** | 2021-11-06 20:22:11.407000 |
| **Modified** | 2021-11-06 20:22:11.407000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestItemId | int | No |  |  |
| 2 | BidRequestItemId_OLD | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | BidRequest | int | Yes |  |  |
| 6 | Active | tinyint | Yes |  |  |
| 7 | RequisitionCount | int | Yes |  |  |
| 8 | Status | varchar(50) | Yes |  |  |
| 9 | Comments | varchar(1024) | Yes |  |  |
| 10 | BidRequestAmount | money | Yes |  |  |
| 11 | Checksum | int | Yes |  |  |
| 12 | MasterItemCodePtr | int | Yes |  |  |
| 13 | BidHeaderKey | int | Yes |  |  |
| 14 | ImageURL | varchar(300) | Yes |  |  |
| 15 | SDS_URL | varchar(300) | Yes |  |  |

### BidRequestManufacturer {archive-bidrequestmanufacturer}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:26:55.360000 |
| **Modified** | 2021-11-06 20:26:55.360000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestManufacturerId | int | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | ManufacturerId | int | Yes |  |  |
| 5 | SequenceNumber | int | Yes |  |  |
| 6 | AllowAdditionalProductLines | tinyint | Yes |  |  |
| 7 | UseOptions | tinyint | Yes |  |  |
| 8 | BidHeaderKey | int | Yes |  |  |

### BidRequestOptions {archive-bidrequestoptions}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:26:55.763000 |
| **Modified** | 2021-11-06 20:26:55.763000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestOptionId | int | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ManufacturerId | int | Yes |  |  |
| 4 | ManufacturerProductLineId | int | Yes |  |  |
| 5 | OptionId | int | Yes |  |  |
| 6 | BidRequestManufacturerId | int | Yes |  |  |
| 7 | BidRequestProductLineId | int | Yes |  |  |
| 8 | Name | varchar(50) | No |  |  |
| 9 | Weight | decimal(9,5) | Yes |  |  |

### BidRequestPriceRanges {archive-bidrequestpriceranges}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:26:56.170000 |
| **Modified** | 2021-11-06 20:26:56.170000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestPriceRangeId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidRequestManufacturerId | int | Yes |  |  |
| 4 | BidRequestProductLineId | int | Yes |  |  |
| 5 | RangeBase | money | Yes |  |  |
| 6 | RangeWeight | decimal(9,5) | Yes |  |  |
| 7 | BidRequestMSRPOptionId | int | Yes |  |  |

### BidResults {archive-bidresults}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 30,585,282 |
| **Created** | 2021-11-06 20:26:56.303000 |
| **Modified** | 2021-11-06 20:26:56.303000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidResultsId | int | No |  |  |
| 2 | BidImportId | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | BidRequestItemId | int | Yes |  |  |
| 5 | CategoryId | int | Yes |  |  |
| 6 | DistrictId | int | Yes |  |  |
| 7 | ItemId | int | Yes |  |  |
| 8 | ItemCode | varchar(50) | Yes |  |  |
| 9 | Units | varchar(16) | Yes |  |  |
| 10 | Alternate | varchar(512) | Yes |  |  |
| 11 | Quantity | int | Yes |  |  |
| 12 | ItemBidType | char(1) | Yes |  |  |
| 13 | UnitPrice | money | Yes |  |  |
| 14 | Cost | money | Yes |  |  |
| 15 | VendorItemCode | varchar(50) | Yes |  |  |
| 16 | QuantityBid | int | Yes |  |  |
| 17 | ItemsPerUnit | varchar(50) | Yes |  |  |
| 18 | UnitId | int | Yes |  |  |
| 19 | Status | varchar(51) | Yes |  |  |
| 20 | Comments | varchar(1024) | Yes |  |  |
| 21 | Active | int | Yes |  |  |
| 22 | PageNo | int | Yes |  |  |
| 23 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 24 | ModifiedDate | datetime | Yes |  |  |
| 25 | ModifiedSessionId | int | Yes |  |  |
| 26 | ModifiedBy | int | Yes |  |  |
| 27 | RTK_MSDSId | int | Yes |  |  |
| 28 | RTK_MSDSNotNeeded | tinyint | Yes |  |  |
| 29 | ContractNumber | varchar(50) | Yes |  |  |
| 30 | OriginalAwardedItem | tinyint | Yes |  |  |
| 31 | VOMId | int | Yes |  |  |
| 32 | AdditionalShipping | tinyint | Yes |  |  |
| 33 | ManufacturerBid | varchar(50) | Yes |  |  |
| 34 | ManufPartNoBid | varchar(50) | Yes |  |  |
| 35 | LinerGaugeMicrons | numeric(2,0) | Yes |  |  |
| 36 | LinerGaugeMil | numeric(3,2) | Yes |  |  |
| 37 | LinerCaseWeight | numeric(4,2) | Yes |  |  |
| 38 | LinerDimWidth | numeric(4,2) | Yes |  |  |
| 39 | LinerDimDepth | numeric(4,2) | Yes |  |  |
| 40 | LinerDimLength | numeric(4,2) | Yes |  |  |
| 41 | PackedManufPartNoBid | varchar(50) | Yes |  |  |
| 42 | BidHeaderKey | int | Yes |  |  |
| 43 | SDS_URL | varchar(300) | Yes |  |  |
| 44 | ImageURL | varchar(300) | Yes |  |  |
| 45 | UPC_ISBN | varchar(20) | Yes |  |  |
| 46 | UNSPSC | varchar(50) | Yes |  |  |

### Bids {archive-bids}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 172,256 |
| **Created** | 2021-11-06 20:39:55.477000 |
| **Modified** | 2021-11-06 20:39:55.477000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidId | int | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CoopId | int | Yes |  |  |
| 4 | ClosingDate | datetime | Yes |  |  |
| 5 | OpeningDate | datetime | Yes |  |  |
| 6 | EffectiveFrom | datetime | Yes |  |  |
| 7 | EffectiveUntil | datetime | Yes |  |  |
| 8 | Name | varchar(255) | Yes |  |  |
| 9 | PricePlanId | int | Yes |  |  |
| 10 | CategoryId | int | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | BidDiscountRate | decimal(8,5) | Yes |  |  |
| 13 | VendorBidNumber | varchar(50) | Yes |  |  |
| 14 | DistrictId | int | Yes |  |  |
| 15 | ItemsBid | int | Yes |  |  |
| 16 | AmountBid | money | Yes |  |  |
| 17 | CatalogId | int | Yes |  |  |
| 18 | Description | varchar(511) | Yes |  |  |
| 19 | BidHeaderId | int | Yes |  |  |
| 20 | UseGrossPrices | int | Yes |  |  |
| 21 | BidImportId | int | Yes |  |  |
| 22 | DateModified | datetime | Yes |  |  |
| 23 | AdditionalHandlingAmount | money | Yes |  |  |
| 24 | FreeHandlingAmount | money | Yes |  |  |
| 25 | FreeHandlingStart | datetime | Yes |  |  |
| 26 | FreeHandlingEnd | datetime | Yes |  |  |
| 27 | WebsiteLink | varchar(255) | Yes |  |  |

### BidTrades {archive-bidtrades}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 119 |
| **Created** | 2021-11-06 20:40:13.490000 |
| **Modified** | 2021-11-08 20:59:36.747000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidTradeId | int | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | TradeId | int | No |  |  |
| 4 | Title | varchar(255) | No |  |  |
| 5 | Specifications | varchar(MAX) | No |  |  |

### Catalog {archive-catalog}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 2,422 |
| **Created** | 2021-11-07 10:54:25.180000 |
| **Modified** | 2021-11-08 20:59:36.953000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogId | int IDENTITY | No |  |  |

### cxmlSession {archive-cxmlsession}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 50,022 |
| **Created** | 2022-12-16 23:40:40.747000 |
| **Modified** | 2022-12-16 23:40:40.747000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SessionId | int | No |  |  |
| 2 | payloadId | varchar(255) | Yes |  |  |
| 3 | buyerCookie | varchar(255) | Yes |  |  |
| 4 | BrowserFormPost | varchar(255) | Yes |  |  |
| 5 | fromDomain | varchar(255) | Yes |  |  |
| 6 | fromIdentity | varchar(255) | Yes |  |  |
| 7 | toDomain | varchar(255) | Yes |  |  |
| 8 | toIdentity | varchar(255) | Yes |  |  |
| 9 | senderDomain | varchar(255) | Yes |  |  |
| 10 | senderIdentity | varchar(255) | Yes |  |  |
| 11 | fromUserAgent | varchar(255) | Yes |  |  |
| 12 | OrigReqId | int | Yes |  |  |
| 13 | RequisitionId | int | Yes |  |  |
| 14 | CategoryId | int | Yes |  |  |
| 15 | Mode | int | Yes |  |  |
| 16 | BudgetAccountId | int | Yes |  |  |
| 17 | UserAccountId | int | Yes |  |  |
| 18 | AccountCode | varchar(50) | Yes |  |  |
| 19 | BudgetId | int | Yes |  |  |
| 20 | UniqueId | uniqueidentifier | Yes |  |  |

### Detail {archive-detail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 25,480,018 |
| **Created** | 2021-11-07 01:29:08.650000 |
| **Modified** | 2021-11-07 01:29:08.650000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailId | int | No |  |  |
| 2 | RequisitionId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | AddendumItem | tinyint | Yes |  |  |
| 6 | ItemCode | varchar(50) | Yes |  |  |
| 7 | Quantity | int | Yes |  |  |
| 8 | LastYearsQuantity | int | Yes |  |  |
| 9 | Description | varchar(1024) | Yes |  |  |
| 10 | UnitId | int | Yes |  |  |
| 11 | UnitCode | varchar(20) | Yes |  |  |
| 12 | BidPrice | money | Yes |  |  |
| 13 | CatalogPrice | money | Yes |  |  |
| 14 | GrossPrice | money | Yes |  |  |
| 15 | DiscountRate | decimal(9,5) | Yes |  |  |
| 16 | CatalogPage | char(4) | Yes |  |  |
| 17 | PricePlanId | int | Yes |  |  |
| 18 | PriceId | int | Yes |  |  |
| 19 | AwardId | int | Yes |  |  |
| 20 | VendorId | int | Yes |  |  |
| 21 | VendorItemCode | varchar(50) | Yes |  |  |
| 22 | Alternate | varchar(1024) | Yes |  |  |
| 23 | POId | int | Yes |  |  |
| 24 | BatchDetailId | int | Yes |  |  |
| 25 | Modified | datetime | Yes |  |  |
| 26 | ModifiedById | int | Yes |  |  |
| 27 | SourceId | int | Yes |  |  |
| 28 | SortSeq | varchar(64) | Yes |  |  |
| 29 | BidItemId | int | Yes |  |  |
| 30 | ExtraDescription | varchar(1024) | Yes |  |  |
| 31 | ReProc | tinyint | Yes |  |  |
| 32 | UseGrossPrices | tinyint | Yes |  |  |
| 33 | BidHeaderId | int | Yes |  |  |
| 34 | DistrictRequisitionNumber | varchar(50) | Yes |  |  |
| 35 | HeadingTitle | varchar(255) | Yes |  |  |
| 36 | Keyword | varchar(50) | Yes |  |  |
| 37 | SectionId | int | Yes |  |  |
| 38 | SectionName | varchar(255) | Yes |  |  |
| 39 | OriginalItemId | int | Yes |  |  |
| 40 | HeadingId | int | Yes |  |  |
| 41 | KeywordId | int | Yes |  |  |
| 42 | ItemMustBeBid | int | Yes |  |  |
| 43 | SessionId | int | Yes |  |  |
| 44 | Active | tinyint | Yes |  |  |
| 45 | RTK_MSDSId | int | Yes |  |  |
| 46 | AddedFromAddenda | datetime | Yes |  |  |
| 47 | LastAlteredSessionId | int | Yes |  |  |
| 48 | AdditionalShipping | tinyint | Yes |  |  |
| 49 | CrossRefId | int | Yes |  |  |
| 50 | ShippingCost | decimal(9,2) | Yes |  |  |
| 51 | ShippingQuantity | int | Yes |  |  |
| 52 | ShippingUpdated | datetime | Yes |  |  |

### DetailHold {archive-detailhold}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:13.797000 |
| **Modified** | 2021-11-06 20:40:13.797000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailId | int | No |  |  |
| 2 | RequisitionId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | AddendumItem | tinyint | Yes |  |  |
| 6 | ItemCode | varchar(50) | Yes |  |  |
| 7 | Quantity | int | Yes |  |  |
| 8 | LastYearsQuantity | int | Yes |  |  |
| 9 | Description | varchar(1024) | Yes |  |  |
| 10 | UnitId | int | Yes |  |  |
| 11 | UnitCode | varchar(20) | Yes |  |  |
| 12 | BidPrice | money | Yes |  |  |
| 13 | CatalogPrice | money | Yes |  |  |
| 14 | GrossPrice | money | Yes |  |  |
| 15 | DiscountRate | decimal(9,5) | Yes |  |  |
| 16 | CatalogPage | char(4) | Yes |  |  |
| 17 | PricePlanId | int | Yes |  |  |
| 18 | PriceId | int | Yes |  |  |
| 19 | AwardId | int | Yes |  |  |
| 20 | VendorId | int | Yes |  |  |
| 21 | VendorItemCode | varchar(50) | Yes |  |  |
| 22 | Alternate | varchar(1024) | Yes |  |  |
| 23 | POId | int | Yes |  |  |
| 24 | BatchDetailId | int | Yes |  |  |
| 25 | Modified | datetime | Yes |  |  |
| 26 | ModifiedById | int | Yes |  |  |
| 27 | SourceId | int | Yes |  |  |
| 28 | SortSeq | varchar(64) | Yes |  |  |
| 29 | BidItemId | int | Yes |  |  |
| 30 | ExtraDescription | varchar(1024) | Yes |  |  |
| 31 | ReProc | tinyint | Yes |  |  |
| 32 | UseGrossPrices | tinyint | Yes |  |  |
| 33 | BidHeaderId | int | Yes |  |  |
| 34 | DistrictRequisitionNumber | varchar(50) | Yes |  |  |
| 35 | HeadingTitle | varchar(255) | Yes |  |  |
| 36 | Keyword | varchar(50) | Yes |  |  |
| 37 | SectionId | int | Yes |  |  |
| 38 | SectionName | varchar(255) | Yes |  |  |
| 39 | OriginalItemId | int | Yes |  |  |
| 40 | HeadingId | int | Yes |  |  |
| 41 | KeywordId | int | Yes |  |  |
| 42 | ItemMustBeBid | int | Yes |  |  |
| 43 | SessionId | int | Yes |  |  |
| 44 | Active | tinyint | Yes |  |  |
| 45 | RTK_MSDSId | int | Yes |  |  |

### DetailMatch {archive-detailmatch}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 1,499 |
| **Created** | 2021-11-06 20:40:13.800000 |
| **Modified** | 2021-11-06 20:40:13.800000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BudgetId | int | Yes |  |  |
| 2 | TotalRequisitionCost | money | Yes |  |  |
| 3 | DetailId | int | No |  |  |
| 4 | RequisitionId | int | Yes |  |  |
| 5 | CatalogId | int | Yes |  |  |
| 6 | ItemId | int | Yes |  |  |
| 7 | AddendumItem | tinyint | Yes |  |  |
| 8 | ItemCode | varchar(50) | Yes |  |  |
| 9 | Quantity | int | Yes |  |  |
| 10 | LastYearsQuantity | int | Yes |  |  |
| 11 | Description | varchar(1024) | Yes |  |  |
| 12 | UnitId | int | Yes |  |  |
| 13 | UnitCode | varchar(20) | Yes |  |  |
| 14 | BidPrice | money | Yes |  |  |
| 15 | CatalogPrice | money | Yes |  |  |
| 16 | GrossPrice | money | Yes |  |  |
| 17 | DiscountRate | decimal(9,5) | Yes |  |  |
| 18 | CatalogPage | char(4) | Yes |  |  |
| 19 | PricePlanId | int | Yes |  |  |
| 20 | PriceId | int | Yes |  |  |
| 21 | AwardId | int | Yes |  |  |
| 22 | VendorId | int | Yes |  |  |
| 23 | VendorItemCode | varchar(50) | Yes |  |  |
| 24 | Alternate | varchar(1024) | Yes |  |  |
| 25 | POId | int | Yes |  |  |
| 26 | BatchDetailId | int | Yes |  |  |
| 27 | Modified | datetime | Yes |  |  |
| 28 | ModifiedById | int | Yes |  |  |
| 29 | SourceId | int | Yes |  |  |
| 30 | SortSeq | varchar(64) | Yes |  |  |
| 31 | BidItemId | int | Yes |  |  |
| 32 | ExtraDescription | varchar(1024) | Yes |  |  |
| 33 | ReProc | tinyint | Yes |  |  |
| 34 | UseGrossPrices | tinyint | Yes |  |  |
| 35 | BidHeaderId | int | Yes |  |  |
| 36 | DistrictRequisitionNumber | varchar(50) | Yes |  |  |
| 37 | HeadingTitle | varchar(255) | Yes |  |  |
| 38 | Keyword | varchar(50) | Yes |  |  |
| 39 | SectionId | int | Yes |  |  |
| 40 | SectionName | varchar(255) | Yes |  |  |
| 41 | OriginalItemId | int | Yes |  |  |
| 42 | HeadingId | int | Yes |  |  |
| 43 | KeywordId | int | Yes |  |  |
| 44 | ItemMustBeBid | int | Yes |  |  |
| 45 | SessionId | int | Yes |  |  |
| 46 | Active | tinyint | Yes |  |  |
| 47 | RTK_MSDSId | int | Yes |  |  |
| 48 | AddedFromAddenda | datetime | Yes |  |  |
| 49 | LastAlteredSessionId | int | Yes |  |  |

### DMSBidDocuments {archive-dmsbiddocuments}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:14.937000 |
| **Modified** | 2021-11-06 20:40:14.937000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidNbr | varchar(MAX) | Yes |  |  |
| 4 | DocType | varchar(MAX) | Yes |  |  |
| 5 | DocId | uniqueidentifier | Yes |  |  |
| 6 | DistrictVisible | varchar(MAX) | Yes |  |  |
| 7 | PagesCaptured | int | Yes |  |  |
| 8 | FileName | varchar(1024) | Yes |  |  |

### DMSVendorBidDocuments {archive-dmsvendorbiddocuments}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.023000 |
| **Modified** | 2021-11-06 20:40:15.023000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No |  |  |
| 2 | VendorCode | varchar(10) | Yes |  |  |
| 3 | DistrictVisible | varchar(10) | Yes |  |  |
| 4 | BidHeaderId | int | Yes |  |  |
| 5 | BidNbr | varchar(20) | Yes |  |  |
| 6 | DocType | varchar(255) | Yes |  |  |
| 7 | ExpirationDate | varchar(30) | Yes |  |  |
| 8 | DocumentNumber | varchar(255) | Yes |  |  |
| 9 | DocId | uniqueidentifier | Yes |  |  |
| 10 | PagesCaptured | int | Yes |  |  |
| 11 | FileName | varchar(1024) | Yes |  |  |

### FreezeItems {archive-freezeitems}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.107000 |
| **Modified** | 2021-11-06 20:40:15.107000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No |  |  |
| 2 | ItemId | int | No |  |  |
| 3 | CrossRefId | int | No |  |  |
| 4 | VendorId | int | No |  |  |
| 5 | VendorItemCode | varchar(50) | Yes |  |  |
| 6 | BidHeaderId | int | No |  |  |
| 7 | GrossPrice | money | Yes |  |  |

### ItemContractPrices {archive-itemcontractprices}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.150000 |
| **Modified** | 2021-11-06 20:40:15.150000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ICPId | int | No |  |  |
| 2 | ItemId | int | No |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | CrossRefId | int | Yes |  |  |
| 5 | Price | money | Yes |  |  |

### OrderBooks {archive-orderbooks}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 692 |
| **Created** | 2021-11-06 20:40:15.153000 |
| **Modified** | 2021-11-06 20:40:15.153000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OrderBookId | int | No |  |  |
| 2 | PricePlanDescription | varchar(255) | Yes |  |  |
| 3 | Category | varchar(255) | Yes |  |  |
| 4 | CategoryId | int | Yes |  |  |
| 5 | PricePlanId | int | Yes |  |  |
| 6 | AwardId | int | Yes |  |  |
| 7 | Type | char(1) | Yes |  |  |
| 8 | DistrictId | int | Yes |  |  |
| 9 | Markup | decimal(9,5) | Yes |  |  |
| 10 | BidHeaderId | int | Yes |  |  |
| 11 | OrderBookYear | int | Yes |  |  |
| 12 | OrderBookCreated | datetime | Yes |  |  |
| 13 | Active | int | Yes |  |  |
| 14 | MasterBook | int | Yes |  |  |
| 15 | MasterLetter | char(1) | Yes |  |  |
| 16 | UseParentCatalog | int | Yes |  |  |
| 17 | KeepZeroPages | int | Yes |  |  |

### PO {archive-po}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 1,300,617 |
| **Created** | 2021-11-07 01:14:00.410000 |
| **Modified** | 2021-11-07 01:14:00.410000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POId | int | No |  |  |
| 2 | RequisitionId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | PONumber | varchar(24) | Yes |  |  |
| 5 | PODate | datetime | Yes |  |  |
| 6 | DatePrinted | datetime | Yes |  |  |
| 7 | DatePrintedDetail | datetime | Yes |  |  |
| 8 | DateExported | datetime | Yes |  |  |
| 9 | DateOrdered | datetime | Yes |  |  |
| 10 | DateReceived | datetime | Yes |  |  |
| 11 | Amount | money | Yes |  |  |
| 12 | ItemCount | int | Yes |  |  |
| 13 | AwardId | int | Yes |  |  |
| 14 | DiscountAmount | money | Yes |  |  |
| 15 | TotalGross | money | Yes |  |  |
| 16 | DiscountRate | decimal(9,5) | Yes |  |  |
| 17 | ShippingAmount | money | Yes |  |  |
| 18 | ExportedToVendor | datetime | Yes |  |  |
| 19 | UploadId | int | Yes |  |  |
| 20 | Cancelled | tinyint | Yes |  |  |
| 21 | POStatusID | int | Yes |  |  |
| 22 | rowguid | uniqueidentifier | No |  |  |

### PODetailItems {archive-podetailitems}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 22,905,929 |
| **Created** | 2021-11-06 21:37:16.417000 |
| **Modified** | 2021-11-06 21:37:16.417000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PODetailItemId | int IDENTITY | No |  |  |
| 2 | POId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | Quantity | int | Yes |  |  |
| 6 | BidItemId | int | Yes |  |  |
| 7 | BidPrice | money | Yes |  |  |
| 8 | GrossPrice | money | Yes |  |  |
| 9 | DiscountRate | decimal(9,5) | Yes |  |  |
| 10 | AwardId | int | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | VendorItemCode | varchar(50) | Yes |  |  |
| 13 | Alternate | varchar(1024) | Yes |  |  |
| 14 | ContractNumber | varchar(50) | Yes |  |  |
| 15 | rowguid | uniqueidentifier | No |  |  |

### POTempDetails {archive-potempdetails}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.187000 |
| **Modified** | 2021-11-06 20:40:15.187000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POTempDetailID | int | No |  |  |
| 2 | POTempID | int | Yes |  |  |
| 3 | RequisitionID | int | No |  |  |
| 4 | VendorID | int | No |  |  |
| 5 | BidHeaderID | int | No |  |  |
| 6 | PONumber | varchar(50) | Yes |  |  |
| 7 | POPrefix | varchar(50) | Yes |  |  |
| 8 | POSuffix | varchar(50) | Yes |  |  |

### Prices {archive-prices}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.220000 |
| **Modified** | 2021-11-06 20:40:15.220000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemId | int | No |  |  |
| 2 | PackedCode | varchar(50) | Yes |  |  |
| 3 | CrossRefId | int | Yes |  |  |
| 4 | CrossRefIdBid | int | Yes |  |  |
| 5 | BidPrice | decimal(34,13) | Yes |  |  |
| 6 | GrossPrice | money | Yes |  |  |
| 7 | CatalogPrice | money | Yes |  |  |
| 8 | AwardId | int | No |  |  |
| 9 | VendorId | int | No |  |  |
| 10 | PricePlanId | int | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | VendorItemCode | varchar(50) | Yes |  |  |
| 13 | ParentCatalogId | int | Yes |  |  |
| 14 | ItemCode | varchar(50) | Yes |  |  |
| 15 | Description | varchar(1024) | Yes |  |  |
| 16 | UnitId | int | Yes |  |  |
| 17 | UnitCode | varchar(20) | Yes |  |  |
| 18 | PriceId | uniqueidentifier | No |  |  |
| 19 | Page | char(4) | Yes |  |  |
| 20 | DiscountRate | decimal(9,5) | Yes |  |  |
| 21 | Name | varchar(50) | Yes |  |  |
| 22 | VendorName | varchar(50) | Yes |  |  |
| 23 | CategoryId | int | Yes |  |  |
| 24 | PackedItemCode | varchar(50) | Yes |  |  |
| 25 | BidItemId | int | Yes |  |  |
| 26 | Alternate | varchar(1024) | Yes |  |  |
| 27 | PackedVendorItemCode | varchar(255) | Yes |  |  |
| 28 | CatalogYear | char(2) | Yes |  |  |
| 29 | RedirectedItemId | int | Yes |  |  |
| 30 | BidHeaderId | int | Yes |  |  |

### PricingConsolidatedOrderCounts {archive-pricingconsolidatedordercounts}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.223000 |
| **Modified** | 2021-11-06 20:40:15.223000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PCOCId | bigint | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ItemId | int | No |  |  |
| 4 | OrderCount | int | No |  |  |

### PricingMap {archive-pricingmap}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.253000 |
| **Modified** | 2021-11-06 20:40:15.253000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ItemId | int | No |  |  |
| 4 | MappedItemId | int | No |  |  |
| 5 | ItemCode | varchar(50) | Yes |  |  |
| 6 | PackedItemCode | varchar(50) | Yes |  |  |
| 7 | BidPrice | money | No |  |  |
| 8 | CatalogPrice | money | No |  |  |
| 9 | BidItemId | int | Yes |  |  |
| 10 | VendorId | int | No |  |  |
| 11 | VendorItemCode | varchar(50) | Yes |  |  |
| 12 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 13 | ManufacturerPartNumber | varchar(50) | Yes |  |  |
| 14 | PackedManufacturerPartNumber | varchar(50) | Yes |  |  |
| 15 | UnitId | int | No |  |  |
| 16 | UnitCode | varchar(16) | No |  |  |
| 17 | Alternate | varchar(512) | Yes |  |  |
| 18 | ItemDescription | varchar(1024) | Yes |  |  |
| 19 | SortSeq | varchar(64) | Yes |  |  |

### PricingUpdate {archive-pricingupdate}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.260000 |
| **Modified** | 2021-11-06 20:40:15.260000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PricingUpdateId | int | No |  |  |
| 2 | BidHeaderId | int | No |  |  |
| 3 | LastUpdated | datetime | Yes |  |  |

### RequisitionChangeLog {archive-requisitionchangelog}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 1,936,897 |
| **Created** | 2022-12-16 23:40:36.880000 |
| **Modified** | 2022-12-16 23:40:36.880000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionChangeId | int IDENTITY | No |  |  |
| 2 | RequisitionId | int | No |  |  |
| 3 | OrigSchoolId | int | Yes |  |  |
| 4 | OrigUserId | int | Yes |  |  |
| 5 | OrigBudgetId | int | Yes |  |  |
| 6 | OrigBudgetAccountId | int | Yes |  |  |
| 7 | OrigUserAccountId | int | Yes |  |  |
| 8 | OrigCategoryId | int | Yes |  |  |
| 9 | OrigShippingId | int | Yes |  |  |
| 10 | OrigAttention | varchar(50) | Yes |  |  |
| 11 | OrigAccountCode | varchar(50) | Yes |  |  |
| 12 | OrigBidHeaderId | int | Yes |  |  |
| 13 | NewSchoolId | int | Yes |  |  |
| 14 | NewUserId | int | Yes |  |  |
| 15 | NewBudgetId | int | Yes |  |  |
| 16 | NewBudgetAccountId | int | Yes |  |  |
| 17 | NewUserAccountId | int | Yes |  |  |
| 18 | NewCategoryId | int | Yes |  |  |
| 19 | NewShippingId | int | Yes |  |  |
| 20 | NewAttention | varchar(50) | Yes |  |  |
| 21 | NewAccountCode | varchar(50) | Yes |  |  |
| 22 | NewBidHeaderId | int | Yes |  |  |
| 23 | UserId | int | Yes |  |  |
| 24 | SessionId | int | Yes |  |  |
| 25 | ChangeDate | datetime | Yes |  |  |

### Requisitions {archive-requisitions}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 1,433,904 |
| **Created** | 2022-12-16 23:40:13.307000 |
| **Modified** | 2022-12-16 23:40:13.307000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionId | int IDENTITY | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | RequisitionNumber | varchar(24) | Yes |  |  |
| 4 | SchoolId | int | Yes |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | BudgetId | int | Yes |  |  |
| 7 | BudgetAccountId | int | Yes |  |  |
| 8 | UserAccountId | int | Yes |  |  |
| 9 | CategoryId | int | Yes |  |  |
| 10 | ShippingId | int | Yes |  |  |
| 11 | Attention | varchar(50) | Yes |  |  |
| 12 | AccountCode | varchar(50) | Yes |  |  |
| 13 | DateEntered | datetime | Yes |  |  |
| 14 | ShippingPercent | decimal(9,5) | Yes |  |  |
| 15 | DiscountPercent | decimal(9,5) | Yes |  |  |
| 16 | ShippingCost | money | Yes |  |  |
| 17 | TotalItemsCost | money | Yes |  |  |
| 18 | TotalRequisitionCost | money | Yes |  |  |
| 19 | Comments | varchar(1023) | Yes |  |  |
| 20 | ApprovalRequired | tinyint | Yes |  |  |
| 21 | ApprovalId | int | Yes |  |  |
| 22 | ApprovalLevel | tinyint | Yes |  |  |
| 23 | StatusId | int | Yes |  |  |
| 24 | OrderDate | datetime | Yes |  |  |
| 25 | DateExported | datetime | Yes |  |  |
| 26 | BidId | int | Yes |  |  |
| 27 | BookId | int | Yes |  |  |
| 28 | SourceId | int | Yes |  |  |
| 29 | BidHeaderId | int | Yes |  |  |
| 30 | LastAlteredSessionId | int | Yes |  |  |
| 31 | DateUpdated | datetime | Yes |  |  |
| 32 | OrderType | tinyint | Yes |  |  |
| 33 | NotesCount | int | Yes |  |  |
| 34 | AddendaTotal | money | Yes |  |  |
| 35 | ApprovalCount | int | Yes |  |  |
| 36 | AdditionalFreight | tinyint | Yes |  |  |
| 37 | HistoryCount | int | Yes |  |  |
| 38 | POCount | int | Yes |  |  |
| 39 | LowPOCount | int | Yes |  |  |
| 40 | AdditionalShippingCost | money | Yes |  |  |

### TMAwards {archive-tmawards}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 29,335 |
| **Created** | 2021-11-06 20:40:15.397000 |
| **Modified** | 2021-11-06 20:40:15.397000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMAwardId | int | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidHeaderId | int | No |  |  |
| 4 | BidTradeCountyId | int | No |  |  |
| 5 | BidImportId | int | Yes |  |  |
| 6 | VendorId | int | Yes |  |  |
| 7 | AwardType | varchar(50) | Yes |  |  |
| 8 | DateModified | datetime | Yes |  |  |
| 9 | AwardAmount | money | Yes |  |  |

### UserAccounts {archive-useraccounts}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 2,704,140 |
| **Created** | 2022-12-16 23:40:09.187000 |
| **Modified** | 2022-12-16 23:40:09.187000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UserAccountId | int IDENTITY | No |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | AccountId | int | Yes |  |  |
| 4 | BudgetId | int | Yes |  |  |
| 5 | BudgetAccountId | int | Yes |  |  |
| 6 | UserId | int | Yes |  |  |
| 7 | AllocationAmount | money | Yes |  |  |
| 8 | AllocationAvailable | money | Yes |  |  |
| 9 | UseAllocations | tinyint | Yes |  |  |

### UserAccountsUserAccountId_CrossMapping {archive-useraccountsuseraccountid-crossmapping}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 2,704,140 |
| **Created** | 2022-12-16 23:40:45.687000 |
| **Modified** | 2022-12-16 23:40:45.687000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | New_UserAccountId | int IDENTITY | No |  |  |
| 2 | Old_UserAccountId | int | Yes |  |  |

### VendorDocRequest {archive-vendordocrequest}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.737000 |
| **Modified** | 2024-06-21 22:40:42.400000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorDocRequestId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorDocRequestNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorDocRequestDetail {archive-vendordocrequestdetail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:15.740000 |
| **Modified** | 2021-11-06 20:40:15.740000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorDocRequestDetailId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidImportId | int | Yes |  |  |
| 4 | BidHeaderCheckListId | int | Yes |  |  |
| 5 | VendorDocRequestId | int | Yes |  |  |
| 6 | AddDate | datetime | Yes |  |  |
| 7 | SendDate | datetime | Yes |  |  |
| 8 | CommentsRejectReason | varchar(1024) | Yes |  |  |
| 9 | VendorId | int | Yes |  |  |
| 10 | DistrictName | varchar(50) | Yes |  |  |
| 11 | ResolvedFlag | tinyint | Yes |  |  |

### VendorQuery {archive-vendorquery}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 4,057 |
| **Created** | 2021-11-06 20:40:15.747000 |
| **Modified** | 2021-11-08 21:29:55.857000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorQueryNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorQueryDetail {archive-vendorquerydetail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 39,321 |
| **Created** | 2021-11-06 20:40:16.400000 |
| **Modified** | 2021-11-08 21:29:55.883000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryDetailId | int | No |  |  |
| 2 | BidResultsId | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | VendorQueryId | int | Yes |  |  |
| 6 | AddDate | datetime | Yes |  |  |
| 7 | SendDate | datetime | Yes |  |  |
| 8 | ItemQuery | varchar(4000) | Yes |  |  |
| 9 | ItemQueryNotes | varchar(1000) | Yes |  |  |
| 10 | VendorId | int | Yes |  |  |
| 11 | DistrictName | varchar(50) | Yes |  |  |
| 12 | ResolvedFlag | tinyint | Yes |  |  |
| 13 | CommonVendorQueryId | int | Yes |  |  |

### VendorQueryMSRP {archive-vendorquerymsrp}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:17.883000 |
| **Modified** | 2021-11-06 20:40:17.883000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryMSRPId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorQueryMSRPNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorQueryMSRPDetail {archive-vendorquerymsrpdetail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:17.887000 |
| **Modified** | 2021-11-06 20:40:17.887000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryMSRPDetailId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidImportId | int | Yes |  |  |
| 4 | VendorQueryMSRPId | int | Yes |  |  |
| 5 | AddDate | datetime | Yes |  |  |
| 6 | SendDate | datetime | Yes |  |  |
| 7 | MSRPQueryType | int | Yes |  |  |
| 8 | MSRPQuery | varchar(4000) | Yes |  |  |
| 9 | MSRPQueryManufacturers | varchar(MAX) | Yes |  |  |
| 10 | MSRPQueryNotes | varchar(1000) | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | ResolvedFlag | tinyint | Yes |  |  |
| 13 | AllowReply | tinyint | Yes |  |  |
| 14 | ManufacturerSelection | int | Yes |  |  |

### VendorQueryTandM {archive-vendorquerytandm}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 7 |
| **Created** | 2021-11-06 20:40:17.890000 |
| **Modified** | 2021-11-06 20:40:17.890000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryTandMId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorQueryTandMNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorQueryTandMDetail {archive-vendorquerytandmdetail}

| Property | Value |
|----------|-------|
| **Schema** | archive |
| **Rows** | 0 |
| **Created** | 2021-11-06 20:40:18.277000 |
| **Modified** | 2021-11-06 20:40:18.277000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryTandMDetailId | int | No |  |  |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidImportId | int | Yes |  |  |
| 4 | VendorQueryTandMId | int | Yes |  |  |
| 5 | AddDate | datetime | Yes |  |  |
| 6 | SendDate | datetime | Yes |  |  |
| 7 | TandMQueryType | int | Yes |  |  |
| 8 | TandMQuery | varchar(4000) | Yes |  |  |
| 9 | TandMQueryCounties | varchar(1000) | Yes |  |  |
| 10 | TandMQueryNotes | varchar(1000) | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | ResolvedFlag | tinyint | Yes |  |  |

### AccountingDetail {dbo-accountingdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 17:43:23.100000 |
| **Modified** | 2024-06-21 21:30:30.927000 |
| **Primary Key** | AccountingDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AccountingDetailId | int IDENTITY | No |  | PK |
| 2 | UserAccountId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | RequisitionId | int | Yes |  |  |
| 5 | Amount | money | Yes |  |  |

### AccountingFormats {dbo-accountingformats}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 49 |
| **Created** | 2006-08-29 17:57:46.977000 |
| **Modified** | 2024-06-21 21:30:33.807000 |
| **Primary Key** | AccountingFormatId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AccountingFormatId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(255) | Yes |  |  |
| 3 | FileLayoutId | int | Yes |  |  |
| 4 | MaxPODetailItems | int | Yes |  |  |
| 5 | LocationCodeRequired | tinyint | Yes |  |  |
| 6 | VendorBidNumberRequired | tinyint | Yes |  |  |
| 7 | VendorBidCommentsRequired | tinyint | Yes |  |  |
| 8 | UsersDistrictAccountingCodeRequired | tinyint | Yes |  |  |
| 9 | IncidentalOrdersSupported | tinyint | Yes |  |  |
| 11 | ShortName | varchar(50) | Yes |  |  |
| 12 | DetailedFormat | tinyint | Yes |  |  |
| 13 | ScriptURL | varchar(1024) | Yes |  |  |
| 14 | useFirstLast | tinyint | Yes |  |  |

### AccountingUserFields {dbo-accountinguserfields}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 80 |
| **Created** | 2010-04-29 17:12:54.293000 |
| **Modified** | 2024-06-21 21:30:35.157000 |
| **Primary Key** | AccountingUserFieldId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AccountingUserFieldId | int IDENTITY | No |  | PK |
| 2 | AccountingFormatId | int | No |  |  |
| 3 | DistrictId | int | No |  |  |
| 4 | FieldPos | int | Yes |  |  |
| 5 | FieldName | varchar(50) | Yes |  |  |
| 6 | RequiredField | tinyint | Yes |  |  |

### Accounts {dbo-accounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 110,104 |
| **Created** | 2006-08-30 20:46:53.353000 |
| **Modified** | 2024-06-21 22:41:30.240000 |
| **Primary Key** | AccountId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AccountId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | DistrictId | int | Yes |  | FK → dbo.District.DistrictId |
| 4 | SchoolId | int | Yes |  | FK → dbo.School.SchoolId |
| 5 | Code | varchar(50) | Yes |  |  |
| 6 | Description | varchar(512) | Yes |  |  |

### AccountSeparators {dbo-accountseparators}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 17:58:24.650000 |
| **Modified** | 2024-06-21 21:30:42.023000 |
| **Primary Key** | AccountSeparatorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AccountSeparatorId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | Yes |  |  |
| 3 | Code | char(1) | Yes |  |  |

### AddendumItems {dbo-addendumitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2001-08-24 14:40:31.787000 |
| **Modified** | 2024-06-21 21:30:47.287000 |
| **Primary Key** | ItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemId | int | No |  | PK |
| 2 | ItemCode | varchar(15) | Yes |  |  |
| 3 | Description | varchar(255) | Yes |  |  |
| 4 | UnitId | int | Yes |  |  |
| 5 | UnitCode | varchar(20) | Yes |  |  |
| 6 | PriceId | int | Yes |  |  |
| 7 | CatalogPrice | decimal(9,2) | Yes |  |  |
| 8 | Page | int | Yes |  |  |
| 9 | BidPrice | decimal(9,2) | Yes |  |  |
| 10 | CatalogId | int | Yes |  |  |
| 11 | CatalogName | varchar(30) | Yes |  |  |
| 12 | CategoryId | int | Yes |  |  |
| 13 | VendorId | int | Yes |  |  |
| 14 | VendorName | varchar(30) | Yes |  |  |
| 15 | DistrictId | int | Yes |  |  |
| 16 | ContractId | int | Yes |  |  |
| 17 | ContractNumber | varchar(20) | Yes |  |  |

### additems {dbo-additems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2001-08-24 14:40:32.437000 |
| **Modified** | 2024-06-21 21:30:49.150000 |
| **Primary Key** | ITEMID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ITEMID | int | No |  | PK |
| 2 | ITEMCODE | varchar(15) | Yes |  |  |
| 3 | DESCRIPTION | varchar(255) | Yes |  |  |
| 4 | UNITID | int | Yes |  |  |
| 5 | PRICEID | int | Yes |  |  |
| 6 | CATALOGPRICE | decimal(9,2) | Yes |  |  |
| 7 | PAGE | int | Yes |  |  |
| 8 | BIDPRICE | decimal(9,2) | Yes |  |  |
| 9 | CATALOGID | int | Yes |  |  |
| 10 | CATEGORYID | int | Yes |  |  |
| 11 | VENDORID | int | Yes |  |  |
| 12 | DISTRICTID | int | Yes |  |  |
| 13 | CONTRACTID | int | Yes |  |  |
| 14 | CONTRACTNUMBER | varchar(20) | Yes |  |  |
| 15 | VENDORITEMCODE | varchar(20) | Yes |  |  |

### Alerts {dbo-alerts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4 |
| **Created** | 2012-06-13 23:50:42.677000 |
| **Modified** | 2024-06-21 21:30:51.453000 |
| **Primary Key** | AlertID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AlertID | int IDENTITY | No |  | PK |
| 2 | DistrictID | int | Yes |  |  |
| 3 | DisplayStart | datetime | Yes |  |  |
| 4 | DisplayEnd | datetime | Yes |  |  |
| 5 | Message | varchar(MAX) | Yes |  |  |

### allitems {dbo-allitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,276,768 |
| **Created** | 2019-06-13 13:14:40.803000 |
| **Modified** | 2021-11-08 21:28:06.850000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderId | int | Yes |  |  |
| 2 | ItemId | int | Yes |  |  |
| 3 | ItemCode | varchar(50) | Yes |  |  |
| 4 | Description | varchar(2311) | Yes |  |  |
| 5 | UnitCode | varchar(20) | Yes |  |  |
| 6 | VendorItemCode | varchar(50) | Yes |  |  |
| 7 | Alternate | varchar(512) | Yes |  |  |
| 8 | BidPrice | money | Yes |  |  |
| 9 | VendorId | int | Yes |  |  |
| 10 | BidItemId | int | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | CrossRefId | int | Yes |  |  |
| 13 | PricePlanId | int | Yes |  |  |
| 14 | CategoryId | int | Yes |  |  |
| 15 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 16 | ItemBidType | varchar(50) | Yes |  |  |
| 17 | TotalOrdered | int | Yes |  |  |
| 18 | TotalBid | int | Yes |  |  |
| 19 | SysId | int IDENTITY | No |  |  |

### AnswerTypes {dbo-answertypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2011-11-03 15:13:08.257000 |
| **Modified** | 2024-06-21 21:31:01.317000 |
| **Primary Key** | AnswerTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AnswerTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |
| 3 | Mask | varchar(50) | Yes |  |  |
| 4 | RegExp | varchar(1024) | Yes |  |  |

### ApprovalLevels {dbo-approvallevels}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9 |
| **Created** | 2006-08-29 17:59:05.243000 |
| **Modified** | 2024-06-21 21:31:02.580000 |
| **Primary Key** | ApprovalLevelId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ApprovalLevelId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | Yes |  |  |
| 3 | ApprovalLevel | tinyint | No |  |  |

### Approvals {dbo-approvals}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 7,897,407 |
| **Created** | 2006-08-30 21:22:39.243000 |
| **Modified** | 2024-06-21 22:45:16.390000 |
| **Primary Key** | ApprovalId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ApprovalId | int IDENTITY | No |  | PK |
| 2 | ApprovalById | int | Yes |  |  |
| 3 | Level | tinyint | Yes |  |  |
| 4 | StatusId | int | Yes |  |  |
| 5 | RequisitionId | int | Yes |  |  |
| 6 | ApprovalDate | datetime | Yes |  |  |
| 7 | ApproverId | int | Yes |  |  |

### ApprovalsHistory {dbo-approvalshistory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 335,966 |
| **Created** | 2008-01-02 15:34:24.983000 |
| **Modified** | 2024-06-21 22:45:17.703000 |
| **Primary Key** | ApprovalId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ApprovalId | int | No |  | PK |
| 2 | ApprovalById | int | Yes |  |  |
| 3 | Level | tinyint | Yes |  |  |
| 4 | StatusId | int | Yes |  |  |
| 5 | RequisitionId | int | Yes |  |  |
| 6 | ApprovalDate | datetime | Yes |  |  |
| 7 | ApproverId | int | Yes |  |  |

### Audit {dbo-audit}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,568,656 |
| **Created** | 2006-08-30 20:01:00.007000 |
| **Modified** | 2024-06-21 21:31:08.253000 |
| **Primary Key** | AuditId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AuditId | int IDENTITY | No |  | PK |
| 2 | AuditDate | datetime | Yes | (getdate()) |  |
| 3 | AuditBy | int | Yes |  |  |
| 4 | AuditAction | int | Yes |  |  |
| 5 | AuditFile | varchar(50) | Yes |  |  |
| 6 | AuditRecord | int | Yes |  |  |
| 7 | AuditMessage | varchar(255) | Yes |  |  |

### Awardings {dbo-awardings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11,313 |
| **Created** | 2020-03-08 22:13:40.633000 |
| **Modified** | 2024-06-21 21:31:09.540000 |
| **Primary Key** | AwardingId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AwardingId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | StartTimestamp | datetime | No | (getdate()) |  |
| 4 | EndTimestamp | datetime | Yes |  |  |
| 5 | NotificationsCreated | bigint | Yes |  |  |
| 6 | NotificationsSent | datetime | Yes |  |  |

### Awards {dbo-awards}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 138,204 |
| **Created** | 2006-08-29 18:01:45.600000 |
| **Modified** | 2024-06-21 21:31:12.267000 |
| **Primary Key** | AwardId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AwardId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidId | int | Yes |  |  |
| 4 | VendorId | int | Yes |  |  |
| 5 | PricePlanId | int | Yes |  |  |
| 6 | CategoryId | int | Yes |  |  |
| 7 | BidStartDate | datetime | Yes |  |  |
| 8 | BidEndDate | datetime | Yes |  |  |
| 9 | VendorBidNumber | varchar(50) | Yes |  |  |
| 10 | Description | varchar(511) | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | DiscountRate | decimal(9,5) | Yes |  |  |
| 13 | ItemsBid | int | Yes |  |  |
| 14 | AmountBid | money | Yes |  |  |
| 15 | BidDiscountRate | decimal(9,5) | Yes |  |  |
| 16 | StateContractDiscount | decimal(9,5) | Yes |  |  |
| 17 | UseGrossPrices | int | Yes |  |  |
| 18 | BidHeaderId | int | Yes |  |  |
| 19 | DateModified | datetime | Yes |  |  |
| 20 | BidImportId | int | Yes |  |  |

### AwardsCatalogList {dbo-awardscataloglist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 84,245 |
| **Created** | 2006-08-30 19:59:35.850000 |
| **Modified** | 2024-06-21 21:31:15.513000 |
| **Primary Key** | AwardCatalogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AwardCatalogId | int IDENTITY | No |  | PK |
| 2 | AwardId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | DiscountRate | decimal(9,5) | Yes |  |  |
| 5 | DateModified | datetime | Yes |  |  |
| 6 | BidImportCatalogId | int | Yes |  |  |

### AwardTypes {dbo-awardtypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2012-02-16 10:48:30.523000 |
| **Modified** | 2024-06-21 21:31:12.833000 |
| **Primary Key** | AwardTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | AwardTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |

### BatchBook {dbo-batchbook}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 217,611 |
| **Created** | 2006-08-30 19:58:57.460000 |
| **Modified** | 2021-11-08 21:28:07.370000 |
| **Primary Key** | BatchBookId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BatchBookId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BatchId | int | No |  |  |
| 4 | DistrictCode | char(2) | Yes |  |  |
| 5 | Category | char(1) | Yes |  |  |
| 6 | CometCode | char(5) | Yes |  |  |
| 7 | AccountCode | char(50) | Yes |  |  |
| 8 | DistrictId | int | Yes |  |  |
| 9 | CategoryId | int | Yes |  |  |
| 10 | UserId | int | Yes |  |  |
| 11 | BudgetId | int | Yes |  |  |
| 12 | AccountId | int | Yes |  |  |
| 13 | BudgetAccountId | int | Yes |  |  |
| 14 | UserAccountId | int | Yes |  |  |
| 15 | Records | int | Yes |  |  |
| 16 | InputAmount | money | Yes |  |  |
| 17 | CalcAmount | money | Yes |  |  |
| 18 | Errors | int | Yes |  |  |
| 19 | DuplicateOk | tinyint | Yes |  |  |
| 20 | DuplicateDetected | tinyint | Yes |  |  |
| 21 | RequisitionId | int | Yes |  |  |
| 22 | AmountOk | tinyint | Yes |  |  |

### BatchDetail {dbo-batchdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,020,036 |
| **Created** | 2010-02-12 10:54:51.150000 |
| **Modified** | 2024-06-21 21:59:55.823000 |
| **Primary Key** | BatchDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BatchDetailId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BatchBookId | int | Yes |  |  |
| 4 | BatchId | int | No |  |  |
| 5 | RecordNumber | int | Yes |  |  |
| 6 | Type | char(1) | Yes |  |  |
| 7 | DistrictCode | char(2) | Yes |  |  |
| 8 | Category | char(1) | Yes |  |  |
| 9 | CometId | char(5) | Yes |  |  |
| 10 | BookAmount | char(10) | Yes |  |  |
| 11 | ItemCode | char(20) | Yes |  |  |
| 12 | Quantity | char(6) | Yes |  |  |
| 13 | OrigType | char(1) | Yes |  |  |
| 14 | OrigDistrictCode | char(2) | Yes |  |  |
| 15 | OrigCategory | char(1) | Yes |  |  |
| 16 | OrigCometCode | char(5) | Yes |  |  |
| 17 | OrigItemCode | char(15) | Yes |  |  |
| 18 | OrigQuantity | char(6) | Yes |  |  |
| 19 | ErrorField | tinyint | Yes |  |  |
| 20 | DistrictId | int | Yes |  |  |
| 21 | CategoryId | int | Yes |  |  |
| 22 | UserId | int | Yes |  |  |
| 23 | ItemId | int | Yes |  |  |
| 24 | BidPrice | money | Yes |  |  |
| 25 | Qty | int | Yes |  |  |
| 26 | Total | money | Yes |  |  |
| 27 | DetailId | int | Yes |  |  |
| 28 | SourceId | int | Yes |  |  |
| 29 | Modified | datetime | Yes |  |  |
| 30 | ModifiedBy | int | Yes |  |  |
| 31 | PackedCode | varchar(16) | Yes |  |  |
| 32 | Location | char(1) | Yes |  |  |
| 33 | OrigBookAmount | char(10) | Yes |  |  |
| 34 | BatchFileName | varchar(16) | Yes |  |  |
| 35 | BidHeaderId | int | Yes |  |  |
| 36 | PreviousCategory | char(1) | Yes |  |  |
| 37 | PackComplete | tinyint | Yes |  |  |

### BatchDetailInserts {dbo-batchdetailinserts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,176 |
| **Created** | 2006-08-29 12:14:20.803000 |
| **Modified** | 2021-11-08 21:28:19.267000 |
| **Primary Key** | BatchDetailInsertId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BatchDetailInsertId | uniqueidentifier | No | (newsequentialid()) | PK |
| 2 | RequisitionId | int | No |  |  |
| 3 | ItemId | int | Yes |  |  |
| 4 | qty | int | Yes |  |  |
| 5 | BatchDetailId | int | No |  |  |
| 6 | SourceId | int | Yes |  |  |

### Batches {dbo-batches}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14,507 |
| **Created** | 2006-08-30 19:47:38.910000 |
| **Modified** | 2021-11-08 21:28:19.310000 |
| **Primary Key** | BatchId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BatchId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BatchDate | datetime | Yes |  |  |
| 4 | Imported | datetime | Yes |  |  |
| 5 | Converted | datetime | Yes |  |  |
| 6 | Records | int | Yes |  |  |
| 7 | ErrorCount | int | Yes |  |  |
| 8 | Amount | money | Yes |  |  |
| 9 | Type | char(1) | Yes |  |  |
| 10 | InputRecords | int | Yes |  |  |
| 11 | ImportedRecords | int | Yes |  |  |
| 12 | SourceId | int | Yes |  |  |
| 13 | Scheduled | datetime | Yes |  |  |
| 14 | Completed | datetime | Yes |  |  |
| 15 | Description | varchar(255) | Yes |  |  |
| 16 | Started | datetime | Yes |  |  |
| 17 | Loaded | datetime | Yes |  |  |

### BidAnswers {dbo-bidanswers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 552,512 |
| **Created** | 2015-12-21 00:22:38.160000 |
| **Modified** | 2024-06-21 21:31:31.293000 |
| **Primary Key** | BidAnswerId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidAnswerId | int IDENTITY | No |  | PK |
| 2 | BidImportId | int | No |  |  |
| 3 | BidQuestionId | int | No |  |  |
| 4 | CountyId | int | No |  |  |
| 5 | BidTradeId | int | No |  |  |
| 6 | VendorBidTMAnswerId | int | Yes |  |  |

### BidAnswersJournal {dbo-bidanswersjournal}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,264,847 |
| **Created** | 2015-12-21 00:23:13.907000 |
| **Modified** | 2024-06-21 22:41:18.687000 |
| **Primary Key** | BidAnswerJournalId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidAnswerJournalId | int IDENTITY | No |  | PK |
| 2 | BidAnswerId | int | No |  | FK → dbo.BidAnswers.BidAnswerId |
| 3 | SessionId | int | Yes |  |  |
| 4 | DateModified | datetime | No | (getdate()) |  |
| 5 | BidAnswer | varchar(512) | Yes |  |  |
| 6 | BidAnswerExtended | varchar(512) | Yes |  |  |
| 7 | VendorBidTMAnswerJournalId | int | Yes |  |  |

### BidCalendar {dbo-bidcalendar}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2006-08-29 18:20:01.303000 |
| **Modified** | 2024-06-21 21:31:31.703000 |
| **Primary Key** | CalendarId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalendarId | int IDENTITY | No |  | PK |
| 2 | DateAvailable | datetime | Yes |  |  |
| 3 | OpeningDate | datetime | Yes |  |  |
| 4 | Description | varchar(255) | Yes |  |  |
| 5 | CategoryName | varchar(255) | Yes |  |  |
| 6 | CategoryId | int | Yes |  |  |
| 7 | Comments | varchar(4096) | Yes |  |  |
| 8 | Status | varchar(255) | Yes |  |  |
| 9 | StateId | int | Yes |  |  |
| 10 | PricePlanId | int | Yes |  |  |
| 11 | TotalAwardMinimumDiscount | decimal(9,5) | Yes |  |  |
| 12 | AllowTotalAward | tinyint | Yes |  |  |

### BidderCheckList {dbo-bidderchecklist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 140 |
| **Created** | 2012-06-26 15:08:13.293000 |
| **Modified** | 2024-06-21 21:31:32.130000 |
| **Primary Key** | BidderCheckListId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidderCheckListId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CheckListText | varchar(100) | Yes |  |  |
| 4 | AdditionalInfoRTF | varchar(1000) | Yes |  |  |
| 5 | AdditionalInfoRTFText | varchar(1000) | Yes |  |  |
| 7 | DocumentName | varchar(50) | Yes |  |  |
| 8 | OptionalDocument | tinyint | Yes |  |  |
| 13 | OnFileEligible | tinyint | Yes |  |  |
| 14 | UploadEligible | tinyint | Yes |  |  |
| 17 | DocumentTypeId | int | Yes |  |  |
| 25 | ExpirationDateReqd | tinyint | Yes |  |  |
| 26 | DocNumberReqd | tinyint | Yes |  |  |
| 27 | DocNumberLabel | varchar(50) | Yes |  |  |

### BidderCheckListPkgDetail {dbo-bidderchecklistpkgdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,195 |
| **Created** | 2012-06-21 16:32:13.960000 |
| **Modified** | 2024-06-21 21:31:32.560000 |
| **Primary Key** | BidderCheckListPkgDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidderCheckListPkgDetailId | int IDENTITY | No |  | PK |
| 2 | BidderCheckListPkgHeaderId | int | Yes |  |  |
| 3 | BidderCheckListId | int | Yes |  |  |
| 4 | DisplaySequence | int | Yes |  |  |

### BidderCheckListPkgHeader {dbo-bidderchecklistpkgheader}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 56 |
| **Created** | 2012-06-21 15:34:47.430000 |
| **Modified** | 2024-06-21 21:31:32.943000 |
| **Primary Key** | BidderCheckListPkgHeaderId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidderCheckListPkgHeaderId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | PackageName | varchar(80) | Yes |  |  |

### BidDocument {dbo-biddocument}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 10,654 |
| **Created** | 2018-02-19 21:45:12.110000 |
| **Modified** | 2024-06-21 21:31:35.053000 |
| **Primary Key** | BidDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidDocumentId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | DocumentTitle | varchar(80) | Yes |  |  |
| 4 | DocumentFilename | varchar(80) | Yes |  |  |
| 5 | DocumentType | varchar(50) | Yes |  |  |
| 6 | DocumentBody | text | Yes |  |  |

### BidDocumentTypes {dbo-biddocumenttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 298 |
| **Created** | 2011-09-19 12:56:09.340000 |
| **Modified** | 2024-06-21 21:31:35.543000 |
| **Primary Key** | BidDocumentTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidDocumentTypeId | int IDENTITY | No |  | PK |
| 2 | BidType | int | Yes |  |  |
| 3 | Name | varchar(50) | No |  |  |
| 4 | Description | varchar(4096) | Yes |  |  |
| 5 | VendorSpecific | tinyint | Yes |  |  |
| 6 | State | char(2) | Yes |  |  |
| 7 | Sequence | int | Yes |  |  |
| 8 | DistrictVisible | tinyint | Yes |  |  |
| 9 | OnlyShowOne | tinyint | Yes |  |  |
| 10 | Grouping | varchar(50) | Yes |  |  |
| 12 | VendorUnique | tinyint | Yes |  |  |
| 13 | Expires | tinyint | Yes |  |  |

### BidHeaderCheckList {dbo-bidheaderchecklist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 111,945 |
| **Created** | 2012-06-21 16:43:36.613000 |
| **Modified** | 2024-06-21 21:31:37.127000 |
| **Primary Key** | BidHeaderCheckListId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderCheckListId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidderCheckListId | int | Yes |  |  |
| 4 | DisplaySequence | int | Yes |  |  |

### BidHeaderDetail {dbo-bidheaderdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 123,800,580 |
| **Created** | 2021-09-11 19:40:33.573000 |
| **Modified** | 2024-10-28 05:02:15.220000 |
| **Primary Key** | BidHeaderDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDetailId | bigint IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | BidRequestItemId | int | Yes |  |  |
| 5 | Quantity | int | Yes |  |  |
| 6 | DateAdded | datetime | Yes | (getdate()) |  |
| 7 | BidHeaderKey | int | Yes |  |  |
| 13 | RequisitionId | int | Yes |  |  |
| 14 | id | uniqueidentifier | No | (newsequentialid()) |  |

### BidHeaderDetail_Orig {dbo-bidheaderdetail-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 102,658,927 |
| **Created** | 2018-03-13 23:29:26.220000 |
| **Modified** | 2021-09-11 19:40:09.687000 |
| **Primary Key** | BidHeaderDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDetailId | bigint IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | BidRequestItemId | int | Yes |  |  |
| 5 | Quantity | int | Yes |  |  |
| 6 | DateAdded | datetime | Yes | (getdate()) |  |
| 7 | BidHeaderKey | int | Yes |  |  |

### BidHeaderDocument {dbo-bidheaderdocument}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 163,579 |
| **Created** | 2011-09-14 00:13:12.793000 |
| **Modified** | 2024-06-21 21:34:11.400000 |
| **Primary Key** | BidHeaderDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDocumentId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidDocumentId | int | Yes |  |  |
| 4 | DisplaySequence | int | Yes |  |  |

### BidHeaderDocuments {dbo-bidheaderdocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2006-08-29 18:34:18.950000 |
| **Modified** | 2024-06-21 21:34:11.780000 |
| **Primary Key** | BidHeaderDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderDocumentId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | DocumentDate | datetime | Yes |  |  |
| 4 | DocumentTitle | varchar(255) | No |  |  |
| 5 | DocumentFile | varchar(255) | Yes |  |  |
| 6 | DocumentData | text | Yes |  |  |
| 8 | DisplaySeq | int | Yes |  |  |

### BidHeaders {dbo-bidheaders}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9,617 |
| **Created** | 2015-12-06 12:43:44.910000 |
| **Modified** | 2025-07-01 21:57:21.167000 |
| **Primary Key** | BidHeaderKey |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderId | int | Yes |  |  |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | PricePlanId | int | Yes |  |  |
| 5 | DistrictId | int | Yes |  |  |
| 6 | BidDate | datetime | Yes |  |  |
| 7 | BidAwardDate | datetime | Yes |  |  |
| 8 | BidMessage | varchar(1024) | Yes |  |  |
| 9 | BidType | tinyint | Yes |  |  |
| 10 | PriceVarianceLevel | decimal(9,5) | Yes | ((2)) |  |
| 11 | MinimumPOAmount | money | Yes |  |  |
| 12 | Section | int | Yes |  |  |
| 13 | BudgetYearOption | tinyint | Yes |  |  |
| 14 | DateCreated | datetime | Yes | (getdate()) |  |
| 15 | EffectiveFrom | datetime | Yes |  |  |
| 16 | EffectiveUntil | datetime | Yes |  |  |
| 17 | Description | varchar(512) | Yes |  |  |
| 18 | ParentBidHeaderId | int | Yes |  |  |
| 19 | UpdateHold | int | Yes |  |  |
| 20 | ScheduledReaward | datetime | Yes |  |  |
| 21 | AllowTotalAward | tinyint | Yes |  |  |
| 22 | TotalAwardMinimumDiscount | decimal(9,5) | Yes |  |  |
| 23 | CalendarId | int | Yes |  |  |
| 24 | StateId | int | Yes |  |  |
| 25 | MarkAsOriginal | int | Yes |  |  |
| 26 | HostDistrictId | int | Yes |  |  |
| 27 | AwardMsg | varchar(1024) | Yes |  |  |
| 28 | AlertLink | varchar(255) | Yes |  |  |
| 29 | AlertMsg | varchar(4096) | Yes |  |  |
| 30 | BidManagerId | int | Yes |  |  |
| 31 | CompliantAlert | tinyint | Yes |  |  |
| 32 | HostAwardDate | datetime | Yes |  |  |
| 33 | AllowAdditionalManufacturers | tinyint | Yes |  |  |
| 34 | AllowAdditionalProductLines | tinyint | Yes |  |  |
| 35 | UseOptions | tinyint | Yes |  |  |
| 36 | BidHeaderKey | int IDENTITY | No |  | PK |
| 48 | ImageURLRuleset | int | Yes |  |  |
| 50 | ReadyToUseDate | datetime | Yes |  |  |

### BidImportCatalogList {dbo-bidimportcataloglist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 32,925 |
| **Created** | 2015-12-21 00:42:22.377000 |
| **Modified** | 2025-01-27 16:03:22.757000 |
| **Primary Key** | BidImportCatalogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidImportCatalogId | int IDENTITY | No |  | PK |
| 2 | BidImportId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | DiscountRate | decimal(9,5) | Yes |  |  |
| 5 | DateModified | datetime | Yes |  |  |

### BidImportCounties {dbo-bidimportcounties}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 65,169 |
| **Created** | 2012-02-16 12:37:12.793000 |
| **Modified** | 2024-06-21 21:34:14.710000 |
| **Primary Key** | BidImportCountyId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidImportCountyId | int IDENTITY | No |  | PK |
| 2 | BidImportId | int | No |  |  |
| 3 | BidTradeCountyId | int | No |  |  |
| 4 | Active | tinyint | Yes |  |  |
| 5 | DateModified | datetime | No | (getdate()) |  |
| 6 | Comments | varchar(4096) | Yes |  |  |

### BidImports {dbo-bidimports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 55,381 |
| **Created** | 2012-05-23 16:03:46.857000 |
| **Modified** | 2024-06-21 21:34:16.523000 |
| **Primary Key** | BidImportId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidImportId | int | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | VendorId | int | Yes |  |  |
| 5 | BidItemDiscountRate | decimal(9,5) | Yes |  |  |
| 6 | CatalogId | int | Yes |  |  |
| 7 | CatalogDiscountRate | decimal(9,5) | Yes |  |  |
| 8 | VendorBidNumber | varchar(50) | Yes |  |  |
| 9 | ItemsBid | int | Yes |  |  |
| 10 | AmountBid | money | Yes |  |  |
| 11 | MinimumOrder | money | Yes |  |  |
| 12 | FreeDeliveryMinimum | money | Yes |  |  |
| 13 | Status | varchar(50) | Yes |  |  |
| 14 | Comments | varchar(1024) | Yes |  |  |
| 15 | DateModified | datetime | Yes |  |  |
| 16 | StateContractDiscount | decimal(9,5) | Yes |  |  |
| 17 | AdditionalHandlingAmount | money | Yes |  |  |
| 18 | FreeHandlingAmount | money | Yes |  |  |
| 19 | FreeHandlingStart | datetime | Yes |  |  |
| 20 | FreeHandlingEnd | datetime | Yes |  |  |
| 21 | UseVendorContactInfo | tinyint | Yes |  |  |
| 22 | ContactEmail | varchar(255) | Yes |  |  |
| 23 | ContactName | varchar(50) | Yes |  |  |
| 24 | ContactPhone | varchar(20) | Yes |  |  |
| 25 | ContactFax | varchar(20) | Yes |  |  |
| 26 | POVendorContactId | int | Yes |  |  |
| 27 | VendorBidId | int | Yes |  |  |
| 28 | BidVendorContactId | int | Yes |  |  |
| 29 | WebsiteLink | varchar(255) | Yes |  |  |
| 30 | CatalogDiscountComments | varchar(512) | Yes |  |  |
| 32 | BidHeaderKey | int | Yes |  |  |

### BidItems {dbo-biditems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 27,308,634 |
| **Created** | 2018-03-18 23:32:19.243000 |
| **Modified** | 2024-10-28 05:03:25.067000 |
| **Primary Key** | BidItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidItemId | int IDENTITY | No |  | PK |
| 2 | BidItemId_Old | int | Yes |  |  |
| 3 | BidId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | Price | money | Yes |  |  |
| 6 | Alternate | varchar(512) | Yes |  |  |
| 7 | BidQuantity | int | Yes |  |  |
| 8 | BidRequest | int | Yes |  |  |
| 9 | AwardId | int | Yes |  |  |
| 10 | VendorItemCode | varchar(50) | Yes |  |  |
| 11 | CrossRefId | int | Yes |  |  |
| 12 | ItemBidType | varchar(32) | Yes |  |  |
| 13 | PackedItemCode | varchar(50) | Yes |  |  |
| 14 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 15 | DateUpdated | datetime | Yes |  |  |
| 16 | PageNo | int | Yes |  |  |
| 17 | RTK_MSDSId | int | Yes |  |  |
| 18 | BidResultsId | int | Yes |  |  |
| 19 | ContractNumber | varchar(50) | Yes |  |  |
| 20 | AdditionalShipping | tinyint | Yes |  |  |

### BidItems_Old {dbo-biditems-old}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 16,238,384 |
| **Created** | 2006-08-29 18:35:33.900000 |
| **Modified** | 2021-03-17 23:18:57.703000 |
| **Primary Key** | BidItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidItemId | int IDENTITY | No |  | PK |
| 2 | BidId | int | Yes |  |  |
| 3 | ItemId | int | Yes |  |  |
| 4 | Price | money | Yes |  |  |
| 5 | Alternate | varchar(512) | Yes |  |  |
| 6 | BidQuantity | int | Yes |  |  |
| 7 | BidRequest | int | Yes |  |  |
| 8 | AwardId | int | Yes |  |  |
| 9 | VendorItemCode | varchar(50) | Yes |  |  |
| 10 | CrossRefId | int | Yes |  |  |
| 11 | ItemBidType | varchar(32) | Yes |  |  |
| 12 | PackedItemCode | varchar(50) | Yes |  |  |
| 13 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 14 | DateUpdated | datetime | Yes |  |  |
| 15 | PageNo | int | Yes |  |  |
| 16 | RTK_MSDSId | int | Yes |  |  |
| 17 | BidResultsId | int | Yes |  |  |
| 18 | ContractNumber | varchar(50) | Yes |  |  |
| 20 | AdditionalShipping | tinyint | Yes |  |  |

### BidManagers {dbo-bidmanagers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2011-09-07 12:11:23.430000 |
| **Modified** | 2024-06-21 21:35:28.127000 |
| **Primary Key** | BidManagerId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidManagerId | int IDENTITY | No |  | PK |
| 2 | Name | varchar(50) | Yes |  |  |
| 3 | UserId | int | Yes |  |  |
| 4 | Phone | varchar(20) | Yes |  |  |
| 5 | Email | varchar(255) | Yes |  |  |

### BidManufacturers {dbo-bidmanufacturers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 252,694 |
| **Created** | 2012-04-24 22:22:04.297000 |
| **Modified** | 2024-06-21 21:35:29.893000 |
| **Primary Key** | BMAId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BMAId | int IDENTITY | No |  | PK |
| 2 | BidId | int | No |  |  |
| 3 | ManufacturerId | int | No |  |  |
| 4 | DiscountRate | decimal(9,5) | Yes |  |  |
| 5 | Modified | datetime | No | (getdate()) |  |

### BidMappedItems {dbo-bidmappeditems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,047,571 |
| **Created** | 2017-02-19 10:18:11.940000 |
| **Modified** | 2026-03-21 02:40:10.660000 |
| **Primary Key** | BidMappedItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMappedItemId | uniqueidentifier | No | (newid()) | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | OrigItemId | int | No |  |  |
| 4 | NewItemId | int | No |  |  |
| 5 | ReasonCode | varchar(20) | Yes |  |  |
| 6 | MapDate | datetime | No | (getdate()) |  |

### BidMgrConfiguration {dbo-bidmgrconfiguration}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2012-07-11 11:55:29.887000 |
| **Modified** | 2024-06-21 21:35:31.720000 |
| **Primary Key** | BidMgrConfigurationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMgrConfigurationId | int IDENTITY | No |  | PK |
| 2 | CheckListHeaderRTF | varchar(5000) | Yes |  |  |

### BidMgrTagFile {dbo-bidmgrtagfile}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4,419,284 |
| **Created** | 2015-11-17 09:59:52.827000 |
| **Modified** | 2024-06-21 21:31:28.480000 |
| **Primary Key** | BidMgrTagFileId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMgrTagFileId | int IDENTITY | No |  | PK |
| 2 | Usr | int | Yes |  |  |
| 3 | Tbl | int | Yes |  |  |
| 4 | Ptr | int | Yes |  |  |
| 5 | Val | char(10) | Yes |  |  |
| 6 | OrigVal | char(10) | Yes |  |  |

### BidMSRPResultPrices {dbo-bidmsrpresultprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 422,692 |
| **Created** | 2015-12-21 00:43:21.367000 |
| **Modified** | 2024-06-21 21:35:33.737000 |
| **Primary Key** | BidMSRPResultPricesId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMSRPResultPricesId | int IDENTITY | No |  | PK |
| 2 | BidMSRPResultsId | int | No |  |  |
| 3 | BidMSRPResultsProductLineId | int | Yes |  |  |
| 4 | Active | tinyint | Yes |  |  |
| 5 | BidRequestPriceRangeId | int | No |  |  |
| 6 | RangeBase | money | Yes |  |  |
| 7 | RangeWeight | decimal(9,5) | Yes |  |  |
| 8 | RangeValue | decimal(9,5) | Yes |  |  |

### BidMSRPResults {dbo-bidmsrpresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 40,980 |
| **Created** | 2015-12-21 00:44:01.833000 |
| **Modified** | 2024-06-21 21:35:34.323000 |
| **Primary Key** | BidMSRPResultsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMSRPResultsId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidHeaderId | int | No |  |  |
| 4 | BidImportId | int | No |  |  |
| 5 | ManufacturerId | int | Yes |  |  |
| 6 | DiscountRate | decimal(9,5) | Yes |  |  |
| 7 | Modified | datetime | No | (getdate()) |  |
| 8 | DiscountRateString | char(10) | Yes |  |  |
| 9 | WriteInFlag | tinyint | Yes |  |  |
| 10 | WriteInManufacturer | varchar(100) | Yes |  |  |
| 11 | VendorNotes | varchar(1000) | Yes |  |  |
| 12 | BidRequestManufacturerId | int | Yes |  |  |
| 13 | WinningBidOverride | tinyint | Yes |  |  |
| 14 | PriceListTypeId | int | Yes |  |  |
| 15 | AuthorizationLetter | tinyint | Yes |  |  |
| 16 | SubmittedExcel | tinyint | Yes |  |  |
| 17 | ProductCatalog | tinyint | Yes |  |  |
| 18 | TotalAward | tinyint | Yes |  |  |
| 19 | VendorPriceFile | tinyint | Yes |  |  |
| 20 | TotalAwardDiscount | decimal(9,5) | Yes |  |  |
| 21 | TotalAwardString | varchar(20) | Yes |  |  |
| 22 | ExcelFileApproved | tinyint | Yes |  |  |
| 23 | BidHeaderKey | int | Yes |  |  |

### BidMSRPResultsProductLines {dbo-bidmsrpresultsproductlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 110,442 |
| **Created** | 2013-10-23 16:34:43.920000 |
| **Modified** | 2024-06-21 21:35:35.020000 |
| **Primary Key** | BidMSRPResultsProductLineId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidMSRPResultsProductLineId | int IDENTITY | No |  | PK |
| 2 | BidMSRPResultsId | int | No |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | BidRequestProductLineId | int | Yes |  |  |
| 5 | WriteInProductLineName | varchar(100) | Yes |  |  |
| 6 | BidRequestOptionId | int | Yes |  |  |
| 7 | MSRPOptionId | int | Yes |  |  |
| 8 | OptionName | varchar(50) | Yes |  |  |
| 9 | WriteInProductLineFlag | tinyint | Yes |  |  |
| 10 | Weight | decimal(9,5) | Yes |  |  |
| 11 | Modified | datetime | Yes |  |  |
| 12 | WeightedDiscount | decimal(9,5) | Yes |  |  |
| 13 | ManufacturerProductLineId | int | Yes |  |  |

### BidPackage {dbo-bidpackage}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 50 |
| **Created** | 2011-09-14 00:13:43.807000 |
| **Modified** | 2024-06-21 21:35:36.153000 |
| **Primary Key** | BidPackageId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidPackageId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidPackageName | varchar(80) | Yes |  |  |

### BidPackageDocument {dbo-bidpackagedocument}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,430 |
| **Created** | 2011-09-14 00:14:00.087000 |
| **Modified** | 2024-06-21 21:35:36.553000 |
| **Primary Key** | BidPackageDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidPackageDocumentId | int IDENTITY | No |  | PK |
| 2 | BidPackageId | int | Yes |  |  |
| 3 | BidDocumentId | int | Yes |  |  |
| 4 | DisplaySequence | int | Yes |  |  |

### BidProductLinePrices {dbo-bidproductlineprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,326,490 |
| **Created** | 2013-12-12 14:40:02.690000 |
| **Modified** | 2024-06-21 21:30:58.943000 |
| **Primary Key** | BidProductLinePriceId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidProductLinePriceId | int IDENTITY | No |  | PK |
| 2 | BidProductLineId | int | No |  |  |
| 3 | RangeBase | money | Yes |  |  |
| 4 | DiscountRate | decimal(9,5) | Yes |  |  |
| 5 | Modified | datetime | No | (getdate()) |  |

### BidProductLines {dbo-bidproductlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 286,844 |
| **Created** | 2013-12-12 14:46:57.087000 |
| **Modified** | 2024-06-21 21:31:14.497000 |
| **Primary Key** | BidProductLineId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidProductLineId | int IDENTITY | No |  | PK |
| 2 | BMAId | int | No |  |  |
| 3 | ManufacturerProductLineId | int | No |  |  |
| 4 | MSRPOptionId | int | No |  |  |
| 5 | DiscountRate | decimal(9,5) | Yes |  |  |
| 6 | Modified | datetime | No | (getdate()) |  |

### BidQuestions {dbo-bidquestions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 23,509 |
| **Created** | 2015-12-21 00:44:55.720000 |
| **Modified** | 2024-06-21 22:41:19.313000 |
| **Primary Key** | BidQuestionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidQuestionId | int IDENTITY | No |  | PK |
| 2 | BidTradeId | int | No |  | FK → dbo.BidTrades.BidTradeId |
| 3 | BidSection | varchar(255) | Yes |  |  |
| 4 | Sequence | int | Yes |  |  |
| 5 | QuestionPositionX | int | Yes |  |  |
| 6 | QuestionPositionY | int | Yes |  |  |
| 7 | QuestionHeight | int | Yes |  |  |
| 8 | QuestionWidth | int | Yes |  |  |
| 9 | QuestionText | varchar(MAX) | No |  |  |
| 10 | QuestionQty | int | Yes |  |  |
| 11 | QuestionUOMId | int | Yes |  |  |
| 12 | AnswerPositionX | int | Yes |  |  |
| 13 | AnswerPositionY | int | Yes |  |  |
| 14 | AnswerHeight | int | Yes |  |  |
| 15 | AnswerWidth | int | Yes |  |  |
| 16 | AnswerTypeId | int | Yes |  |  |
| 17 | AnswerTypeMask | varchar(50) | Yes |  |  |
| 18 | Weight | decimal(9,5) | Yes |  |  |
| 19 | Required | tinyint | Yes |  |  |
| 20 | ExtendCalculation | tinyint | Yes |  |  |
| 21 | ExtdCalcTypeId | int | Yes |  |  |
| 22 | ExtdCalcMask | varchar(50) | Yes |  |  |
| 23 | UseInCalculation | tinyint | Yes |  |  |
| 24 | OnChecklist | tinyint | Yes |  |  |
| 25 | CountyIdSpecific | int | Yes |  |  |
| 26 | BidEntryDisplayLabel | varchar(255) | Yes |  |  |

### BidReawards {dbo-bidreawards}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 615 |
| **Created** | 2016-11-28 13:23:33.150000 |
| **Modified** | 2024-06-21 21:51:29.437000 |
| **Primary Key** | BidReawardId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidReawardId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ReawardDate | datetime | No |  |  |
| 4 | EffectiveFrom | datetime | No |  |  |
| 5 | EffectiveUntil | datetime | No |  |  |
| 6 | Comments | varchar(4096) | Yes |  |  |

### BidRequestItemMergeActions {dbo-bidrequestitemmergeactions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 36,542 |
| **Created** | 2021-09-11 20:01:27.460000 |
| **Modified** | 2024-06-21 21:51:29.793000 |
| **Primary Key** | BidRequestItemMergeActionsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestItemMergeActionsId | int IDENTITY | No |  | PK |
| 2 | BidRequestItemId | int | Yes |  |  |
| 3 | DestinationBidRequestItemId | int | Yes |  |  |
| 4 | Merged | tinyint | Yes |  |  |

### BidRequestItemMergeActions_Orig {dbo-bidrequestitemmergeactions-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 27,168 |
| **Created** | 2015-08-17 14:32:05.093000 |
| **Modified** | 2021-09-11 20:01:13.797000 |
| **Primary Key** | BidRequestItemMergeActionsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestItemMergeActionsId | int IDENTITY | No |  | PK |
| 2 | BidRequestItemId | int | Yes |  |  |
| 4 | DestinationBidRequestItemId | int | Yes |  |  |
| 5 | Merged | tinyint | Yes |  |  |

### BidRequestItemMergeActions_Saved_101521 {dbo-bidrequestitemmergeactions-saved-101521}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 27,298 |
| **Created** | 2021-10-15 12:51:08.043000 |
| **Modified** | 2021-10-15 12:51:08.043000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestItemMergeActionsId | int IDENTITY | No |  |  |
| 2 | BidRequestItemId | int | Yes |  |  |
| 3 | DestinationBidRequestItemId | int | Yes |  |  |
| 4 | Merged | tinyint | Yes |  |  |
| 5 | rowguid | uniqueidentifier | No |  |  |

### BidRequestItems {dbo-bidrequestitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 27,866,138 |
| **Created** | 2021-09-11 18:50:23.843000 |
| **Modified** | 2024-10-28 05:04:42.273000 |
| **Primary Key** | BidRequestItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestItemId | int IDENTITY | No |  | PK |
| 2 | BidRequestItemId_OLD | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | BidRequest | int | Yes |  |  |
| 6 | Active | tinyint | Yes |  |  |
| 7 | RequisitionCount | int | Yes |  |  |
| 8 | Status | varchar(50) | Yes |  |  |
| 9 | Comments | varchar(1024) | Yes |  |  |
| 10 | BidRequestAmount | money | Yes |  |  |
| 11 | Checksum | int | Yes |  |  |
| 12 | MasterItemCodePtr | int | Yes |  |  |
| 13 | BidHeaderKey | int | Yes |  |  |
| 14 | ImageURL | varchar(300) | Yes |  |  |
| 15 | SDS_URL | varchar(300) | Yes |  |  |

### BidRequestItems_Orig {dbo-bidrequestitems-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 25,521,585 |
| **Created** | 2021-08-14 09:18:57.370000 |
| **Modified** | 2021-09-11 18:50:17.617000 |
| **Primary Key** | BidRequestItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestItemId | int IDENTITY | No |  | PK |
| 2 | BidRequestItemId_OLD | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | BidRequest | int | Yes |  |  |
| 6 | Active | tinyint | Yes |  |  |
| 7 | RequisitionCount | int | Yes |  |  |
| 8 | Status | varchar(50) | Yes |  |  |
| 9 | Comments | varchar(1024) | Yes |  |  |
| 10 | BidRequestAmount | money | Yes |  |  |
| 11 | Checksum | int | Yes |  |  |
| 12 | MasterItemCodePtr | int | Yes |  |  |
| 13 | BidHeaderKey | int | Yes |  |  |
| 14 | ImageURL | varchar(300) | Yes |  |  |
| 15 | SDS_URL | varchar(300) | Yes |  |  |

### BidRequestManufacturer {dbo-bidrequestmanufacturer}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 104,823 |
| **Created** | 2015-12-21 00:45:33.660000 |
| **Modified** | 2024-06-21 22:41:19.933000 |
| **Primary Key** | BidRequestManufacturerId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestManufacturerId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  | FK → dbo.BidHeaders.BidHeaderId |
| 4 | ManufacturerId | int | Yes |  |  |
| 5 | SequenceNumber | int | Yes |  |  |
| 6 | AllowAdditionalProductLines | tinyint | Yes |  |  |
| 7 | UseOptions | tinyint | Yes |  |  |
| 8 | BidHeaderKey | int | Yes |  |  |

### BidRequestOptions {dbo-bidrequestoptions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 422,035 |
| **Created** | 2015-12-21 00:46:04.580000 |
| **Modified** | 2024-06-21 21:52:09.563000 |
| **Primary Key** | BidRequestOptionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestOptionId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ManufacturerId | int | Yes |  |  |
| 4 | ManufacturerProductLineId | int | Yes |  |  |
| 5 | OptionId | int | Yes |  |  |
| 6 | BidRequestManufacturerId | int | Yes |  |  |
| 7 | BidRequestProductLineId | int | Yes |  |  |
| 8 | Name | varchar(50) | No |  |  |
| 9 | Weight | decimal(9,5) | Yes |  |  |

### BidRequestPriceRanges {dbo-bidrequestpriceranges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,897,760 |
| **Created** | 2015-12-21 00:46:37.010000 |
| **Modified** | 2024-06-21 21:52:12.693000 |
| **Primary Key** | BidRequestPriceRangeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestPriceRangeId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidRequestManufacturerId | int | Yes |  |  |
| 4 | BidRequestProductLineId | int | Yes |  |  |
| 5 | RangeBase | money | Yes |  |  |
| 6 | RangeWeight | decimal(9,5) | Yes |  |  |
| 7 | BidRequestMSRPOptionId | int | Yes |  |  |

### BidRequestProductLines {dbo-bidrequestproductlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 175,875 |
| **Created** | 2015-12-21 00:48:17.117000 |
| **Modified** | 2024-06-21 21:52:13.287000 |
| **Primary Key** | BidRequestProductLineId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidRequestProductLineId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidRequestManufacturerId | int | No |  |  |
| 4 | ManufacturerProductLineId | int | Yes |  |  |
| 5 | UseOptions | tinyint | Yes |  |  |

### BidResponses {dbo-bidresponses}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2011-11-08 15:53:15.453000 |
| **Modified** | 2024-06-21 21:52:13.560000 |
| **Primary Key** | BidResponseId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidResponseId | int IDENTITY | No |  | PK |
| 2 | BidImportId | int | No |  |  |
| 3 | CountyId | int | No |  |  |
| 4 | BidQuestionId | int | No |  |  |
| 5 | BidAnswer | varchar(MAX) | Yes |  |  |

### BidResultChanges {dbo-bidresultchanges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 18,229,521 |
| **Created** | 2015-11-18 23:38:38.030000 |
| **Modified** | 2024-06-21 21:52:24.963000 |
| **Primary Key** | BRChangeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BRChangeId | int IDENTITY | No |  | PK |
| 2 | BidResultsId | int | Yes |  |  |
| 3 | ChangeDate | datetime | Yes |  |  |
| 4 | PrevActive | int | Yes |  |  |
| 5 | PrevUnitPrice | money | Yes |  |  |
| 6 | NewActive | int | Yes |  |  |
| 7 | NewUnitPrice | money | Yes |  |  |
| 8 | PrevBidType | char(1) | Yes |  |  |
| 9 | NewBidType | char(1) | Yes |  |  |
| 10 | PrevComments | varchar(1024) | Yes |  |  |

### BidResults {dbo-bidresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 33,162,067 |
| **Created** | 2022-07-19 20:09:38.437000 |
| **Modified** | 2026-03-07 05:18:36.333000 |
| **Primary Key** | BidResultsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidResultsId | int IDENTITY | No |  | PK |
| 2 | BidImportId | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | BidRequestItemId | int | Yes |  |  |
| 5 | CategoryId | int | Yes |  |  |
| 6 | DistrictId | int | Yes |  |  |
| 7 | ItemId | int | Yes |  |  |
| 8 | ItemCode | varchar(50) | Yes |  |  |
| 9 | Units | varchar(16) | Yes |  |  |
| 10 | Alternate | varchar(512) | Yes |  |  |
| 11 | Quantity | int | Yes |  |  |
| 12 | ItemBidType | char(1) | Yes |  |  |
| 13 | UnitPrice | money | Yes |  |  |
| 14 | Cost | money | Yes |  |  |
| 15 | VendorItemCode | varchar(50) | Yes |  |  |
| 16 | QuantityBid | int | Yes |  |  |
| 17 | ItemsPerUnit | varchar(50) | Yes |  |  |
| 18 | UnitId | int | Yes |  |  |
| 19 | Status | varchar(51) | Yes |  |  |
| 20 | Comments | varchar(1024) | Yes |  |  |
| 21 | Active | int | Yes |  |  |
| 22 | PageNo | int | Yes |  |  |
| 23 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 24 | ModifiedDate | datetime | Yes |  |  |
| 25 | ModifiedSessionId | int | Yes |  |  |
| 26 | ModifiedBy | int | Yes |  |  |
| 27 | RTK_MSDSId | int | Yes |  |  |
| 28 | RTK_MSDSNotNeeded | tinyint | Yes |  |  |
| 29 | ContractNumber | varchar(50) | Yes |  |  |
| 30 | OriginalAwardedItem | tinyint | Yes |  |  |
| 31 | VOMId | int | Yes |  |  |
| 32 | AdditionalShipping | tinyint | Yes |  |  |
| 33 | ManufacturerBid | varchar(50) | Yes |  |  |
| 34 | ManufPartNoBid | varchar(50) | Yes |  |  |
| 35 | LinerGaugeMicrons | numeric(2,0) | Yes |  |  |
| 36 | LinerGaugeMil | numeric(3,2) | Yes |  |  |
| 37 | LinerCaseWeight | numeric(4,2) | Yes |  |  |
| 38 | LinerDimWidth | numeric(4,2) | Yes |  |  |
| 39 | LinerDimDepth | numeric(4,2) | Yes |  |  |
| 40 | LinerDimLength | numeric(4,2) | Yes |  |  |
| 41 | PackedManufPartNoBid | varchar(50) | Yes |  |  |
| 42 | BidHeaderKey | int | Yes |  |  |
| 43 | SDS_URL | varchar(300) | Yes |  |  |
| 44 | ImageURL | varchar(300) | Yes |  |  |
| 45 | UPC_ISBN | varchar(20) | Yes |  |  |
| 46 | UNSPSC | varchar(50) | Yes |  |  |
| 47 | UniqueItemNumber | varchar(50) | Yes |  |  |
| 50 | DigitallyDelivered | tinyint | Yes |  |  |
| 51 | MinimumOrderQuantity | int | Yes |  |  |
| 52 | PrescriptionRequired | bit | Yes |  |  |
| 53 | PerishableItem | bit | Yes |  |  |
| 54 | HashKey | varbinary(64) | Yes |  |  |
| 55 | ProductNames | varchar(4000) | Yes |  |  |
| 56 | TypeAheads | nvarchar(4000) | Yes |  |  |
| 57 | AIShortDesc | nvarchar(1024) | Yes |  |  |
| 58 | AIFullDesc | nvarchar(4000) | Yes |  |  |
| 59 | AIUNSPSC | varchar(20) | Yes |  |  |
| 60 | AIDate | datetime | Yes |  |  |

### BidResults_Orig {dbo-bidresults-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 55,592,743 |
| **Created** | 2021-08-16 23:02:14.180000 |
| **Modified** | 2021-09-11 18:58:41.837000 |
| **Primary Key** | BidResultsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidResultsId | int IDENTITY | No |  | PK |
| 2 | BidImportId | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | BidRequestItemId | int | Yes |  |  |
| 5 | CategoryId | int | Yes |  |  |
| 6 | DistrictId | int | Yes |  |  |
| 7 | ItemId | int | Yes |  |  |
| 8 | ItemCode | varchar(50) | Yes |  |  |
| 9 | Units | varchar(16) | Yes |  |  |
| 10 | Alternate | varchar(512) | Yes |  |  |
| 11 | Quantity | int | Yes |  |  |
| 12 | ItemBidType | char(1) | Yes |  |  |
| 13 | UnitPrice | money | Yes |  |  |
| 14 | Cost | money | Yes |  |  |
| 15 | VendorItemCode | varchar(50) | Yes |  |  |
| 16 | QuantityBid | int | Yes |  |  |
| 17 | ItemsPerUnit | varchar(50) | Yes |  |  |
| 18 | UnitId | int | Yes |  |  |
| 19 | Status | varchar(51) | Yes |  |  |
| 20 | Comments | varchar(1024) | Yes |  |  |
| 21 | Active | int | Yes |  |  |
| 22 | PageNo | int | Yes |  |  |
| 23 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 24 | ModifiedDate | datetime | Yes |  |  |
| 25 | ModifiedSessionId | int | Yes |  |  |
| 26 | ModifiedBy | int | Yes |  |  |
| 27 | RTK_MSDSId | int | Yes |  |  |
| 28 | RTK_MSDSNotNeeded | tinyint | Yes |  |  |
| 29 | ContractNumber | varchar(50) | Yes |  |  |
| 30 | OriginalAwardedItem | tinyint | Yes |  |  |
| 31 | VOMId | int | Yes |  |  |
| 32 | AdditionalShipping | tinyint | Yes |  |  |
| 33 | ManufacturerBid | varchar(50) | Yes |  |  |
| 34 | ManufPartNoBid | varchar(50) | Yes |  |  |
| 35 | LinerGaugeMicrons | numeric(2,0) | Yes |  |  |
| 36 | LinerGaugeMil | numeric(3,2) | Yes |  |  |
| 37 | LinerCaseWeight | numeric(4,2) | Yes |  |  |
| 38 | LinerDimWidth | numeric(4,2) | Yes |  |  |
| 39 | LinerDimDepth | numeric(4,2) | Yes |  |  |
| 40 | LinerDimLength | numeric(4,2) | Yes |  |  |
| 41 | PackedManufPartNoBid | varchar(50) | Yes |  |  |
| 42 | BidHeaderKey | int | Yes |  |  |
| 43 | SDS_URL | varchar(300) | Yes |  |  |
| 44 | ImageURL | varchar(300) | Yes |  |  |
| 45 | UPC_ISBN | varchar(20) | Yes |  |  |
| 46 | UNSPSC | varchar(50) | Yes |  |  |

### BidResultsChangeLog {dbo-bidresultschangelog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 240,737 |
| **Created** | 2006-08-29 18:50:42.950000 |
| **Modified** | 2024-06-21 21:54:25.560000 |
| **Primary Key** | BRChangeLogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BRChangeLogId | int IDENTITY | No |  | PK |
| 2 | ChangeDate | datetime | Yes |  |  |
| 3 | BidResultsId | int | Yes |  |  |
| 4 | SessionId | int | Yes |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | Reason | varchar(4096) | Yes |  |  |
| 7 | RequisitionId | int | Yes |  |  |
| 8 | DetailId | int | Yes |  |  |
| 9 | ItemId | int | Yes |  |  |
| 10 | BidType | char(1) | Yes |  |  |
| 11 | NetPrice | money | Yes |  |  |
| 13 | VOMId | int | Yes |  |  |

### Bids {dbo-bids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 146,241 |
| **Created** | 2006-08-29 18:50:59.917000 |
| **Modified** | 2024-06-21 21:54:27.443000 |
| **Primary Key** | BidId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CoopId | int | Yes |  |  |
| 4 | ClosingDate | datetime | Yes |  |  |
| 5 | OpeningDate | datetime | Yes |  |  |
| 6 | EffectiveFrom | datetime | Yes |  |  |
| 7 | EffectiveUntil | datetime | Yes |  |  |
| 8 | Name | varchar(255) | Yes |  |  |
| 9 | PricePlanId | int | Yes |  |  |
| 10 | CategoryId | int | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | BidDiscountRate | decimal(8,5) | Yes |  |  |
| 13 | VendorBidNumber | varchar(50) | Yes |  |  |
| 14 | DistrictId | int | Yes |  |  |
| 15 | ItemsBid | int | Yes |  |  |
| 16 | AmountBid | money | Yes |  |  |
| 17 | CatalogId | int | Yes |  |  |
| 18 | Description | varchar(511) | Yes |  |  |
| 19 | BidHeaderId | int | Yes |  |  |
| 20 | UseGrossPrices | int | Yes |  |  |
| 21 | BidImportId | int | Yes |  |  |
| 22 | DateModified | datetime | Yes |  |  |
| 25 | AdditionalHandlingAmount | money | Yes |  |  |
| 28 | FreeHandlingAmount | money | Yes |  |  |
| 29 | FreeHandlingStart | datetime | Yes |  |  |
| 30 | FreeHandlingEnd | datetime | Yes |  |  |
| 31 | WebsiteLink | varchar(255) | Yes |  |  |

### BidsCatalogList {dbo-bidscataloglist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 84,410 |
| **Created** | 2006-08-30 19:16:57.567000 |
| **Modified** | 2024-06-21 21:54:27.997000 |
| **Primary Key** | BidCatalogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidCatalogId | int IDENTITY | No |  | PK |
| 2 | BidId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | DiscountRate | decimal(9,5) | Yes |  |  |
| 5 | BidImportCatalogId | int | Yes |  |  |

### BidTradeCounties {dbo-bidtradecounties}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 42,912 |
| **Created** | 2011-11-03 15:13:08.240000 |
| **Modified** | 2024-06-21 21:54:28.323000 |
| **Primary Key** | BidTradeCountyId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidTradeCountyId | int IDENTITY | No |  | PK |
| 2 | BidTradeId | int | No |  |  |
| 3 | CountyId | int | No |  |  |

### BidTrades {dbo-bidtrades}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,591 |
| **Created** | 2011-11-03 15:13:08.160000 |
| **Modified** | 2024-06-21 21:54:29.210000 |
| **Primary Key** | BidTradeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidTradeId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | TradeId | int | No |  |  |
| 4 | Title | varchar(255) | No |  |  |
| 5 | Specifications | varchar(MAX) | No |  |  |

### BidTypes {dbo-bidtypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2006-08-29 18:51:41.073000 |
| **Modified** | 2024-06-21 21:54:29.420000 |
| **Primary Key** | BidTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |

### BookTypes {dbo-booktypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4 |
| **Created** | 2006-08-30 19:15:52.660000 |
| **Modified** | 2024-06-21 21:54:29.557000 |
| **Primary Key** | BookTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BookTypeId | int IDENTITY | No |  | PK |
| 2 | BookType | varchar(50) | No |  |  |

### BudgetAccounts {dbo-budgetaccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,417,444 |
| **Created** | 2006-08-30 19:15:17.363000 |
| **Modified** | 2026-03-07 05:19:02.577000 |
| **Primary Key** | BudgetAccountId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BudgetAccountId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BudgetId | int | Yes |  | FK → dbo.Budgets.BudgetId |
| 4 | AccountId | int | Yes |  | FK → dbo.Accounts.AccountId |
| 5 | BudgetAmount | money | Yes |  |  |
| 6 | AmountAvailable | money | Yes |  |  |
| 7 | UseAllocations | tinyint | Yes |  |  |

### Budgets {dbo-budgets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 16,410 |
| **Created** | 2006-08-30 19:14:09.303000 |
| **Modified** | 2024-06-21 22:41:20.617000 |
| **Primary Key** | BudgetId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BudgetId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  | FK → dbo.District.DistrictId |
| 3 | Active | tinyint | Yes |  |  |
| 4 | Name | varchar(30) | Yes |  |  |
| 5 | StartDate | datetime | Yes |  |  |
| 6 | EndDate | datetime | Yes |  |  |
| 7 | VisibleFrom | datetime | Yes |  |  |
| 8 | VisibleUntil | datetime | Yes |  |  |
| 10 | AnnualCutoff | datetime | Yes |  |  |
| 11 | EditFrom | datetime | Yes |  |  |
| 12 | EditUntil | datetime | Yes |  |  |
| 13 | EarlyAccess | datetime | Yes |  |  |

### CalDistricts {dbo-caldistricts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 21:11:54.787000 |
| **Modified** | 2024-06-21 21:54:29.783000 |
| **Primary Key** | CalDistrictId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalDistrictId | int IDENTITY | No |  | PK |
| 2 | CalendarId | int | Yes |  |  |
| 3 | DistrictId | int | Yes |  |  |

### CalendarDates {dbo-calendardates}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,261 |
| **Created** | 2009-10-30 00:13:08.603000 |
| **Modified** | 2024-06-21 21:54:29.997000 |
| **Primary Key** | CalendarDateId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalendarDateId | int IDENTITY | No |  | PK |
| 2 | CalendarId | int | No |  |  |
| 3 | Description | varchar(50) | Yes |  |  |
| 4 | Date1 | datetime | No |  |  |
| 5 | Date2 | datetime | Yes |  |  |
| 6 | Date3 | datetime | Yes |  |  |
| 7 | Date4 | datetime | Yes |  |  |

### CalendarIB {dbo-calendarib}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 684 |
| **Created** | 2009-10-30 10:26:04.950000 |
| **Modified** | 2024-06-21 21:54:30.760000 |
| **Primary Key** | CalendarIBId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalendarIBId | int IDENTITY | No |  | PK |
| 2 | CalendarId | int | No |  |  |
| 3 | IBTypeId | int | No |  |  |
| 4 | ScheduleId | int | No |  |  |
| 5 | CalendarTypeId | int | No |  |  |

### CalendarItems {dbo-calendaritems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-30 19:12:59.960000 |
| **Modified** | 2024-06-21 21:54:31.027000 |
| **Primary Key** | CalendarItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalendarItemId | int | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | LinkId | int | Yes |  |  |
| 4 | LinkType | char(1) | Yes |  |  |
| 5 | Description | varchar(50) | Yes |  |  |
| 6 | ScheduledEventDate | datetime | Yes |  |  |
| 7 | ActualEventDate | datetime | Yes |  |  |

### Calendars {dbo-calendars}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 300 |
| **Created** | 2009-10-30 10:22:14.940000 |
| **Modified** | 2024-06-21 21:54:31.700000 |
| **Primary Key** | CalendarId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalendarId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | No |  |  |
| 3 | BudgetYear | int | No |  |  |
| 4 | ScheduleId | int | No |  |  |
| 5 | CalendarTypeId | int | No |  |  |
| 6 | Description | varchar(50) | No |  |  |
| 9 | HeaderText | varchar(8000) | Yes |  |  |
| 10 | FooterText | varchar(8000) | Yes |  |  |
| 11 | HeaderTextHTML | varchar(4096) | Yes |  |  |
| 12 | FooterTextHTML | varchar(4096) | Yes |  |  |

### CalendarTypes {dbo-calendartypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2009-10-30 00:13:08.497000 |
| **Modified** | 2024-06-21 21:54:31.960000 |
| **Primary Key** | CalendarTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CalendarTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |
| 3 | DateCount | int | No |  |  |
| 4 | TimeSpace1to2 | int | Yes |  |  |
| 5 | TimeSpace2to3 | int | Yes |  |  |
| 6 | TimeSpace3to4 | int | Yes |  |  |

### Carolina Living Items {dbo-carolina-living-items}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,017 |
| **Created** | 2023-06-14 15:01:10.960000 |
| **Modified** | 2023-06-14 15:01:10.960000 |
| **Primary Key** | inventorynumber |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | inventorynumber | nvarchar(255) | No |  | PK |
| 2 | Description | nvarchar(255) | Yes |  |  |

### Catalog {dbo-catalog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4,050 |
| **Created** | 2020-03-05 19:21:36.897000 |
| **Modified** | 2026-01-22 20:16:25.373000 |
| **Primary Key** | CatalogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | Yes |  | FK → dbo.Category.CategoryId |
| 4 | VendorId | int | Yes |  | FK → dbo.Vendors.VendorId |
| 5 | Name | varchar(50) | Yes |  |  |
| 6 | DisplayedVendorName | varchar(50) | Yes |  |  |
| 7 | ImportFormat | tinyint | Yes |  |  |
| 8 | Prefix | varchar(10) | Yes |  |  |
| 9 | NextNumber | int | Yes |  |  |
| 10 | VendorFormat | int | Yes |  |  |
| 11 | Description | varchar(255) | Yes |  |  |
| 12 | CrossRefLetter | char(1) | Yes |  |  |
| 13 | DropSeq | varchar(16) | Yes |  |  |
| 14 | CatalogYear | char(2) | Yes |  |  |
| 15 | EffectiveFrom | datetime | Yes |  |  |
| 16 | EffectiveUntil | datetime | Yes |  |  |
| 17 | CreateDate | datetime | Yes |  |  |
| 18 | PostDate | datetime | Yes |  |  |
| 19 | WebDesc | varchar(50) | Yes |  |  |
| 20 | WebLink | varchar(255) | Yes |  |  |
| 21 | NotValidForOB | tinyint | Yes |  |  |
| 22 | AlertMsg | varchar(1024) | Yes |  |  |
| 23 | BeginDefault | datetime | Yes |  |  |
| 24 | PackExp | varchar(1024) | Yes |  |  |
| 25 | PackReplace | varchar(1024) | Yes |  |  |
| 26 | Index | int | Yes |  |  |
| 27 | Page1 | int | Yes |  |  |
| 28 | MaxPage | int | Yes |  |  |
| 29 | PDFAvailable | tinyint | Yes |  |  |
| 30 | pdfDirectory | varchar(1024) | Yes |  |  |
| 31 | BasePath | varchar(255) | Yes |  |  |
| 32 | BaseCatalogId | int | Yes |  |  |

### CatalogImportFields {dbo-catalogimportfields}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 15 |
| **Created** | 2011-10-03 16:31:49.660000 |
| **Modified** | 2024-06-21 21:57:15.667000 |
| **Primary Key** | CatalogImportFieldId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogImportFieldId | int IDENTITY | No |  | PK |
| 2 | CatalogImportId | int | No |  |  |
| 3 | SequenceId | int | Yes |  |  |
| 4 | Name | varchar(50) | No |  |  |
| 5 | Optional | tinyint | Yes |  |  |

### CatalogImportMap {dbo-catalogimportmap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2011-10-03 16:31:49.713000 |
| **Modified** | 2024-06-21 21:57:15.913000 |
| **Primary Key** | CatalogImportMapId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogImportMapId | int IDENTITY | No |  | PK |
| 2 | CatalogId | int | No |  |  |
| 3 | CatalogImportFieldId | int | No |  |  |
| 4 | ImportIndex | int | No |  |  |
| 5 | ImportRegExp | varchar(1024) | Yes |  |  |

### CatalogPricing {dbo-catalogpricing}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-09-24 15:39:15.900000 |
| **Modified** | 2024-06-21 21:57:16.123000 |
| **Primary Key** | CPId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CPId | int IDENTITY | No |  | PK |
| 2 | CrossRefId | int | No |  |  |
| 3 | ACLId | int | No |  |  |
| 4 | AwardId | int | No |  |  |
| 5 | BidId | int | No |  |  |
| 6 | NetPrice | money | Yes |  |  |

### CatalogRequest {dbo-catalogrequest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2015-03-24 17:15:37.737000 |
| **Modified** | 2024-06-21 21:57:16.320000 |
| **Primary Key** | CatalogRequestId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogRequestId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | Yes |  |  |
| 3 | EmailAddress | varchar(255) | Yes |  |  |
| 4 | Fax | varchar(20) | Yes |  |  |
| 5 | AddDate | datetime | Yes |  |  |
| 6 | SendDate | datetime | Yes |  |  |
| 7 | EmailAddress2 | varchar(255) | Yes |  |  |
| 8 | EmailCCAddress | varchar(255) | Yes |  |  |
| 9 | MessageContent | varchar(MAX) | Yes |  |  |
| 10 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 11 | CatalogRequestNotes | varchar(1000) | Yes |  |  |
| 12 | ContactName | varchar(255) | Yes |  |  |

### CatalogRequestDetail {dbo-catalogrequestdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2015-12-21 00:48:59.723000 |
| **Modified** | 2024-06-21 22:41:20.740000 |
| **Primary Key** | CatalogRequestDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogRequestDetailId | int IDENTITY | No |  | PK |
| 2 | CatalogRequestId | int | Yes |  | FK → dbo.CatalogRequest.CatalogRequestId |
| 3 | AddDate | datetime | Yes |  |  |
| 4 | SendDate | datetime | Yes |  |  |
| 5 | CatalogRequestType | int | Yes |  |  |
| 6 | CatalogRequestMsg | varchar(4000) | Yes |  |  |
| 7 | CatalogRequestNotes | varchar(1000) | Yes |  |  |
| 8 | VendorId | int | Yes |  |  |
| 9 | ResolvedFlag | tinyint | Yes |  |  |

### CatalogRequestStatus {dbo-catalogrequeststatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2015-12-21 00:49:32.870000 |
| **Modified** | 2024-06-21 22:41:20.853000 |
| **Primary Key** | CatalogRequestStatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogRequestStatusId | int IDENTITY | No |  | PK |
| 2 | CatalogRequestId | int | Yes |  | FK → dbo.CatalogRequest.CatalogRequestId |
| 3 | StatusId | int | Yes |  |  |
| 4 | StatusDate | datetime | Yes |  |  |
| 5 | FollowUpDate | datetime | Yes |  |  |

### CatalogText {dbo-catalogtext}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 112,799 |
| **Created** | 2012-07-27 22:18:23.583000 |
| **Modified** | 2021-11-08 21:28:22.250000 |
| **Primary Key** | CatalogTextId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogTextId | int IDENTITY | No |  | PK |
| 2 | CatalogId | int | No |  |  |
| 3 | PageNbr | int | No |  |  |
| 4 | BaseFileName | varchar(255) | No |  |  |
| 5 | TextData | nvarchar(MAX) | Yes |  |  |

### CatalogTextParts {dbo-catalogtextparts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 17,179,537 |
| **Created** | 2017-04-08 21:03:39.433000 |
| **Modified** | 2021-11-08 21:28:47.520000 |
| **Primary Key** | CatalogTextPartId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CatalogTextPartId | int IDENTITY | No |  | PK |
| 2 | CatalogTextId | int | No |  |  |
| 3 | BaseOffset | int | Yes |  |  |
| 4 | TextPart | varchar(4096) | Yes |  |  |

### Category {dbo-category}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 134 |
| **Created** | 2006-08-30 19:11:31.427000 |
| **Modified** | 2025-01-12 19:21:30.217000 |
| **Primary Key** | CategoryId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CategoryId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryNumber | int | Yes |  |  |
| 4 | Name | varchar(50) | Yes |  |  |
| 5 | EDSId | int | Yes |  |  |
| 6 | Prefix | varchar(10) | Yes |  |  |
| 7 | NextNumber | int | Yes |  |  |
| 8 | AllowAddenda | int | Yes |  |  |
| 9 | HeadingTitle | varchar(32) | Yes |  |  |
| 10 | ExtraTitle | varchar(128) | Yes |  |  |
| 11 | KeywordExamples | varchar(50) | Yes |  |  |
| 12 | OnSavingsReport | int | Yes |  |  |
| 13 | Code | varchar(16) | Yes |  |  |
| 14 | Type | int | Yes |  |  |
| 15 | BreakOnHeadingChange | int | Yes |  |  |
| 16 | MasterBookCopies | int | Yes |  |  |
| 18 | Grouping | varchar(50) | Yes |  |  |
| 19 | AppendBidMessage | tinyint | Yes |  |  |
| 20 | DefaultHeadingID | int | Yes |  |  |
| 21 | AvgDiscountFactor | decimal(9,5) | Yes | ((0.6)) |  |
| 22 | useCatalogViewer | tinyint | Yes |  |  |
| 27 | RTKLocation | varchar(50) | Yes |  |  |
| 38 | Description | varchar(2048) | Yes |  |  |
| 39 | Priority | tinyint | Yes |  |  |

### CatList {dbo-catlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 155,059 |
| **Created** | 2015-07-21 12:30:20.877000 |
| **Modified** | 2021-11-08 21:28:47.603000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CategoryName | varchar(50) | Yes |  |  |
| 2 | PriceplanCode | varchar(20) | Yes |  |  |
| 3 | DistrictName | varchar(50) | Yes |  |  |
| 4 | SchoolName | varchar(50) | Yes |  |  |
| 5 | SchoolAddress | varchar(30) | Yes |  |  |
| 6 | SchoolCity | varchar(25) | Yes |  |  |
| 7 | SchoolState | varchar(2) | Yes |  |  |
| 8 | SchoolZip | varchar(10) | Yes |  |  |
| 9 | Attention | varchar(50) | Yes |  |  |
| 10 | UserNumber | int | Yes |  |  |

### CertificateAuthority {dbo-certificateauthority}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2010-01-19 11:47:03.137000 |
| **Modified** | 2024-06-21 21:57:22.430000 |
| **Primary Key** | CertificateAuthorityId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CertificateAuthorityId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | StateId | int | No |  |  |
| 4 | CertificateName | varchar(50) | No |  |  |
| 5 | CertificatesExpire | tinyint | Yes |  |  |
| 6 | ExpireInMonths | int | Yes |  |  |

### ChargeTypes {dbo-chargetypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14 |
| **Created** | 2007-03-20 18:05:46.967000 |
| **Modified** | 2026-01-06 15:57:06.727000 |
| **Primary Key** | ChargeTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ChargeTypeId | int IDENTITY | No |  | PK |
| 2 | Active | int | Yes |  |  |
| 3 | Description | varchar(50) | Yes |  |  |
| 4 | RTK | int | Yes |  |  |
| 5 | Frequency | int | Yes |  |  |
| 6 | Repeats | int | Yes |  |  |
| 7 | FrequencyData | varchar(50) | Yes |  |  |
| 8 | AccountingChargeCode | varchar(50) | Yes |  |  |
| 9 | LM | tinyint | Yes |  |  |
| 24 | ContinuanceDesc | varchar(128) | Yes |  |  |

### CommonMSRPVendorQuery {dbo-commonmsrpvendorquery}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4 |
| **Created** | 2014-02-26 16:20:14.497000 |
| **Modified** | 2024-06-21 21:57:23.310000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CommonMSRPVendorQueryId | int IDENTITY | No |  |  |
| 2 | CategoryIdSpecific | int | Yes |  |  |
| 3 | CommonQuestion | varchar(500) | Yes |  |  |
| 4 | GroupFilter | varchar(50) | Yes |  |  |
| 5 | AllowReply | tinyint | Yes |  |  |
| 6 | ManufacturerSelection | int | Yes |  |  |

### CommonTandMVendorQuery {dbo-commontandmvendorquery}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 22 |
| **Created** | 2013-01-21 14:15:18.447000 |
| **Modified** | 2024-06-21 21:57:23.583000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CommonTandMVendorQueryId | int IDENTITY | No |  |  |
| 2 | CategoryIdSpecific | int | Yes |  |  |
| 3 | CommonQuestion | varchar(500) | Yes |  |  |
| 4 | GroupFilter | varchar(50) | Yes |  |  |

### CommonVendorQuery {dbo-commonvendorquery}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 43 |
| **Created** | 2013-03-06 14:57:25.323000 |
| **Modified** | 2024-06-21 21:57:24.033000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CommonVendorQueryId | int IDENTITY | No |  |  |
| 2 | CategoryIdSpecific | int | Yes |  |  |
| 3 | CommonQuestion | varchar(1000) | Yes |  |  |

### CommonVendorQueryAnswer {dbo-commonvendorqueryanswer}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-05-07 23:00:40.300000 |
| **Modified** | 2024-06-21 21:57:24.400000 |
| **Primary Key** | CommonVendorQueryAnswerId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CommonVendorQueryAnswerId | int IDENTITY | No |  | PK |
| 2 | CommonVendorQueryId | int | Yes |  |  |
| 3 | SeqNumber | tinyint | Yes |  |  |
| 4 | AnswerText | varchar(100) | Yes |  |  |
| 5 | AnswerAction | int | Yes |  |  |

### ContractTypes {dbo-contracttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-30 19:10:14.770000 |
| **Modified** | 2021-11-08 21:28:47.630000 |
| **Primary Key** | ContractId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ContractId | int | No |  | PK |
| 2 | ContractType | varchar(20) | Yes |  |  |
| 3 | NumberRequired | tinyint | Yes |  |  |

### Control {dbo-control}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2007-03-22 13:08:30.530000 |
| **Modified** | 2024-06-21 21:57:27.870000 |
| **Primary Key** | ControlId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ControlId | int IDENTITY | No |  | PK |
| 2 | LastPriceUpdateStart | datetime | Yes |  |  |
| 3 | LastPriceUpdateEnd | datetime | Yes |  |  |
| 4 | ControlYear | int | Yes |  |  |
| 5 | RTKBaseYear | int | Yes |  |  |
| 6 | BillingYear | int | Yes |  |  |

### Coops {dbo-coops}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 20 |
| **Created** | 2006-08-30 19:09:36.960000 |
| **Modified** | 2024-06-21 21:57:28.827000 |
| **Primary Key** | CoopId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CoopId | int | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Code | char(2) | Yes |  |  |
| 4 | Name | varchar(50) | Yes |  |  |

### CopyRequests {dbo-copyrequests}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 24,259 |
| **Created** | 2006-08-29 21:14:05.100000 |
| **Modified** | 2024-06-21 21:57:32.900000 |
| **Primary Key** | CopyRequestId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CopyRequestId | int IDENTITY | No |  | PK |
| 2 | RSId | int | No |  |  |
| 3 | SessionId | int | No |  |  |
| 4 | StartTime | datetime | Yes |  |  |
| 5 | EndTime | datetime | Yes |  |  |
| 6 | Requested | datetime | Yes |  |  |

### Counties {dbo-counties}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 78 |
| **Created** | 2008-06-09 14:14:44.107000 |
| **Modified** | 2024-06-21 21:57:33.313000 |
| **Primary Key** | CountyId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CountyId | int IDENTITY | No |  | PK |
| 2 | State | char(2) | No |  |  |
| 3 | Name | varchar(50) | No |  |  |
| 4 | StateId | int | Yes |  |  |

### CoverView {dbo-coverview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-11-03 14:35:51.927000 |
| **Modified** | 2021-11-08 21:28:47.640000 |
| **Primary Key** | CoverViewId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictId | int | No |  |  |
| 2 | DistrictCode | varchar(2) | Yes |  |  |
| 3 | DistrictName | varchar(50) | Yes |  |  |
| 4 | DistrictAddress1 | varchar(30) | Yes |  |  |
| 5 | DistrictAddress2 | varchar(30) | Yes |  |  |
| 6 | DistrictAddress3 | varchar(30) | Yes |  |  |
| 7 | DistrictCity | varchar(25) | Yes |  |  |
| 8 | DistrictState | varchar(2) | Yes |  |  |
| 9 | DistrictZipcode | varchar(10) | Yes |  |  |
| 10 | SchoolId | int | Yes |  |  |
| 11 | SchoolName | varchar(50) | Yes |  |  |
| 12 | SchoolAddress1 | varchar(30) | Yes |  |  |
| 13 | SchoolAddress2 | varchar(30) | Yes |  |  |
| 14 | SchoolAddress3 | varchar(30) | Yes |  |  |
| 15 | SchoolCity | varchar(25) | Yes |  |  |
| 16 | SchoolState | varchar(2) | Yes |  |  |
| 17 | SchoolZipcode | varchar(10) | Yes |  |  |
| 18 | UserId | int | Yes |  |  |
| 19 | UserName | varchar(50) | Yes |  |  |
| 20 | CometId | int | Yes |  |  |
| 21 | AccountCode | varchar(50) | Yes |  |  |
| 22 | AccountCount | int | Yes |  |  |
| 23 | BudgetStartDate | datetime | Yes |  |  |
| 24 | BudgetEndDate | datetime | Yes |  |  |
| 25 | ItemCount | int | Yes |  |  |
| 26 | CategoryId | int | Yes |  |  |
| 27 | OrderBookId | int | Yes |  |  |
| 28 | CategoryDescription | varchar(255) | Yes |  |  |
| 29 | PricePlanDescription | varchar(255) | Yes |  |  |
| 30 | UsesBooklet | int | Yes |  |  |
| 31 | UsesOnline | int | Yes |  |  |
| 32 | RepMsg | varchar(512) | Yes |  |  |
| 33 | IBTypeId | int | Yes |  |  |
| 34 | BookType | varchar(50) | Yes |  |  |
| 35 | ScheduleGroup | varchar(50) | Yes |  |  |
| 36 | StateName | varchar(50) | Yes |  |  |
| 37 | CoverViewId | uniqueidentifier | No | (newsequentialid()) | PK |

### CrossRefs {dbo-crossrefs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 168,675,390 |
| **Created** | 2018-03-19 17:40:40.743000 |
| **Modified** | 2026-03-07 08:08:02.987000 |
| **Primary Key** | CrossRefId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CrossRefId | int IDENTITY | No |  | PK |
| 2 | CrossRefId_Old | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | VendorItemCode | varchar(50) | Yes |  |  |
| 6 | CatalogId | int | Yes |  |  |
| 7 | CatalogPrice | money | Yes |  |  |
| 8 | Page | char(4) | Yes |  |  |
| 9 | CatalogYear | char(2) | Yes |  |  |
| 10 | CrossRefLocation | char(1) | Yes |  |  |
| 11 | PackedCode | varchar(50) | Yes | ('([dbo].[uf_PackCode]([VendorItemCode]))') |  |
| 12 | Manufacturor | varchar(50) | Yes |  |  |
| 13 | ManufacturorPartNumber | varchar(50) | Yes |  |  |
| 14 | DateDeactivated | datetime | Yes |  |  |
| 15 | DateUpdated | datetime | Yes | (getdate()) |  |
| 16 | GrossPrice | money | Yes |  |  |
| 17 | DoNotDiscount | int | Yes |  |  |
| 18 | RTK_MSDSId | int | Yes |  |  |
| 19 | RTK_MSDSNotNeeded | tinyint | Yes |  |  |
| 20 | ReplacementCrossRefId | int | Yes |  |  |
| 21 | AdditionalShipping | tinyint | Yes |  |  |
| 22 | FullDescription | varchar(4096) | Yes |  |  |
| 23 | UOM | varchar(20) | Yes |  |  |
| 24 | MatchKey | varchar(150) | Yes |  |  |
| 25 | ManufacturerId | int | Yes |  |  |
| 26 | ProductLine | varchar(50) | Yes |  |  |
| 27 | ManufacturerProductLineId | int | Yes |  |  |
| 28 | ItemsPerUnit | varchar(30) | Yes |  |  |
| 29 | MSDSFlag | tinyint | Yes |  |  |
| 30 | MSDSRef | varchar(255) | Yes |  |  |
| 31 | Heading | varchar(50) | Yes |  |  |
| 32 | UniqueItemNumber | varchar(50) | Yes |  |  |
| 33 | ShortDescription | varchar(512) | Yes |  |  |
| 34 | keyword | varchar(1024) | Yes |  |  |
| 35 | ImageURL | varchar(1024) | Yes |  |  |
| 38 | UPC_ISBN | varchar(20) | Yes |  |  |
| 39 | UNSPSC | varchar(20) | Yes |  |  |
| 44 | ImageId | bigint | Yes |  |  |
| 46 | PerishableItem | bit | Yes | ((0)) |  |
| 47 | PrescriptionRequired | bit | Yes | ((0)) |  |
| 49 | DigitallyDelivered | tinyint | Yes |  |  |
| 50 | MinimumOrderQuantity | int | Yes |  |  |
| 51 | HashKey | varbinary(64) | Yes |  |  |
| 52 | ProductNames | nvarchar(4000) | Yes |  |  |
| 53 | TypeAheads | nvarchar(4000) | Yes |  |  |
| 54 | AIShortDesc | nvarchar(1024) | Yes |  |  |
| 55 | AIFullDesc | nvarchar(4000) | Yes |  |  |
| 56 | AIUNSPSC | varchar(20) | Yes |  |  |
| 57 | AIDate | datetime | Yes |  |  |

### CSCommands {dbo-cscommands}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 16 |
| **Created** | 2012-02-12 21:59:51.380000 |
| **Modified** | 2024-06-21 21:57:38.540000 |
| **Primary Key** | CSCommandId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CSCommandId | int IDENTITY | No |  | PK |
| 2 | ShortDesc | varchar(50) | No |  |  |
| 3 | FullDescription | varchar(1024) | Yes |  |  |
| 4 | Command | varchar(255) | No |  |  |
| 5 | Target | varchar(255) | Yes |  |  |
| 6 | SecurityRoleId | int | Yes |  |  |

### CSMessageFiles {dbo-csmessagefiles}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-06-14 00:09:05.897000 |
| **Modified** | 2024-06-21 21:57:38.727000 |
| **Primary Key** | CSMessageFileID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CSMessageFileID | int IDENTITY | No |  | PK |
| 2 | CSMessageID | int | No |  |  |
| 3 | CSFileName | varchar(255) | No |  |  |
| 4 | CSFile | varbinary(MAX) | No |  |  |

### CSMessages {dbo-csmessages}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11,924 |
| **Created** | 2012-06-14 00:09:16.347000 |
| **Modified** | 2024-06-21 21:57:39.920000 |
| **Primary Key** | CSMessageID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CSMessageID | int IDENTITY | No |  | PK |
| 2 | UserID | int | No |  |  |
| 3 | CSMessage | varchar(MAX) | Yes |  |  |

### CSRep {dbo-csrep}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 45 |
| **Created** | 2006-08-30 19:04:35.973000 |
| **Modified** | 2024-06-21 21:57:40.263000 |
| **Primary Key** | CSRepId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | CSRepId | int IDENTITY | No |  | PK |
| 2 | Name | varchar(30) | Yes |  |  |
| 3 | ID | char(2) | Yes |  |  |
| 4 | UserId | int | Yes |  |  |
| 6 | Phone | varchar(20) | Yes |  |  |
| 7 | EMail | varchar(128) | Yes |  |  |

### CXmlSession {dbo-cxmlsession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 65,957 |
| **Created** | 2008-01-29 12:03:15.670000 |
| **Modified** | 2024-06-21 21:57:46.850000 |
| **Primary Key** | SessionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SessionId | int | No |  | PK |
| 2 | payloadId | varchar(255) | Yes |  |  |
| 3 | buyerCookie | varchar(255) | Yes |  |  |
| 4 | BrowserFormPost | varchar(255) | Yes |  |  |
| 5 | fromDomain | varchar(255) | Yes |  |  |
| 6 | fromIdentity | varchar(255) | Yes |  |  |
| 7 | toDomain | varchar(255) | Yes |  |  |
| 8 | toIdentity | varchar(255) | Yes |  |  |
| 9 | senderDomain | varchar(255) | Yes |  |  |
| 10 | senderIdentity | varchar(255) | Yes |  |  |
| 11 | fromUserAgent | varchar(255) | Yes |  |  |
| 12 | OrigReqId | int | Yes |  |  |
| 13 | RequisitionId | int | Yes |  |  |
| 14 | CategoryId | int | Yes |  |  |
| 15 | Mode | int | Yes |  |  |
| 16 | BudgetAccountId | int | Yes |  |  |
| 17 | UserAccountId | int | Yes |  |  |
| 18 | AccountCode | varchar(50) | Yes |  |  |
| 19 | BudgetId | int | Yes |  |  |
| 20 | UniqueId | uniqueidentifier | Yes | (newid()) |  |

### dchtest {dbo-dchtest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,192 |
| **Created** | 2015-11-18 21:39:01.207000 |
| **Modified** | 2021-11-08 06:55:55.540000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POId | int | No |  |  |
| 2 | PONumber | varchar(24) | Yes |  |  |
| 3 | ItemCount | int | Yes |  |  |
| 4 | Amount | money | Yes |  |  |
| 5 | BudgetName | varchar(30) | Yes |  |  |
| 6 | RequisitionNumber | varchar(24) | Yes |  |  |
| 7 | AccountCode | varchar(50) | Yes |  |  |
| 8 | Attention | varchar(50) | Yes |  |  |
| 9 | CometId | int | Yes |  |  |
| 10 | DistrictCode | varchar(4) | Yes |  |  |
| 11 | DistrictName | varchar(50) | Yes |  |  |
| 12 | DistrictNameAddress | varchar(237) | Yes |  |  |
| 13 | SchoolName | varchar(50) | Yes |  |  |
| 14 | SchoolNameAddress | varchar(189) | Yes |  |  |
| 15 | VendorCode | varchar(16) | Yes |  |  |
| 16 | VendorPhone | varchar(25) | Yes |  |  |
| 17 | DistrictVendorCode | varchar(20) | Yes |  |  |
| 18 | VendorName | varchar(50) | Yes |  |  |
| 19 | VendorNameAddress | varchar(249) | Yes |  |  |
| 20 | PODate | datetime | Yes |  |  |
| 21 | DatePrinted | datetime | Yes |  |  |
| 22 | DatePrintedDetail | datetime | Yes |  |  |
| 23 | DateExported | datetime | Yes |  |  |
| 24 | DistrictId | int | Yes |  |  |
| 25 | CategoryId | int | Yes |  |  |
| 26 | BudgetId | int | Yes |  |  |
| 27 | AccountId | int | Yes |  |  |
| 28 | VendorId | int | Yes |  |  |
| 29 | UserId | int | Yes |  |  |
| 30 | SchoolId | int | No |  |  |
| 31 | VendorBidNumber | varchar(50) | Yes |  |  |
| 32 | VendorBidComments | varchar(540) | Yes |  |  |
| 33 | CategoryCode | char(1) | Yes |  |  |
| 34 | CategoryName | varchar(50) | Yes |  |  |
| 35 | DiscountRate | decimal(9,5) | Yes |  |  |
| 36 | DiscountAmount | money | Yes |  |  |
| 37 | TotalGross | money | Yes |  |  |
| 38 | LocationCode | varchar(32) | No |  |  |
| 39 | ShippingAmount | money | Yes |  |  |
| 40 | ShippingPercentage | decimal(9,5) | Yes |  |  |
| 41 | ShippingNameAddress | varchar(189) | Yes |  |  |
| 42 | DistrictAddress1 | varchar(30) | Yes |  |  |
| 43 | DistrictAddress2 | varchar(30) | Yes |  |  |
| 44 | DistrictAddress3 | varchar(30) | Yes |  |  |
| 45 | DistrictCity | varchar(25) | Yes |  |  |
| 46 | DistrictState | varchar(2) | Yes |  |  |
| 47 | DistrictZipcode | varchar(10) | Yes |  |  |
| 48 | SchoolAddress1 | varchar(30) | Yes |  |  |
| 49 | SchoolAddress2 | varchar(30) | Yes |  |  |
| 50 | SchoolAddress3 | varchar(30) | Yes |  |  |
| 51 | SchoolCity | varchar(25) | Yes |  |  |
| 52 | SchoolState | varchar(2) | Yes |  |  |
| 53 | SchoolZipcode | varchar(10) | Yes |  |  |
| 54 | VendorsAddress1 | varchar(50) | Yes |  |  |
| 55 | VendorsAddress2 | varchar(50) | Yes |  |  |
| 56 | VendorsAddress3 | varchar(50) | Yes |  |  |
| 57 | VendorsCity | varchar(50) | Yes |  |  |
| 58 | VendorsState | varchar(2) | Yes |  |  |
| 59 | VendorsZipcode | varchar(10) | Yes |  |  |
| 60 | ShipLocationsAddress1 | varchar(30) | Yes |  |  |
| 61 | ShipLocationsAddress2 | varchar(30) | Yes |  |  |
| 62 | ShipLocationsAddress3 | varchar(30) | Yes |  |  |
| 63 | ShipLocationsCity | varchar(25) | Yes |  |  |
| 64 | ShipLocationsState | varchar(2) | Yes |  |  |
| 65 | ShipLocationsZipcode | varchar(10) | Yes |  |  |
| 66 | ShipLocationsName | varchar(50) | Yes |  |  |
| 67 | DistrictMessage | varchar(4096) | Yes |  |  |
| 68 | BidDate | datetime | Yes |  |  |
| 69 | UsersDistrictAcctgCode | varchar(20) | Yes |  |  |
| 70 | AwardsBidHeaderId | int | Yes |  |  |
| 71 | ExportedToVendor | datetime | Yes |  |  |

### DebugMsgs {dbo-debugmsgs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 22,580,010 |
| **Created** | 2016-03-01 19:47:44.113000 |
| **Modified** | 2021-11-08 21:28:49.047000 |
| **Primary Key** | SysId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SysId | bigint IDENTITY | No |  | PK |
| 2 | LogDate | datetime | Yes | (getdate()) |  |
| 3 | Msg | varchar(1024) | Yes |  |  |

### DebugMsgs_Orig {dbo-debugmsgs-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,211,696 |
| **Created** | 2006-08-29 21:20:17.023000 |
| **Modified** | 2016-03-01 19:50:07.903000 |
| **Primary Key** | sysid |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | sysid | int IDENTITY | No |  | PK |
| 2 | LogDate | datetime | Yes | (getdate()) |  |
| 3 | Msg | varchar(1024) | Yes |  |  |

### Detail {dbo-detail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 31,786,381 |
| **Created** | 2015-11-16 20:46:13.593000 |
| **Modified** | 2026-03-21 03:16:23.770000 |
| **Primary Key** | DetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailId | int IDENTITY | No |  | PK |
| 2 | RequisitionId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | AddendumItem | tinyint | Yes |  |  |
| 6 | ItemCode | varchar(50) | Yes |  |  |
| 7 | Quantity | int | Yes |  |  |
| 8 | LastYearsQuantity | int | Yes |  |  |
| 9 | Description | varchar(1024) | Yes |  |  |
| 10 | UnitId | int | Yes |  |  |
| 11 | UnitCode | varchar(20) | Yes |  |  |
| 12 | BidPrice | money | Yes |  |  |
| 13 | CatalogPrice | money | Yes |  |  |
| 14 | GrossPrice | money | Yes |  |  |
| 15 | DiscountRate | decimal(9,5) | Yes |  |  |
| 16 | CatalogPage | char(4) | Yes |  |  |
| 17 | PricePlanId | int | Yes |  |  |
| 18 | PriceId | int | Yes |  |  |
| 19 | AwardId | int | Yes |  |  |
| 20 | VendorId | int | Yes |  |  |
| 21 | VendorItemCode | varchar(50) | Yes |  |  |
| 22 | Alternate | varchar(1024) | Yes |  |  |
| 23 | POId | int | Yes |  |  |
| 24 | BatchDetailId | int | Yes |  |  |
| 25 | Modified | datetime | Yes |  |  |
| 26 | ModifiedById | int | Yes |  |  |
| 27 | SourceId | int | Yes |  |  |
| 28 | SortSeq | varchar(64) | Yes |  |  |
| 29 | BidItemId | int | Yes |  |  |
| 30 | ExtraDescription | varchar(1024) | Yes |  |  |
| 31 | ReProc | tinyint | Yes |  |  |
| 32 | UseGrossPrices | tinyint | Yes |  |  |
| 33 | BidHeaderId | int | Yes |  |  |
| 34 | DistrictRequisitionNumber | varchar(50) | Yes |  |  |
| 35 | HeadingTitle | varchar(255) | Yes |  |  |
| 36 | Keyword | varchar(50) | Yes |  |  |
| 37 | SectionId | int | Yes |  |  |
| 38 | SectionName | varchar(255) | Yes |  |  |
| 39 | OriginalItemId | int | Yes |  |  |
| 40 | HeadingId | int | Yes |  |  |
| 41 | KeywordId | int | Yes |  |  |
| 42 | ItemMustBeBid | int | Yes |  |  |
| 43 | SessionId | int | Yes |  |  |
| 44 | Active | tinyint | Yes |  |  |
| 45 | RTK_MSDSId | int | Yes |  |  |
| 46 | AddedFromAddenda | datetime | Yes |  |  |
| 47 | LastAlteredSessionId | int | Yes |  |  |
| 56 | AdditionalShipping | tinyint | Yes |  |  |
| 57 | CrossRefId | int | Yes |  |  |
| 65 | ShippingCost | decimal(9,2) | Yes |  |  |
| 66 | ShippingQuantity | int | Yes |  |  |
| 67 | ShippingUpdated | datetime | Yes |  |  |
| 70 | PerishableItem | bit | Yes | ((0)) |  |
| 71 | DeliveryDate | date | Yes |  |  |
| 72 | PrescriptionRequired | bit | Yes | ((0)) |  |
| 73 | DoctorsName | varchar(100) | Yes | ('') |  |
| 74 | DEANumber | varchar(9) | Yes | ('') |  |
| 76 | Email | varchar(255) | Yes |  |  |
| 77 | DigitallyDelivered | tinyint | Yes |  |  |
| 78 | DigitallyDeliveredEmail | varchar(255) | Yes |  |  |
| 79 | MinimumOrderQuantity | int | Yes |  |  |

### DetailChangeLog {dbo-detailchangelog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,925,616 |
| **Created** | 2006-08-29 21:49:31.920000 |
| **Modified** | 2024-06-21 21:57:59.453000 |
| **Primary Key** | DetailChangeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailChangeId | int IDENTITY | No |  | PK |
| 2 | DetailId | int | No |  |  |
| 3 | RequisitionId | int | No |  |  |
| 4 | ItemId | int | No |  |  |
| 5 | OrigQty | int | Yes |  |  |
| 6 | NewQty | int | Yes |  |  |
| 7 | OrigBidPrice | money | Yes |  |  |
| 8 | NewBidPrice | money | Yes |  |  |
| 9 | OrigBidItemId | int | Yes |  |  |
| 10 | NewBidItemId | int | Yes |  |  |
| 11 | UserId | int | Yes |  |  |
| 12 | SessionId | int | Yes |  |  |
| 13 | ChangeDate | datetime | Yes |  |  |
| 14 | OrigVendorId | int | Yes |  |  |
| 15 | NewVendorId | int | Yes |  |  |
| 16 | BRChangeLogId | int | Yes |  |  |

### DetailChanges {dbo-detailchanges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 26,502,061 |
| **Created** | 2006-08-29 21:57:46.360000 |
| **Modified** | 2024-06-21 21:58:39.760000 |
| **Primary Key** | DetailChangeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailChangeId | int IDENTITY | No |  | PK |
| 2 | DetailId | int | Yes |  |  |
| 3 | ChangeDate | datetime | Yes |  |  |
| 4 | OrigQty | int | Yes |  |  |
| 5 | NewQty | int | Yes |  |  |
| 6 | RequisitionId | int | Yes |  |  |
| 7 | ItemId | int | Yes |  |  |
| 8 | BidPrice | money | Yes |  |  |
| 9 | BidItemId | int | Yes |  |  |

### DetailHold {dbo-detailhold}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2006-09-16 13:22:47.130000 |
| **Modified** | 2024-06-21 21:58:41.590000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailId | int IDENTITY | No |  |  |
| 2 | RequisitionId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | AddendumItem | tinyint | Yes |  |  |
| 6 | ItemCode | varchar(50) | Yes |  |  |
| 7 | Quantity | int | Yes |  |  |
| 8 | LastYearsQuantity | int | Yes |  |  |
| 9 | Description | varchar(1024) | Yes |  |  |
| 10 | UnitId | int | Yes |  |  |
| 11 | UnitCode | varchar(20) | Yes |  |  |
| 12 | BidPrice | money | Yes |  |  |
| 13 | CatalogPrice | money | Yes |  |  |
| 14 | GrossPrice | money | Yes |  |  |
| 15 | DiscountRate | decimal(9,5) | Yes |  |  |
| 16 | CatalogPage | char(4) | Yes |  |  |
| 17 | PricePlanId | int | Yes |  |  |
| 18 | PriceId | int | Yes |  |  |
| 19 | AwardId | int | Yes |  |  |
| 20 | VendorId | int | Yes |  |  |
| 21 | VendorItemCode | varchar(50) | Yes |  |  |
| 22 | Alternate | varchar(1024) | Yes |  |  |
| 23 | POId | int | Yes |  |  |
| 24 | BatchDetailId | int | Yes |  |  |
| 25 | Modified | datetime | Yes |  |  |
| 26 | ModifiedById | int | Yes |  |  |
| 27 | SourceId | int | Yes |  |  |
| 28 | SortSeq | varchar(64) | Yes |  |  |
| 29 | BidItemId | int | Yes |  |  |
| 30 | ExtraDescription | varchar(1024) | Yes |  |  |
| 31 | ReProc | tinyint | Yes |  |  |
| 32 | UseGrossPrices | tinyint | Yes |  |  |
| 33 | BidHeaderId | int | Yes |  |  |
| 34 | DistrictRequisitionNumber | varchar(50) | Yes |  |  |
| 35 | HeadingTitle | varchar(255) | Yes |  |  |
| 36 | Keyword | varchar(50) | Yes |  |  |
| 37 | SectionId | int | Yes |  |  |
| 38 | SectionName | varchar(255) | Yes |  |  |
| 39 | OriginalItemId | int | Yes |  |  |
| 40 | HeadingId | int | Yes |  |  |
| 41 | KeywordId | int | Yes |  |  |
| 42 | ItemMustBeBid | int | Yes |  |  |
| 43 | SessionId | int | Yes |  |  |
| 44 | Active | tinyint | Yes |  |  |
| 45 | RTK_MSDSId | int | Yes |  |  |

### DetailMatch {dbo-detailmatch}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 103,534 |
| **Created** | 2013-09-13 16:48:26.770000 |
| **Modified** | 2024-06-21 21:58:41.857000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BudgetId | int | Yes |  |  |
| 2 | TotalRequisitionCost | money | Yes |  |  |
| 3 | DetailId | int | No |  |  |
| 4 | RequisitionId | int | Yes |  |  |
| 5 | CatalogId | int | Yes |  |  |
| 6 | ItemId | int | Yes |  |  |
| 7 | AddendumItem | tinyint | Yes |  |  |
| 8 | ItemCode | varchar(50) | Yes |  |  |
| 9 | Quantity | int | Yes |  |  |
| 10 | LastYearsQuantity | int | Yes |  |  |
| 11 | Description | varchar(1024) | Yes |  |  |
| 12 | UnitId | int | Yes |  |  |
| 13 | UnitCode | varchar(20) | Yes |  |  |
| 14 | BidPrice | money | Yes |  |  |
| 15 | CatalogPrice | money | Yes |  |  |
| 16 | GrossPrice | money | Yes |  |  |
| 17 | DiscountRate | decimal(9,5) | Yes |  |  |
| 18 | CatalogPage | char(4) | Yes |  |  |
| 19 | PricePlanId | int | Yes |  |  |
| 20 | PriceId | int | Yes |  |  |
| 21 | AwardId | int | Yes |  |  |
| 22 | VendorId | int | Yes |  |  |
| 23 | VendorItemCode | varchar(50) | Yes |  |  |
| 24 | Alternate | varchar(1024) | Yes |  |  |
| 25 | POId | int | Yes |  |  |
| 26 | BatchDetailId | int | Yes |  |  |
| 27 | Modified | datetime | Yes |  |  |
| 28 | ModifiedById | int | Yes |  |  |
| 29 | SourceId | int | Yes |  |  |
| 30 | SortSeq | varchar(64) | Yes |  |  |
| 31 | BidItemId | int | Yes |  |  |
| 32 | ExtraDescription | varchar(1024) | Yes |  |  |
| 33 | ReProc | tinyint | Yes |  |  |
| 34 | UseGrossPrices | tinyint | Yes |  |  |
| 35 | BidHeaderId | int | Yes |  |  |
| 36 | DistrictRequisitionNumber | varchar(50) | Yes |  |  |
| 37 | HeadingTitle | varchar(255) | Yes |  |  |
| 38 | Keyword | varchar(50) | Yes |  |  |
| 39 | SectionId | int | Yes |  |  |
| 40 | SectionName | varchar(255) | Yes |  |  |
| 41 | OriginalItemId | int | Yes |  |  |
| 42 | HeadingId | int | Yes |  |  |
| 43 | KeywordId | int | Yes |  |  |
| 44 | ItemMustBeBid | int | Yes |  |  |
| 45 | SessionId | int | Yes |  |  |
| 46 | Active | tinyint | Yes |  |  |
| 47 | RTK_MSDSId | int | Yes |  |  |
| 48 | AddedFromAddenda | datetime | Yes |  |  |
| 49 | LastAlteredSessionId | int | Yes |  |  |

### DetailNotifications {dbo-detailnotifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,986,819 |
| **Created** | 2019-11-01 13:11:18.390000 |
| **Modified** | 2026-03-07 09:21:43.333000 |
| **Primary Key** | DetailNotificationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailNotificationId | bigint IDENTITY | No |  | PK |
| 2 | DetailId | bigint | No |  |  |
| 3 | NotificationId | bigint | Yes |  |  |
| 4 | DateCreated | datetime | No | (getdate()) |  |
| 5 | OrigItemId | bigint | Yes |  |  |
| 6 | NewItemId | bigint | Yes |  |  |
| 7 | OrigVendorId | bigint | Yes |  |  |
| 8 | NewVendorId | bigint | Yes |  |  |
| 9 | OrigBidPrice | decimal(11,5) | Yes |  |  |
| 10 | NewBidPrice | decimal(11,5) | Yes |  |  |

### DetailUploads {dbo-detailuploads}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2020-03-09 23:26:31.440000 |
| **Modified** | 2024-06-21 21:59:06.090000 |
| **Primary Key** | DetailUploadId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailUploadId | bigint IDENTITY | No |  | PK |
| 2 | DetailId | bigint | Yes |  |  |
| 3 | Description | varchar(50) | Yes |  |  |
| 4 | ClientFileName | varchar(300) | Yes |  |  |
| 5 | ClientDateTime | datetime2 | Yes |  |  |
| 6 | ClientSize | bigint | Yes |  |  |
| 7 | DateUploaded | datetime2 | No | (getdate()) |  |
| 8 | DocId | uniqueidentifier | Yes | (newid()) |  |
| 9 | DocType | varchar(50) | Yes |  |  |
| 10 | DocData | varbinary(MAX) | Yes |  |  |

### District {dbo-district}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 978 |
| **Created** | 2012-10-17 12:31:04.677000 |
| **Modified** | 2025-10-08 12:40:34.070000 |
| **Primary Key** | DistrictId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictId | int IDENTITY | No |  | PK |
| 2 | DistrictCode | varchar(4) | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | Name | varchar(50) | Yes |  |  |
| 5 | Address1 | varchar(30) | Yes |  |  |
| 6 | Address2 | varchar(30) | Yes |  |  |
| 7 | Address3 | varchar(30) | Yes |  |  |
| 8 | City | varchar(25) | Yes |  |  |
| 9 | State | varchar(2) | Yes |  |  |
| 10 | Zipcode | varchar(10) | Yes |  |  |
| 11 | RequiredApprovalLevel | tinyint | Yes |  |  |
| 12 | POsBySchool | tinyint | Yes |  |  |
| 13 | ReqsBySchool | tinyint | Yes |  |  |
| 14 | SuppressPONumber | tinyint | Yes |  |  |
| 15 | CSRepId | int | Yes |  |  |
| 16 | POConsolidation | char(1) | Yes |  |  |
| 17 | CoopId | int | Yes |  |  |
| 18 | BillingAddressId | int | Yes |  |  |
| 19 | ShippingAddressId | int | Yes |  |  |
| 20 | NextCometId | int | Yes |  |  |
| 21 | PhoneNumber | varchar(20) | Yes |  |  |
| 22 | Fax | varchar(20) | Yes |  |  |
| 23 | EMail | varchar(255) | Yes |  |  |
| 24 | BAName | varchar(50) | Yes |  |  |
| 25 | UseGrossPrices | tinyint | Yes |  |  |
| 26 | POLayoutId | int | Yes |  |  |
| 27 | AccountingFormatId | int | Yes |  |  |
| 28 | TextbookPercentage | decimal(9,5) | Yes |  |  |
| 29 | NoBooklets | tinyint | Yes |  |  |
| 30 | RequireAccounts | tinyint | Yes |  |  |
| 31 | CurrentBudgetOnly | tinyint | Yes |  |  |
| 32 | DistrictTypeId | int | Yes |  |  |
| 33 | AccountSeparator | char(1) | Yes |  |  |
| 34 | EnableLogins | tinyint | Yes |  |  |
| 35 | County | varchar(50) | Yes |  |  |
| 36 | DRsbySchool | int | Yes |  |  |
| 37 | RightToKnow | int | Yes |  |  |
| 38 | RTK | int | Yes |  |  |
| 39 | AllowPasswordChanges | tinyint | Yes |  |  |
| 40 | ScheduleId | int | Yes |  |  |
| 41 | DisableLogins | tinyint | Yes |  |  |
| 42 | LocalPOLayoutId | int | Yes |  |  |
| 43 | POUploadEmail | varchar(255) | Yes |  |  |
| 44 | ContactName | varchar(50) | Yes |  |  |
| 45 | ContactPhone | varchar(20) | Yes |  |  |
| 46 | ParentDistrictId | int | Yes |  |  |
| 47 | NoAdvises | tinyint | Yes |  |  |
| 48 | TimeAndMaterialBids | tinyint | Yes |  |  |
| 49 | MinimumPO | money | Yes | ((25)) |  |
| 50 | AccountingDistrictCode | varchar(50) | Yes |  |  |
| 51 | StateId | int | Yes |  |  |
| 52 | FixedPOMsg | varchar(500) | Yes |  |  |
| 53 | UseEDSVendorCodes | tinyint | Yes |  |  |
| 54 | AccountingSystemOptions | varchar(255) | Yes |  |  |
| 55 | CooperativeBids | tinyint | Yes |  |  |
| 56 | AllowIncidentalOrdering | tinyint | Yes | ((1)) |  |
| 57 | AllowUserMaintenance | tinyint | Yes |  |  |
| 58 | PrintBidAs | tinyint | Yes |  |  |
| 59 | AnnualPOGenerationMethod | varchar(10) | Yes |  |  |
| 60 | IncidentalPOGenerationMethod | varchar(10) | Yes |  |  |
| 61 | SuppressPrintSchedule | tinyint | Yes |  |  |
| 62 | MinimumPOAmount | money | Yes |  |  |
| 69 | EnableRTKOnline | int | Yes |  |  |
| 71 | onlineOrderbook | tinyint | Yes |  |  |
| 77 | AllowElectronicPOs | int | Yes |  |  |
| 79 | NotificationType | int | Yes |  |  |
| 82 | DoNotShipCatalogs | tinyint | Yes |  |  |
| 85 | usesActualPONumber | tinyint | Yes |  |  |
| 87 | HidefromDistrictLists | tinyint | Yes |  |  |
| 88 | AllowSmallPOs | tinyint | Yes |  |  |
| 89 | AllowBringForwardReqs | tinyint | Yes |  |  |

### DistrictCategories {dbo-districtcategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 126,368 |
| **Created** | 2006-08-30 18:37:16.160000 |
| **Modified** | 2025-01-12 19:21:30.263000 |
| **Primary Key** | DistrictCategoryId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictCategoryId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | DistrictId | int | Yes |  |  |
| 5 | Title | varchar(50) | Yes |  |  |
| 6 | Charge | money | Yes |  |  |
| 7 | AllowAddenda | tinyint | Yes |  |  |
| 8 | AllowIncidentals | tinyint | Yes |  |  |
| 9 | OrderBookTypeId | int | Yes |  |  |
| 11 | BidItemsOnly | bit | Yes |  |  |
| 12 | EarlyAccess | tinyint | Yes |  |  |
| 18 | RTKLocation | varchar(50) | Yes |  |  |
| 21 | AllowBudgetBooks | tinyint | Yes |  |  |
| 22 | AllowOrderBooks | tinyint | Yes |  |  |
| 31 | Description | varchar(2048) | Yes |  |  |
| 32 | Priority | tinyint | Yes |  |  |

### DistrictCategoryTitles {dbo-districtcategorytitles}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-30 18:36:33.160000 |
| **Modified** | 2024-06-21 21:59:08.403000 |
| **Primary Key** | DistrictCategoryTitleId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictCategoryTitleId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | Title | varchar(50) | Yes |  |  |

### DistrictCharges {dbo-districtcharges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 22,494 |
| **Created** | 2012-03-20 16:15:05.340000 |
| **Modified** | 2024-06-21 21:59:09.300000 |
| **Primary Key** | DistrictChargeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictChargeId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | Active | int | Yes |  |  |
| 4 | ChargeDate | datetime | Yes |  |  |
| 5 | ChargeTypeId | int | Yes |  |  |
| 6 | Amount | money | Yes |  |  |
| 7 | DateUpdated | datetime | Yes |  |  |
| 8 | Invoiced | datetime | Yes |  |  |
| 9 | Frequency | int | Yes |  |  |
| 10 | Repeats | int | Yes |  |  |
| 11 | FrequencyData | varchar(50) | Yes |  |  |
| 12 | BudgetId | int | Yes |  |  |
| 13 | Comments | varchar(512) | Yes |  |  |

### DistrictChargesNotes {dbo-districtchargesnotes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-10-09 12:26:14.870000 |
| **Modified** | 2024-06-21 21:59:09.463000 |
| **Primary Key** | DistrictChargeNoteId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictChargeNoteId | uniqueidentifier | No | (newid()) | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | BudgetId | int | No |  |  |
| 4 | NoteDate | datetime | No | (getdate()) |  |
| 5 | Comments | varchar(4096) | Yes |  |  |

### DistrictContacts {dbo-districtcontacts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3,838 |
| **Created** | 2011-08-29 13:40:06.843000 |
| **Modified** | 2024-06-21 21:59:09.850000 |
| **Primary Key** | DistrictContactId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictContactId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | DistrictContactTypeId | int | No |  |  |
| 4 | SalutationId | int | Yes |  |  |
| 5 | FirstName | varchar(50) | Yes |  |  |
| 6 | MiddleName | varchar(50) | Yes |  |  |
| 7 | LastName | varchar(50) | Yes |  |  |
| 8 | Suffix | varchar(20) | Yes |  |  |
| 9 | Phone | varchar(20) | Yes |  |  |
| 10 | Fax | varchar(20) | Yes |  |  |
| 11 | eMail | varchar(255) | Yes |  |  |
| 12 | ShippingId | int | Yes |  |  |
| 13 | Address1 | varchar(50) | Yes |  |  |
| 14 | Address2 | varchar(50) | Yes |  |  |
| 15 | City | varchar(50) | Yes |  |  |
| 16 | State | char(2) | Yes |  |  |
| 17 | Zipcode | varchar(10) | Yes |  |  |
| 18 | FullName | varchar(174) | Yes |  |  |

### DistrictContactTypes {dbo-districtcontacttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 7 |
| **Created** | 2011-07-12 12:35:43.070000 |
| **Modified** | 2024-06-21 21:59:10.013000 |
| **Primary Key** | DistrictContactTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictContactTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |

### DistrictContinuances {dbo-districtcontinuances}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14,460 |
| **Created** | 2017-10-30 21:37:50.730000 |
| **Modified** | 2024-06-21 21:59:10.237000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | BudgetId | int | No |  |  |
| 4 | Email | varchar(255) | Yes |  |  |
| 5 | Status | char(1) | Yes | ('P') |  |
| 6 | SignedBy | varchar(255) | Yes |  |  |
| 7 | Comments | varchar(4096) | Yes |  |  |
| 8 | Sent | datetime | No | (getdate()) |  |
| 9 | Received | datetime | Yes |  |  |
| 11 | SavingsBudgetId | int | Yes |  |  |

### DistrictNotes {dbo-districtnotes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 76 |
| **Created** | 2007-07-11 15:05:17.043000 |
| **Modified** | 2024-06-21 21:59:10.483000 |
| **Primary Key** | DistrictNotesId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictNotesId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | NoteTitle | varchar(80) | Yes |  |  |
| 4 | NoteType | char(1) | Yes |  |  |
| 5 | Note | varchar(4000) | Yes |  |  |
| 6 | DateOfNote | datetime | Yes |  |  |

### DistrictNoteType {dbo-districtnotetype}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3 |
| **Created** | 2026-03-05 19:01:55.987000 |
| **Modified** | 2026-03-05 19:01:55.987000 |
| **Primary Key** | DistrictNoteTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictNoteTypeId | char(1) | No |  | PK |
| 2 | NoteTypeName | varchar(80) | Yes |  |  |

### DistrictNotifications {dbo-districtnotifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,077 |
| **Created** | 2016-08-16 23:40:07.163000 |
| **Modified** | 2024-06-21 21:59:10.690000 |
| **Primary Key** | DistrictNotificationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictNotificationId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | NotificationType | varchar(50) | No |  |  |
| 4 | CategoryId | int | Yes |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | Method | varchar(50) | Yes |  |  |
| 7 | NotifyList | varchar(255) | Yes |  |  |
| 8 | OtherNotify | varchar(4096) | Yes |  |  |
| 9 | Modified | datetime | Yes | (getdate()) |  |

### DistrictPP {dbo-districtpp}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9,297 |
| **Created** | 2006-08-30 18:36:02.833000 |
| **Modified** | 2024-06-21 22:41:21.153000 |
| **Primary Key** | DistrictPPId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictPPId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | PricePlanId | int | Yes |  | FK → dbo.PricePlans.PricePlanId |

### DistrictProposedCharges {dbo-districtproposedcharges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12,015 |
| **Created** | 2016-01-08 13:20:04.633000 |
| **Modified** | 2024-06-21 21:59:11.270000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) |  |
| 2 | DistrictId | int | No |  |  |
| 3 | BudgetId | int | No |  |  |
| 4 | ChargeTypeId | int | No |  |  |
| 5 | DateUpdated | datetime | Yes |  |  |
| 6 | DateApplied | datetime | Yes |  |  |
| 7 | Amount | money | Yes |  |  |
| 8 | PreviousAmount | money | Yes |  |  |
| 9 | PreviousBudgetId | int | Yes |  |  |
| 10 | ChangePercentage | decimal(11,5) | Yes |  |  |
| 11 | Action | char(1) | Yes |  |  |
| 12 | Frequency | int | Yes |  |  |
| 13 | FrequencyData | varchar(50) | Yes |  |  |

### DistrictReports {dbo-districtreports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11 |
| **Created** | 2013-03-19 22:56:08.777000 |
| **Modified** | 2024-06-21 21:59:11.437000 |
| **Primary Key** | DistrictReportId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictReportId | int IDENTITY | No |  | PK |
| 2 | Level | int | Yes |  |  |
| 3 | Group | varchar(50) | Yes |  |  |
| 4 | ReportName | varchar(50) | No |  |  |
| 5 | ScriptURL | varchar(1024) | Yes |  |  |

### DistrictTypes {dbo-districttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6 |
| **Created** | 2006-08-29 22:33:04.433000 |
| **Modified** | 2024-06-21 21:59:11.837000 |
| **Primary Key** | DistrictTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(64) | Yes |  |  |
| 3 | UsesOnline | tinyint | Yes |  |  |
| 4 | UsesBooklet | tinyint | Yes |  |  |
| 5 | UsePriorYearReqs | tinyint | Yes |  |  |
| 6 | VerifySBSOnline | tinyint | Yes |  |  |

### DistrictVendor {dbo-districtvendor}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 316,186 |
| **Created** | 2006-08-30 18:33:26.960000 |
| **Modified** | 2026-03-07 09:21:44.177000 |
| **Primary Key** | DistrictVendorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictVendorId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | DistrictId | int | Yes |  | FK → dbo.District.DistrictId |
| 4 | VendorId | int | Yes |  | FK → dbo.Vendors.VendorId |
| 5 | Value | varchar(20) | Yes |  |  |
| 6 | VendorsAccountCode | varchar(50) | Yes |  |  |

### DMSBidDocuments {dbo-dmsbiddocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 29,163 |
| **Created** | 2018-05-01 22:07:53.010000 |
| **Modified** | 2026-03-07 09:21:44.367000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidNbr | varchar(MAX) | Yes |  |  |
| 4 | DocType | varchar(MAX) | Yes |  |  |
| 5 | DocId | uniqueidentifier | Yes |  |  |
| 6 | DistrictVisible | varchar(MAX) | Yes |  |  |
| 7 | PagesCaptured | int | Yes |  |  |
| 9 | FileName | varchar(1024) | Yes |  |  |

### DMSSDSDocuments {dbo-dmssdsdocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 602 |
| **Created** | 2019-02-06 14:40:08.157000 |
| **Modified** | 2024-06-21 21:59:12.140000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | MSDSId | int | No |  |  |
| 3 | DocId | uniqueidentifier | No |  |  |
| 4 | PagesCaptured | int | Yes |  |  |
| 5 | DocName | varchar(1024) | Yes |  |  |

### DMSVendorBidDocuments {dbo-dmsvendorbiddocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 746,082 |
| **Created** | 2020-10-20 02:53:52.827000 |
| **Modified** | 2026-03-27 00:17:10.970000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | VendorCode | varchar(10) | Yes |  |  |
| 3 | DistrictVisible | varchar(10) | Yes |  |  |
| 4 | BidHeaderId | int | Yes |  |  |
| 5 | BidNbr | varchar(20) | Yes |  |  |
| 6 | DocType | varchar(255) | Yes |  |  |
| 7 | ExpirationDate | varchar(30) | Yes |  |  |
| 8 | DocumentNumber | varchar(255) | Yes |  |  |
| 9 | DocId | uniqueidentifier | Yes |  |  |
| 10 | PagesCaptured | int | Yes |  |  |
| 11 | FileName | varchar(1024) | Yes |  |  |

### DMSVendorDocuments {dbo-dmsvendordocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,485 |
| **Created** | 2020-10-20 02:53:30.450000 |
| **Modified** | 2026-03-27 00:17:12.127000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | VendorCode | varchar(10) | Yes |  |  |
| 3 | DistrictVisible | varchar(10) | Yes |  |  |
| 4 | DocType | varchar(255) | Yes |  |  |
| 5 | ExpirationDate | varchar(30) | Yes |  |  |
| 6 | DocumentNumber | varchar(255) | Yes |  |  |
| 7 | DocId | uniqueidentifier | Yes |  |  |
| 8 | PagesCaptured | int | Yes |  |  |
| 9 | FileName | varchar(1024) | Yes |  |  |

### dtproperties {dbo-dtproperties}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 42 |
| **Created** | 2001-08-27 16:22:54.930000 |
| **Modified** | 2001-08-27 16:22:54.930000 |
| **Primary Key** | id, property |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | id | int IDENTITY | No |  | PK |
| 2 | objectid | int | Yes |  |  |
| 3 | property | varchar(64) | No |  | PK |
| 4 | value | varchar(255) | Yes |  |  |
| 5 | uvalue | nvarchar(255) | Yes |  |  |
| 6 | lvalue | image | Yes |  |  |
| 7 | version | int | No | (0) |  |

### EmailBlast {dbo-emailblast}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 17,497 |
| **Created** | 2017-03-04 18:57:20.393000 |
| **Modified** | 2024-06-21 21:59:35.907000 |
| **Primary Key** | EmailBlastId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | EmailBlastId | int IDENTITY | No |  | PK |
| 2 | BlastName | varchar(100) | Yes |  |  |
| 3 | BlastDescription | varchar(2000) | Yes |  |  |
| 4 | BlastHTML | varchar(8000) | Yes |  |  |
| 5 | SQLStmt | varchar(8000) | Yes |  |  |
| 6 | ReportWhereClause | varchar(8000) | Yes |  |  |
| 7 | SentDate | datetime | Yes |  |  |
| 8 | EmailFrom | varchar(500) | Yes |  |  |
| 9 | EmailCC | varchar(500) | Yes |  |  |
| 10 | EmailBCC | varchar(500) | Yes |  |  |
| 11 | EmailSubject | varchar(250) | Yes |  |  |
| 12 | ReadReceipt | tinyint | Yes |  |  |
| 13 | HighPriority | tinyint | Yes |  |  |
| 14 | AddressFromRep | tinyint | Yes |  |  |
| 15 | Attachments | varchar(2000) | Yes |  |  |
| 16 | UseDefaultReadReceiptEmail | tinyint | Yes |  |  |
| 17 | ReadReceiptEmail | varchar(500) | Yes |  |  |
| 18 | BlastVar1 | varchar(250) | Yes |  |  |
| 19 | BlastVar2 | varchar(250) | Yes |  |  |
| 21 | Reference1Id | int | Yes |  |  |
| 22 | Reference2Id | int | Yes |  |  |
| 24 | VarDataSQL | varchar(8000) | Yes |  |  |

### EmailBlastAddresses08132012 {dbo-emailblastaddresses08132012}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 271 |
| **Created** | 2012-08-15 18:00:15.710000 |
| **Modified** | 2021-11-08 21:28:49.073000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | EmailAddress | nvarchar(255) | Yes |  |  |

### EmailBlastCopy {dbo-emailblastcopy}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3 |
| **Created** | 2012-05-04 17:07:31.007000 |
| **Modified** | 2021-11-08 21:28:49.097000 |
| **Primary Key** | EmailBlastId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | EmailBlastId | int IDENTITY | No |  | PK |
| 2 | BlastName | varchar(50) | Yes |  |  |
| 3 | BlastDescription | varchar(2000) | Yes |  |  |
| 4 | BlastHTML | varchar(MAX) | Yes |  |  |
| 5 | SQLStmt | varchar(8000) | Yes |  |  |
| 6 | ReportWhereClause | varchar(8000) | Yes |  |  |
| 7 | SentDate | datetime | Yes |  |  |
| 8 | EmailFrom | varchar(500) | Yes |  |  |
| 9 | EmailCC | varchar(500) | Yes |  |  |
| 10 | EmailBCC | varchar(500) | Yes |  |  |
| 11 | EmailSubject | varchar(80) | Yes |  |  |
| 12 | ReadReceipt | tinyint | Yes |  |  |
| 13 | HighPriority | tinyint | Yes |  |  |
| 14 | AddressFromRep | tinyint | Yes |  |  |
| 15 | Attachments | varchar(2000) | Yes |  |  |
| 16 | UseDefaultReadReceiptEmail | tinyint | Yes |  |  |
| 17 | ReadReceiptEmail | varchar(500) | Yes |  |  |

### EmailBlastLog {dbo-emailblastlog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,502,305 |
| **Created** | 2012-04-27 18:45:43.840000 |
| **Modified** | 2024-06-21 22:01:52.413000 |
| **Primary Key** | EmailBlastLogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | EmailBlastLogId | int IDENTITY | No |  | PK |
| 2 | EmailBlastId | int | Yes |  |  |
| 3 | PrimaryRecipient | varchar(50) | Yes |  |  |
| 4 | ContactFullName | varchar(100) | Yes |  |  |
| 5 | EmailSentTo | varchar(500) | Yes |  |  |
| 6 | EmailFrom | varchar(500) | Yes |  |  |
| 7 | EmailCC | varchar(500) | Yes |  |  |
| 8 | EmailBCC | varchar(500) | Yes |  |  |
| 9 | SendDate | datetime | Yes |  |  |
| 10 | XMLData | varchar(8000) | Yes |  |  |
| 11 | Attachment | varchar(1000) | Yes |  |  |
| 18 | PrimaryRecipientId | int | Yes |  |  |

### FreezeItems {dbo-freezeitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 15,435 |
| **Created** | 2016-03-21 22:31:32.233000 |
| **Modified** | 2024-06-21 22:01:53.743000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | ItemId | int | No |  |  |
| 3 | CrossRefId | int | No |  |  |
| 4 | VendorId | int | No |  |  |
| 5 | VendorItemCode | varchar(50) | Yes |  |  |
| 6 | BidHeaderId | int | No |  |  |
| 7 | GrossPrice | money | Yes |  |  |

### FreezeItems2015 {dbo-freezeitems2015}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 105,203 |
| **Created** | 2015-05-08 20:34:17.010000 |
| **Modified** | 2024-06-21 21:57:16.640000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DistrictName | varchar(50) | Yes |  |  |
| 2 | BudgetName | varchar(30) | Yes |  |  |
| 3 | SchoolName | varchar(50) | Yes |  |  |
| 4 | CometId | int | Yes |  |  |
| 5 | Attention | varchar(50) | Yes |  |  |
| 6 | RequisitionNumber | varchar(24) | Yes |  |  |
| 7 | ItemCode | varchar(50) | Yes |  |  |
| 8 | VendorItemCode | varchar(50) | Yes |  |  |
| 9 | Quantity | int | Yes |  |  |
| 10 | BidPrice | money | Yes |  |  |
| 11 | Extended | money | Yes |  |  |
| 12 | OrigVendorItemCode | varchar(50) | Yes |  |  |
| 13 | OrigBidPrice | money | Yes |  |  |
| 14 | OrigExtended | money | Yes |  |  |
| 15 | Description | varchar(1024) | Yes |  |  |
| 16 | Status | varchar(255) | Yes |  |  |
| 17 | UseAllocations | tinyint | No |  |  |
| 18 | AllocationAvailable | money | No |  |  |
| 19 | DetailId | int | No |  |  |
| 20 | RequisitionId | int | No |  |  |
| 21 | VendorId | int | Yes |  |  |
| 22 | AwardId | int | Yes |  |  |
| 23 | CatalogId | int | Yes |  |  |
| 24 | CatalogPrice | money | Yes |  |  |
| 25 | OrigVendorId | int | Yes |  |  |
| 26 | OrigAwardId | int | Yes |  |  |
| 27 | OrigCatalogId | int | Yes |  |  |
| 28 | OrigCatalogPrice | money | Yes |  |  |

### HeaderWorkItems {dbo-headerworkitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 491,824 |
| **Created** | 2017-09-21 16:34:34.740000 |
| **Modified** | 2021-11-08 21:28:49.343000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OBDWorkId | int IDENTITY | No |  |  |
| 2 | ItemId | int | No |  |  |

### Headings {dbo-headings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 305,714 |
| **Created** | 2006-08-30 18:32:27.083000 |
| **Modified** | 2026-03-07 09:22:20.950000 |
| **Primary Key** | HeadingId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | HeadingId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | Code | varchar(16) | Yes |  |  |
| 5 | ExpandAll | tinyint | Yes |  |  |
| 6 | Title | varchar(255) | Yes |  |  |
| 7 | Description | varchar(4096) | Yes |  |  |
| 8 | DistrictId | int | Yes |  |  |
| 20 | DateCreated | datetime | Yes | (getdate()) |  |
| 21 | DateUpdated | datetime | Yes |  |  |

### HolidayCalendar {dbo-holidaycalendar}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 29 |
| **Created** | 2024-02-06 15:19:21.080000 |
| **Modified** | 2024-02-06 15:19:21.127000 |
| **Primary Key** | Year, Month |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Year | int | No |  | PK |
| 2 | Month | int | No |  | PK |
| 3 | Holidays | varchar(100) | Yes | ('') |  |

### HolidayCalendarVendor {dbo-holidaycalendarvendor}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 7 |
| **Created** | 2024-02-06 15:19:21.173000 |
| **Modified** | 2024-02-06 15:19:21.277000 |
| **Primary Key** | Year, Month, VendorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Year | int | No |  | PK |
| 2 | Month | int | No |  | PK |
| 3 | Holidays | varchar(100) | Yes | ('') |  |
| 4 | VendorId | int | No | ((0)) | PK |

### ImageErrors {dbo-imageerrors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 26,727 |
| **Created** | 2021-05-03 22:02:21.247000 |
| **Modified** | 2025-03-21 09:44:35.430000 |
| **Primary Key** | imageErrorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | imageErrorId | bigint IDENTITY | No |  | PK |
| 2 | imageURL | varchar(2048) | No |  |  |
| 3 | error | varchar(MAX) | Yes |  |  |
| 4 | logDate | datetime | No | (getdate()) |  |

### ImageLog {dbo-imagelog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,788,706 |
| **Created** | 2021-05-03 22:02:20.370000 |
| **Modified** | 2025-03-21 09:18:57.293000 |
| **Primary Key** | imageLogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | imageLogId | bigint IDENTITY | No |  | PK |
| 2 | imageId | bigint | Yes |  |  |
| 3 | imageURL | varchar(2048) | Yes |  |  |
| 4 | imageActualURL | varchar(2048) | Yes |  |  |
| 5 | statusCode | int | Yes |  |  |
| 6 | statusText | varchar(512) | Yes |  |  |
| 7 | contentType | varchar(50) | Yes |  |  |
| 8 | headers | varchar(MAX) | Yes |  |  |
| 9 | testDate | datetime | Yes | (getdate()) |  |
| 10 | writeStatus | int | Yes |  |  |
| 11 | writeDate | datetime | Yes |  |  |

### Images {dbo-images}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,736,177 |
| **Created** | 2021-07-09 10:00:09.433000 |
| **Modified** | 2025-03-22 05:15:23.670000 |
| **Primary Key** | imageId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | imageId | bigint IDENTITY | No |  | PK |
| 2 | imageURL | varchar(768) | Yes |  |  |
| 3 | imageActualURL | varchar(768) | Yes |  |  |
| 4 | imagePath | varchar(512) | Yes |  |  |
| 5 | imageResized | varchar(512) | Yes |  |  |
| 6 | imageThumbnail | varchar(512) | Yes |  |  |
| 7 | pHash | char(64) | Yes |  |  |
| 8 | bipHash | bigint | Yes |  |  |
| 9 | imageSize | int | Yes |  |  |
| 10 | imageFormat | varchar(20) | Yes |  |  |
| 11 | width | int | Yes |  |  |
| 12 | height | int | Yes |  |  |
| 13 | imageSpace | varchar(20) | Yes |  |  |
| 14 | channels | int | Yes |  |  |
| 15 | depth | varchar(20) | Yes |  |  |
| 16 | density | int | Yes |  |  |
| 17 | dateLoaded | datetime | Yes | (getdate()) |  |
| 18 | dateChecked | datetime | Yes | (getdate()) |  |
| 19 | dateDeleted | datetime | Yes |  |  |

### ImportCatalogDetail {dbo-importcatalogdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 18,596 |
| **Created** | 2017-02-15 23:26:30.063000 |
| **Modified** | 2024-06-21 22:03:03.357000 |
| **Primary Key** | ImportCatalogDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ImportCatalogDetailId | int IDENTITY | No |  | PK |
| 2 | ImportCatalogHeaderId | int | Yes |  |  |
| 3 | ImportInfoType | int | Yes |  |  |
| 4 | ImportInfoDesc | varchar(1000) | Yes |  |  |
| 5 | ImportInfoValue | int | Yes |  |  |
| 6 | ImportDateTime | datetime | Yes |  |  |

### ImportCatalogHeader {dbo-importcatalogheader}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,975 |
| **Created** | 2017-02-07 18:47:42.690000 |
| **Modified** | 2024-06-21 22:03:03.850000 |
| **Primary Key** | ImportCatalogHeaderId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ImportCatalogHeaderId | int IDENTITY | No |  | PK |
| 2 | CatalogId | int | Yes |  |  |
| 3 | ImportDateStart | datetime | Yes |  |  |
| 4 | ImportDateComplete | datetime | Yes |  |  |

### ImportDetail {dbo-importdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 882,935 |
| **Created** | 2006-08-29 22:34:21.853000 |
| **Modified** | 2024-06-21 22:03:05.827000 |
| **Primary Key** | ImportDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ImportDetailId | int IDENTITY | No |  | PK |
| 2 | ImportId | int | Yes |  |  |
| 3 | ImportData | varchar(512) | Yes |  |  |

### ImportMessages {dbo-importmessages}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,500 |
| **Created** | 2006-08-29 22:35:08.790000 |
| **Modified** | 2024-06-21 22:03:09.097000 |
| **Primary Key** | MessageId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MessageId | int IDENTITY | No |  | PK |
| 2 | ProcessId | int | No |  |  |
| 3 | MsgDate | datetime | Yes |  |  |
| 4 | Message | varchar(512) | Yes |  |  |

### ImportProcesses {dbo-importprocesses}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 754 |
| **Created** | 2006-08-30 18:31:18.943000 |
| **Modified** | 2024-06-21 22:03:09.333000 |
| **Primary Key** | ProcessId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ProcessId | int IDENTITY | No |  | PK |
| 2 | ImportId | int | No |  |  |
| 3 | ProcessDate | datetime | Yes |  |  |

### Imports {dbo-imports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 301 |
| **Created** | 2006-08-29 22:35:38.277000 |
| **Modified** | 2024-06-21 22:03:09.817000 |
| **Primary Key** | ImportId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ImportId | int IDENTITY | No |  | PK |
| 2 | ImportType | tinyint | Yes |  |  |
| 3 | ImportDate | datetime | Yes |  |  |
| 4 | Comments | varchar(255) | Yes |  |  |
| 5 | Records | int | Yes |  |  |
| 6 | ErrorCount | int | Yes |  |  |
| 7 | CategoryId | int | Yes |  |  |
| 8 | CatalogId1 | int | Yes |  |  |
| 9 | CatalogId2 | int | Yes |  |  |
| 10 | CatalogId3 | int | Yes |  |  |
| 11 | CatalogId4 | int | Yes |  |  |
| 12 | CatalogId5 | int | Yes |  |  |
| 13 | CatalogId6 | int | Yes |  |  |
| 14 | PricePlanId | int | Yes |  |  |

### InstructionBookContents {dbo-instructionbookcontents}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 31 |
| **Created** | 2009-10-28 15:32:22.320000 |
| **Modified** | 2024-06-21 22:03:09.953000 |
| **Primary Key** | IBCId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | IBCId | int IDENTITY | No |  | PK |
| 2 | IBTypeId | int | No |  |  |
| 3 | DistrictId | int | Yes |  |  |
| 4 | Priority | int | Yes |  |  |
| 5 | Title | varchar(255) | Yes |  |  |
| 6 | TitleInTOC | tinyint | Yes |  |  |
| 7 | Body | varchar(4096) | Yes |  |  |
| 9 | HeaderAttributes | int | Yes |  |  |
| 10 | HTMLBody | varchar(MAX) | Yes |  |  |
| 11 | SubReportName | varchar(1024) | Yes |  |  |

### InstructionBookTypes {dbo-instructionbooktypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6 |
| **Created** | 2009-10-27 13:49:57.433000 |
| **Modified** | 2024-06-21 22:03:10.127000 |
| **Primary Key** | IBTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | IBTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |
| 3 | ShowInAllBooks | tinyint | Yes |  |  |

### Instructions {dbo-instructions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 7 |
| **Created** | 2013-03-07 21:10:41.293000 |
| **Modified** | 2024-06-21 22:03:10.390000 |
| **Primary Key** | InstructionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | InstructionId | int IDENTITY | No |  | PK |
| 2 | SectionName | varchar(50) | Yes |  |  |
| 3 | Heading | varchar(255) | Yes |  |  |
| 4 | Body | varchar(8000) | Yes |  |  |

### Invoices {dbo-invoices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:35:50.073000 |
| **Modified** | 2024-06-21 22:03:10.637000 |
| **Primary Key** | InvoiceId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | InvoiceId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | InvoiceTypeId | int | No |  |  |
| 4 | InvoiceDate | datetime | No |  |  |
| 5 | DueDate | datetime | Yes |  |  |
| 6 | Amount | money | Yes |  |  |
| 7 | Comments | varchar(4096) | Yes |  |  |

### InvoiceTypes {dbo-invoicetypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:35:59.980000 |
| **Modified** | 2024-06-21 22:03:11.197000 |
| **Primary Key** | InvoiceTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | InvoiceTypeId | int IDENTITY | No |  | PK |
| 2 | Frequency | int | Yes |  |  |
| 3 | DueDays | int | Yes |  |  |
| 4 | Description | varchar(50) | No |  |  |

### IPQueue {dbo-ipqueue}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,046 |
| **Created** | 2012-12-18 13:08:44.400000 |
| **Modified** | 2024-06-21 22:03:11.750000 |
| **Primary Key** | IPQueueId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | IPQueueId | int IDENTITY | No |  | PK |
| 2 | Queue | varchar(50) | No |  |  |
| 3 | Email | varchar(255) | Yes |  |  |
| 4 | SingleFile | tinyint | Yes |  |  |
| 5 | ToUser | tinyint | Yes |  |  |
| 6 | Requested | datetime | No | (getdate()) |  |
| 7 | Started | datetime | Yes |  |  |
| 8 | Completed | datetime | Yes |  |  |
| 9 | Status | varchar(255) | Yes |  |  |

### IPQueueUsers {dbo-ipqueueusers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 489,930 |
| **Created** | 2012-12-18 13:08:23.960000 |
| **Modified** | 2024-06-21 22:03:28.930000 |
| **Primary Key** | IPQueueUserId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | IPQueueUserId | int IDENTITY | No |  | PK |
| 2 | IPQueueId | int | No |  |  |
| 3 | UserId | int | No |  |  |
| 4 | Requested | datetime | No | (getdate()) |  |
| 5 | Started | datetime | Yes |  |  |
| 6 | Completed | datetime | Yes |  |  |
| 7 | Status | varchar(255) | Yes |  |  |

### ItemContractPrices {dbo-itemcontractprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-12-03 12:05:06.247000 |
| **Modified** | 2021-11-08 21:28:49.373000 |
| **Primary Key** | ICPId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ICPId | int IDENTITY | No |  | PK |
| 2 | ItemId | int | No |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | CrossRefId | int | Yes |  |  |
| 5 | Price | money | Yes |  |  |

### ItemDocuments {dbo-itemdocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2019-07-22 15:23:32.920000 |
| **Modified** | 2024-06-21 22:27:30.200000 |
| **Primary Key** | ItemDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemDocumentId | bigint IDENTITY | No |  | PK |
| 2 | ItemId | int | No |  |  |
| 3 | Description | varchar(255) | Yes |  |  |
| 4 | FileName | varchar(255) | Yes |  |  |
| 5 | DocumentType | varchar(10) | Yes |  |  |
| 6 | DocumentSize | bigint | Yes |  |  |
| 7 | DocumentDate | datetime | Yes |  |  |
| 8 | DateUploaded | datetime | No | (getdate()) |  |
| 9 | DocumentId | uniqueidentifier | No | (newid()) |  |
| 10 | DocumentData | varbinary(MAX) | Yes |  |  |

### Items {dbo-items}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 43,457,543 |
| **Created** | 2006-08-29 22:36:35.917000 |
| **Modified** | 2026-03-07 09:56:31.560000 |
| **Primary Key** | ItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | ItemCode | varchar(50) | Yes |  |  |
| 5 | Description | varchar(512) | Yes |  |  |
| 6 | UnitId | int | Yes |  |  |
| 7 | ParentCatalogId | int | Yes |  |  |
| 8 | HeadingId | int | Yes |  |  |
| 9 | RTK | tinyint | Yes |  |  |
| 10 | SortSeq | varchar(64) | Yes |  |  |
| 11 | EditionId | int | Yes |  |  |
| 12 | CopyrightYear | int | Yes |  |  |
| 13 | PackedCode | varchar(50) | Yes | ('([dbo].[uf_PackCode]([ItemCode]))') |  |
| 14 | DateDeactivated | datetime | Yes |  |  |
| 15 | DistrictId | int | Yes |  |  |
| 16 | BrandName | varchar(50) | Yes |  |  |
| 17 | ManufacturorNumber | varchar(50) | Yes |  |  |
| 18 | VendorId | int | Yes |  |  |
| 19 | VendorPartNumber | varchar(50) | Yes |  |  |
| 20 | ItemsPerUnit | varchar(50) | Yes |  |  |
| 21 | ListPrice | money | Yes |  |  |
| 22 | ExtraDetail | varchar(1024) | Yes |  |  |
| 23 | ShortDescription | varchar(60) | Yes |  |  |
| 24 | KeywordId | int | Yes |  |  |
| 25 | AlternateItemCode | varchar(50) | Yes |  |  |
| 26 | SectionId | int | Yes |  |  |
| 27 | UOMDivisor | int | Yes |  |  |
| 28 | RedirectedItemId | int | Yes |  |  |
| 29 | ListPriceSource | int | Yes |  |  |
| 30 | FullDescription | varchar(1536) | Yes |  |  |
| 31 | CrossRefText | varchar(768) | Yes |  |  |
| 33 | StandardItem | tinyint | Yes |  |  |
| 34 | BidderToSupplyVendor | tinyint | Yes |  |  |
| 35 | BidderToSupplyVendorPartNbr | tinyint | Yes |  |  |
| 36 | ManufacturerId | int | Yes |  |  |
| 37 | VendorToSupplyManufacturer | tinyint | Yes |  |  |
| 52 | ProductLineId | int | Yes |  |  |
| 56 | HeadingKeywordId | bigint | Yes |  |  |

### ItemUpdates {dbo-itemupdates}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 198,886 |
| **Created** | 2006-08-30 18:20:57.300000 |
| **Modified** | 2021-11-08 21:28:49.407000 |
| **Primary Key** | ItemUpdateId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemUpdateId | int IDENTITY | No |  | PK |
| 2 | ItemId | int | Yes |  |  |
| 3 | Reason | varchar(50) | Yes |  |  |
| 4 | UpdateField | varchar(50) | Yes |  |  |
| 5 | Action | int | Yes |  |  |

### jSessions {dbo-jsessions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-01-22 14:02:02.473000 |
| **Modified** | 2021-11-08 06:59:30.497000 |
| **Primary Key** | jSessionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | jSessionId | int IDENTITY | No |  | PK |
| 2 | SessionId | int | No |  |  |
| 3 | jSession | varchar(255) | No |  |  |
| 4 | StartTime | datetime | No | (getdate()) |  |
| 5 | EndTime | datetime | Yes |  |  |
| 6 | IPAddress | varchar(50) | Yes |  |  |

### Keywords {dbo-keywords}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 25,263 |
| **Created** | 2006-08-30 18:20:34.910000 |
| **Modified** | 2024-06-21 22:32:26.780000 |
| **Primary Key** | KeywordId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | KeywordId | int IDENTITY | No |  | PK |
| 2 | Active | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | HeadingId | int | Yes |  |  |
| 5 | DistrictId | int | Yes |  |  |
| 6 | Keyword | varchar(50) | Yes |  |  |
| 18 | DateCreated | datetime | Yes | (getdate()) |  |
| 19 | DateUpdated | datetime | Yes |  |  |

### Ledger {dbo-ledger}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:40:00.167000 |
| **Modified** | 2024-06-21 22:32:26.983000 |
| **Primary Key** | LedgerId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | LedgerId | int IDENTITY | No |  | PK |
| 2 | TransactionTypeId | int | No |  |  |
| 3 | Amount | money | Yes |  |  |
| 4 | TransactionDate | datetime | No |  |  |
| 5 | DueDate | datetime | Yes |  |  |
| 6 | DatePosted | datetime | No |  |  |
| 7 | PostedBy | int | Yes |  |  |
| 8 | DistrictId | int | Yes |  |  |
| 9 | Credit | tinyint | Yes |  |  |
| 10 | Comment | varchar(4096) | Yes |  |  |

### LL_RepArea {dbo-ll-reparea}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2019-10-18 12:35:42.940000 |
| **Modified** | 2019-10-18 12:35:42.940000 |
| **Primary Key** | Ref |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Ref | int | No |  | PK |
| 2 | ReportType | varchar(50) | Yes |  |  |
| 3 | TemplateType | varchar(1) | Yes |  |  |

### LL_RepLay {dbo-ll-replay}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2019-10-18 12:37:23.583000 |
| **Modified** | 2019-10-18 12:37:23.583000 |
| **Primary Key** | Ref |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Ref | int | No |  | PK |
| 2 | Description | varchar(60) | Yes |  |  |
| 3 | AreaRef | int | Yes |  |  |
| 4 | FileName | varchar(80) | Yes |  |  |
| 5 | FactoryDefault | tinyint | Yes |  |  |
| 6 | Type | varchar(5) | Yes |  |  |

### ManufacturerProductLines {dbo-manufacturerproductlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14,298 |
| **Created** | 2015-12-21 00:50:14.020000 |
| **Modified** | 2024-06-21 22:32:27.570000 |
| **Primary Key** | ManufacturerProductLineId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ManufacturerProductLineId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | ManufacturerId | int | No |  |  |
| 4 | Name | varchar(100) | No |  |  |
| 5 | UseOptions | tinyint | Yes |  |  |

### Manufacturers {dbo-manufacturers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9,007 |
| **Created** | 2012-11-14 11:55:40.303000 |
| **Modified** | 2024-06-21 22:32:27.767000 |
| **Primary Key** | ManufacturerId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ManufacturerId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | No |  |  |
| 4 | Name | varchar(100) | No |  |  |
| 5 | WebsiteLink | varchar(255) | Yes |  |  |
| 6 | AllowAdditionalProductLines | tinyint | Yes |  |  |
| 7 | UseOptions | tinyint | Yes |  |  |

### MappedItems {dbo-mappeditems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2014-02-26 11:19:20.140000 |
| **Modified** | 2024-06-21 22:32:28.220000 |
| **Primary Key** | MappedItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MappedItemId | int IDENTITY | No |  | PK |
| 2 | OrigItemId | int | No |  |  |
| 3 | NewItemId | int | No |  |  |
| 4 | MapDate | datetime | No | (getdate()) |  |

### Menus {dbo-menus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4 |
| **Created** | 2009-09-10 12:37:17.297000 |
| **Modified** | 2024-06-21 22:32:28.447000 |
| **Primary Key** | MenuId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MenuId | int IDENTITY | No |  | PK |
| 2 | ParentId | int | Yes |  |  |
| 3 | Name | varchar(50) | Yes |  |  |
| 4 | Description | varchar(255) | Yes |  |  |
| 5 | URL | varchar(1024) | Yes |  |  |
| 6 | RequiredLevel | int | Yes |  |  |
| 7 | SortSeq | int | Yes |  |  |

### Messages {dbo-messages}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-30 18:19:59.113000 |
| **Modified** | 2024-06-21 22:32:28.687000 |
| **Primary Key** | MessageId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MessageId | int | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Code | varchar(20) | Yes |  |  |
| 4 | Comments | varchar(1023) | Yes |  |  |

### Months {dbo-months}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12 |
| **Created** | 2012-09-25 14:08:09.963000 |
| **Modified** | 2024-06-21 22:32:28.857000 |
| **Primary Key** | MonthId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MonthId | int | No |  | PK |
| 2 | MonthName | varchar(50) | No |  |  |
| 3 | Abbrev | char(3) | No |  |  |

### MSDS {dbo-msds}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 58,726 |
| **Created** | 2013-07-16 17:36:10.353000 |
| **Modified** | 2024-06-21 22:32:29.283000 |
| **Primary Key** | MSDSId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MSDSId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CurrentVersionMSDSId | int | Yes |  |  |
| 4 | AlternateDescription | varchar(60) | Yes |  |  |
| 5 | ContentCentralMSDSDocId | varchar(36) | Yes |  |  |

### MSDSDetail {dbo-msdsdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 138,516 |
| **Created** | 2015-12-21 00:50:45.193000 |
| **Modified** | 2024-06-21 22:41:21.630000 |
| **Primary Key** | MSDSDetailID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MSDSDetailID | int IDENTITY | No |  | PK |
| 2 | MSDSID | int | Yes |  | FK → dbo.MSDS.MSDSId |
| 3 | SeqNum | int | Yes |  |  |
| 4 | RTK_CASFileId | int | Yes |  |  |
| 5 | MixturePercent | decimal(9,5) | Yes |  |  |
| 6 | LegacyCASRegNo | varchar(12) | Yes |  |  |
| 7 | MixturePercentCode | char(2) | Yes |  |  |

### MSRPExcelExport {dbo-msrpexcelexport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 563 |
| **Created** | 2014-09-08 18:55:15.300000 |
| **Modified** | 2024-06-21 21:59:56.757000 |
| **Primary Key** | MSRPExcelExportId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MSRPExcelExportId | int IDENTITY | No |  | PK |
| 2 | ManufacturerName | varchar(50) | Yes |  |  |
| 3 | ProductLine | varchar(50) | Yes |  |  |
| 4 | OptionName | varchar(50) | Yes |  |  |
| 5 | ManufWebsite | varchar(255) | Yes |  |  |
| 6 | RangeBase1 | varchar(50) | Yes |  |  |
| 7 | RangeWeight1 | varchar(50) | Yes |  |  |
| 8 | RangeBase2 | varchar(50) | Yes |  |  |
| 9 | RangeWeight2 | varchar(50) | Yes |  |  |
| 10 | RangeBase3 | varchar(50) | Yes |  |  |
| 11 | RangeWeight3 | varchar(50) | Yes |  |  |
| 12 | RangeBase4 | varchar(50) | Yes |  |  |
| 13 | RangeWeight4 | varchar(50) | Yes |  |  |
| 14 | RangeBase5 | varchar(50) | Yes |  |  |
| 15 | RangeWeight5 | varchar(50) | Yes |  |  |
| 16 | RangeBase6 | varchar(50) | Yes |  |  |
| 17 | RangeWeight6 | varchar(50) | Yes |  |  |

### MSRPExcelImport {dbo-msrpexcelimport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 76,315 |
| **Created** | 2014-08-04 15:10:49.360000 |
| **Modified** | 2024-06-21 22:32:29.693000 |
| **Primary Key** | MSRPExcelImportId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MSRPExcelImportId | int IDENTITY | No |  | PK |
| 2 | BidNumber | int | Yes |  |  |
| 3 | SeqNumber | int | Yes |  |  |
| 4 | Manufacturer | varchar(100) | Yes |  |  |
| 5 | ProductLineGroup | varchar(100) | Yes |  |  |
| 6 | DeliveryOption | varchar(50) | Yes |  |  |
| 7 | ManufWebsite | varchar(255) | Yes |  |  |
| 8 | Base1 | money | Yes |  |  |
| 9 | Weight1 | decimal(9,5) | Yes |  |  |
| 10 | Base2 | money | Yes |  |  |
| 11 | Weight2 | decimal(9,5) | Yes |  |  |
| 12 | Base3 | money | Yes |  |  |
| 13 | Weight3 | decimal(9,5) | Yes |  |  |
| 14 | Base4 | money | Yes |  |  |
| 15 | Weight4 | decimal(9,5) | Yes |  |  |
| 16 | Base5 | money | Yes |  |  |
| 17 | Weight5 | decimal(9,5) | Yes |  |  |
| 18 | Base6 | money | Yes |  |  |
| 19 | Weight6 | decimal(9,5) | Yes |  |  |
| 20 | Base7 | money | Yes |  |  |
| 21 | Weight7 | decimal(9,5) | Yes |  |  |
| 22 | Base8 | money | Yes |  |  |
| 23 | Weight8 | decimal(9,5) | Yes |  |  |
| 24 | Base9 | money | Yes |  |  |
| 25 | Weight9 | decimal(9,5) | Yes |  |  |
| 26 | Base10 | money | Yes |  |  |
| 27 | Weight10 | decimal(9,5) | Yes |  |  |

### MSRPOptions {dbo-msrpoptions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12 |
| **Created** | 2013-09-23 15:13:25.943000 |
| **Modified** | 2024-06-21 22:32:30.153000 |
| **Primary Key** | MSRPOptionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MSRPOptionId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | MSRPOptionName | varchar(50) | No |  |  |

### NextNumber {dbo-nextnumber}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 24,535 |
| **Created** | 2006-08-30 18:19:40.100000 |
| **Modified** | 2025-04-16 02:54:31.280000 |
| **Primary Key** | NextNumberId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | NextNumberId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | SchoolId | int | Yes |  |  |
| 4 | BudgetId | int | Yes |  |  |
| 5 | IdType | char(1) | Yes |  |  |
| 6 | Prefix | varchar(20) | Yes |  |  |
| 7 | Suffix | varchar(20) | Yes |  |  |
| 8 | NextNumber | int | Yes |  |  |
| 9 | SuppressLZ | tinyint | Yes |  |  |
| 10 | NumberLength | tinyint | Yes |  |  |
| 11 | FFMessage | varchar(4096) | Yes |  |  |
| 13 | EndNumber | int | Yes |  |  |
| 28 | ActualNumber | tinyint | Yes |  |  |

### NotificationOptions {dbo-notificationoptions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4 |
| **Created** | 2019-11-01 13:11:17.953000 |
| **Modified** | 2024-06-21 22:32:35.243000 |
| **Primary Key** | NotificationOptionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | NotificationOptionId | int IDENTITY | No |  | PK |
| 2 | Name | varchar(50) | No |  |  |

### Notifications {dbo-notifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 720 |
| **Created** | 2019-11-01 13:11:18.267000 |
| **Modified** | 2024-06-21 21:54:28.740000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | NotificationId | bigint IDENTITY | No |  |  |
| 2 | UserId | bigint | No |  |  |
| 3 | Email | varchar(300) | No |  |  |
| 4 | DateSent | datetime | Yes |  |  |
| 8 | NotificationType | varchar(50) | Yes |  |  |
| 10 | EmailBlastId | int | Yes |  |  |
| 12 | EmailHTMLTable | varchar(MAX) | Yes |  |  |

### OBPrices {dbo-obprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2004-04-02 11:08:05.630000 |
| **Modified** | 2021-11-08 21:28:49.433000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemId | int | No |  |  |
| 2 | PackedCode | varchar(50) | Yes |  |  |
| 3 | CrossRefId | int | Yes |  |  |
| 4 | CrossRefIdBid | int | Yes |  |  |
| 5 | BidPrice | money | Yes |  |  |
| 6 | GrossPrice | money | Yes |  |  |
| 7 | CatalogPrice | money | Yes |  |  |
| 8 | AwardId | int | No |  |  |
| 9 | VendorId | int | No |  |  |
| 10 | PricePlanId | int | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | VendorItemCode | varchar(50) | Yes |  |  |
| 13 | ParentCatalogId | int | Yes |  |  |
| 14 | ItemCode | varchar(50) | Yes |  |  |
| 15 | Description | varchar(1024) | Yes |  |  |
| 16 | UnitId | int | Yes |  |  |
| 17 | UnitCode | varchar(20) | Yes |  |  |
| 18 | PriceId | int | Yes |  |  |
| 19 | Page | char(4) | Yes |  |  |
| 20 | DiscountRate | decimal(9,5) | Yes |  |  |
| 21 | Name | varchar(50) | Yes |  |  |
| 22 | VendorName | varchar(50) | Yes |  |  |
| 23 | CategoryId | int | Yes |  |  |
| 24 | PackedItemCode | varchar(50) | Yes |  |  |
| 25 | BidItemId | int | Yes |  |  |
| 26 | Alternate | varchar(1024) | Yes |  |  |
| 27 | PackedVendorItemCode | varchar(255) | Yes |  |  |
| 28 | CatalogYear | char(2) | Yes |  |  |

### OBView {dbo-obview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2007-10-21 17:26:58.403000 |
| **Modified** | 2021-11-08 21:28:49.460000 |
| **Primary Key** | OBDWorkId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OBDWorkId | int IDENTITY | No |  | PK |
| 2 | Title | varchar(255) | Yes |  |  |
| 3 | HeadingDescription | varchar(4096) | Yes |  |  |
| 4 | ItemCode | varchar(32) | Yes |  |  |
| 5 | ItemDescription | varchar(1024) | Yes |  |  |
| 6 | UnitCode | varchar(10) | Yes |  |  |
| 7 | BidPrice | money | Yes |  |  |
| 8 | PricePlanDescription | varchar(255) | Yes |  |  |
| 9 | CatalogPage | varchar(4) | Yes |  |  |
| 10 | CatalogYear | char(2) | Yes |  |  |
| 11 | VendorCode | varchar(16) | Yes |  |  |
| 12 | VendorName | varchar(255) | Yes |  |  |
| 13 | VendorItemCode | varchar(32) | Yes |  |  |
| 14 | Alternate | varchar(1024) | Yes |  |  |
| 15 | Category | varchar(255) | Yes |  |  |
| 16 | TotalQuantity | int | Yes |  |  |
| 17 | TotalRequisitions | int | Yes |  |  |
| 18 | DistrictUsed | int | Yes |  |  |
| 19 | ExpandAll | tinyint | Yes |  |  |
| 20 | ItemId | int | Yes |  |  |
| 21 | HeadingId | int | Yes |  |  |
| 22 | BidItemId | int | Yes |  |  |
| 23 | Weight | int | Yes |  |  |
| 24 | SortSeq | varchar(64) | Yes |  |  |
| 25 | LYQty | int | Yes |  |  |
| 26 | MustKeep | int | Yes |  |  |
| 27 | GrossPrice | money | Yes |  |  |
| 28 | BidDiscountRate | decimal(9,5) | Yes |  |  |
| 29 | CatalogDiscountRate | decimal(9,5) | Yes |  |  |
| 30 | Compliant | tinyint | Yes |  |  |

### Options {dbo-options}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2005-12-01 23:33:48.720000 |
| **Modified** | 2024-06-21 22:32:35.410000 |
| **Primary Key** | OptionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OptionId | int | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Name | varchar(30) | Yes |  |  |
| 4 | OptionType | varchar(40) | Yes |  |  |

### OptionsLink {dbo-optionslink}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2005-12-01 23:34:28.643000 |
| **Modified** | 2024-06-21 22:32:36.017000 |
| **Primary Key** | OptionLinkId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OptionLinkId | int | No |  | PK |
| 2 | OptionId | int | Yes |  |  |
| 3 | LinkId | int | Yes |  |  |
| 4 | Value | varchar(255) | Yes |  |  |

### OrderBookAlwaysAdd {dbo-orderbookalwaysadd}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9 |
| **Created** | 2006-08-30 18:18:28.363000 |
| **Modified** | 2024-06-21 22:32:37.067000 |
| **Primary Key** | OBAAId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OBAAId | int IDENTITY | No |  | PK |
| 2 | CategoryId | int | Yes |  |  |
| 3 | ItemCode | varchar(32) | Yes |  |  |

### OrderBookDetail {dbo-orderbookdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 37,817,410 |
| **Created** | 2016-03-22 02:25:48.800000 |
| **Modified** | 2024-06-21 22:33:09.703000 |
| **Primary Key** | OrderBookDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OrderBookDetailId | int IDENTITY | No |  | PK |
| 2 | OrderBookId | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | BidItemId | int | Yes |  |  |
| 6 | Weight | int | Yes |  |  |
| 7 | BasePrice | money | Yes |  |  |
| 8 | CatalogId | int | Yes |  |  |
| 9 | CrossRefId | int | Yes |  |  |
| 10 | BidPrice | money | Yes |  |  |
| 11 | GrossPrice | money | Yes |  |  |
| 12 | CatalogPrice | money | Yes |  |  |
| 13 | DiscountRate | decimal(9,5) | Yes |  |  |
| 14 | CatalogPage | varchar(4) | Yes |  |  |
| 15 | CatalogYear | varchar(2) | Yes |  |  |
| 16 | VendorCode | varchar(16) | Yes |  |  |
| 17 | VendorName | varchar(255) | Yes |  |  |
| 18 | VendorItemCode | varchar(50) | Yes |  |  |
| 19 | Alternate | varchar(1024) | Yes |  |  |
| 20 | AwardId | int | Yes |  |  |
| 21 | ParentAwardId | int | Yes |  |  |
| 22 | VendorId | int | Yes |  |  |

### OrderBookDetailOld {dbo-orderbookdetailold}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 187,630,151 |
| **Created** | 2015-11-18 23:45:36.673000 |
| **Modified** | 2021-11-08 21:29:55.377000 |
| **Primary Key** | OrderBookDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OrderBookDetailId | int IDENTITY | No |  | PK |
| 2 | OrderBookId | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | BidItemId | int | Yes |  |  |
| 6 | Weight | int | Yes |  |  |
| 7 | BasePrice | money | Yes |  |  |
| 8 | CatalogId | int | Yes |  |  |
| 9 | CrossRefId | int | Yes |  |  |
| 10 | BidPrice | money | Yes |  |  |
| 11 | GrossPrice | money | Yes |  |  |
| 12 | CatalogPrice | money | Yes |  |  |
| 13 | DiscountRate | decimal(9,5) | Yes |  |  |
| 14 | CatalogPage | varchar(4) | Yes |  |  |
| 15 | CatalogYear | varchar(2) | Yes |  |  |
| 16 | VendorCode | varchar(16) | Yes |  |  |
| 17 | VendorName | varchar(255) | Yes |  |  |
| 18 | VendorItemCode | varchar(50) | Yes |  |  |
| 19 | Alternate | varchar(1024) | Yes |  |  |
| 20 | AwardId | int | Yes |  |  |
| 21 | ParentAwardId | int | Yes |  |  |
| 22 | VendorId | int | Yes |  |  |

### OrderBookLog {dbo-orderbooklog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 474,348 |
| **Created** | 2006-08-29 22:44:53.307000 |
| **Modified** | 2024-06-21 22:33:10.603000 |
| **Primary Key** | OrderBookLogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OrderBookLogId | int IDENTITY | No |  | PK |
| 2 | Printed | datetime | Yes |  |  |
| 3 | OrderBookId | int | Yes |  |  |
| 4 | DistrictId | int | Yes |  |  |
| 5 | SchoolId | int | Yes |  |  |
| 6 | UserId | int | Yes |  |  |
| 7 | ItemsPrinted | int | Yes |  |  |
| 8 | PagesPrinted | int | Yes |  |  |
| 9 | Device | varchar(255) | Yes |  |  |

### OrderBooks {dbo-orderbooks}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 30,430 |
| **Created** | 2006-08-29 22:45:05.260000 |
| **Modified** | 2024-06-21 22:33:11.107000 |
| **Primary Key** | OrderBookId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OrderBookId | int IDENTITY | No |  | PK |
| 2 | PricePlanDescription | varchar(255) | Yes |  |  |
| 3 | Category | varchar(255) | Yes |  |  |
| 4 | CategoryId | int | Yes |  |  |
| 5 | PricePlanId | int | Yes |  |  |
| 6 | AwardId | int | Yes |  |  |
| 7 | Type | char(1) | Yes |  |  |
| 8 | DistrictId | int | Yes |  |  |
| 9 | Markup | decimal(9,5) | Yes |  |  |
| 10 | BidHeaderId | int | Yes |  |  |
| 11 | OrderBookYear | int | Yes |  |  |
| 12 | OrderBookCreated | datetime | Yes |  |  |
| 13 | Active | int | Yes |  |  |
| 14 | MasterBook | int | Yes |  |  |
| 15 | MasterLetter | char(1) | Yes |  |  |
| 16 | UseParentCatalog | int | Yes |  |  |
| 17 | KeepZeroPages | int | Yes |  |  |

### OrderBookTypes {dbo-orderbooktypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12 |
| **Created** | 2006-08-29 22:45:16.183000 |
| **Modified** | 2024-06-21 22:33:11.303000 |
| **Primary Key** | OrderBookTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | OrderBookTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(255) | Yes |  |  |
| 3 | PrintMode | int | Yes |  |  |
| 4 | UseOnlineFormat | tinyint | Yes |  |  |

### Payments {dbo-payments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:45:33.370000 |
| **Modified** | 2024-06-21 22:33:12.327000 |
| **Primary Key** | PaymentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PaymentId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | InvoiceId | int | Yes |  |  |
| 4 | PaymentTypeId | int | No |  |  |
| 5 | PaymentDate | datetime | No |  |  |
| 6 | Amount | money | Yes |  |  |
| 7 | Comments | varchar(4096) | Yes |  |  |

### PaymentTypes {dbo-paymenttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:45:43.540000 |
| **Modified** | 2024-06-21 22:33:12.483000 |
| **Primary Key** | PaymentTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PaymentTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |

### PendingApprovals {dbo-pendingapprovals}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 578,386 |
| **Created** | 2015-11-17 09:59:01.840000 |
| **Modified** | 2021-11-08 21:29:55.440000 |
| **Primary Key** | SysId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SysId | int IDENTITY | No |  | PK |
| 2 | SessionId | int | Yes |  |  |
| 3 | SchoolId | int | Yes |  |  |
| 4 | UserId | int | Yes |  |  |
| 5 | RequisitionId | int | Yes |  |  |
| 6 | BudgetId | int | Yes |  |  |
| 7 | AccountId | int | Yes |  |  |
| 8 | CategoryId | int | Yes |  |  |
| 9 | StatusId | int | Yes |  |  |
| 10 | Amount | money | Yes |  |  |
| 11 | ApprovalLevel | tinyint | Yes |  |  |
| 12 | ApprovalDate | datetime | Yes |  |  |
| 13 | LastApprovalId | int | Yes |  |  |
| 14 | NextApproverId | int | Yes |  |  |
| 15 | LastApproverId | int | Yes |  |  |

### PO {dbo-po}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,465,867 |
| **Created** | 2006-08-30 18:16:24.613000 |
| **Modified** | 2026-01-22 20:16:25.917000 |
| **Primary Key** | POId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POId | int IDENTITY | No |  | PK |
| 2 | RequisitionId | int | Yes |  | FK → dbo.Requisitions.RequisitionId |
| 3 | VendorId | int | Yes |  | FK → dbo.Vendors.VendorId |
| 4 | PONumber | varchar(24) | Yes |  |  |
| 5 | PODate | datetime | Yes |  |  |
| 6 | DatePrinted | datetime | Yes |  |  |
| 7 | DatePrintedDetail | datetime | Yes |  |  |
| 8 | DateExported | datetime | Yes |  |  |
| 9 | DateOrdered | datetime | Yes |  |  |
| 10 | DateReceived | datetime | Yes |  |  |
| 11 | Amount | money | Yes |  |  |
| 12 | ItemCount | int | Yes |  |  |
| 13 | AwardId | int | Yes |  |  |
| 14 | DiscountAmount | money | Yes |  |  |
| 15 | TotalGross | money | Yes |  |  |
| 16 | DiscountRate | decimal(9,5) | Yes |  |  |
| 17 | ShippingAmount | money | Yes |  |  |
| 18 | ExportedToVendor | datetime | Yes |  |  |
| 19 | UploadId | int | Yes |  |  |
| 21 | Cancelled | tinyint | Yes |  |  |
| 22 | POStatusID | int | Yes |  |  |
| 35 | isActualNumber | tinyint | Yes |  |  |
| 37 | ePOSuppressed | tinyint | Yes |  |  |

### PODetailItems {dbo-podetailitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 24,349,864 |
| **Created** | 2006-08-29 22:47:35.683000 |
| **Modified** | 2024-06-21 22:48:37.943000 |
| **Primary Key** | PODetailItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PODetailItemId | int IDENTITY | No |  | PK |
| 2 | POId | int | Yes |  | FK → dbo.PO.POId |
| 3 | DetailId | int | Yes |  | FK → dbo.Detail.DetailId |
| 4 | ItemId | int | Yes |  |  |
| 5 | Quantity | int | Yes |  |  |
| 6 | BidItemId | int | Yes |  |  |
| 7 | BidPrice | money | Yes |  |  |
| 8 | GrossPrice | money | Yes |  |  |
| 9 | DiscountRate | decimal(9,5) | Yes |  |  |
| 10 | AwardId | int | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | VendorItemCode | varchar(50) | Yes |  |  |
| 13 | Alternate | varchar(1024) | Yes |  |  |
| 14 | ContractNumber | varchar(50) | Yes |  |  |

### POIDTable {dbo-poidtable}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-06-13 23:52:19.750000 |
| **Modified** | 2024-06-21 22:33:12.657000 |
| **Primary Key** | POIDID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POIDID | int IDENTITY | No |  | PK |
| 2 | POID | int | No |  |  |
| 3 | DateCreated | datetime | Yes | (getdate()) |  |

### POLayoutDetail {dbo-polayoutdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,856 |
| **Created** | 2006-08-30 18:13:36.473000 |
| **Modified** | 2024-06-21 22:33:12.930000 |
| **Primary Key** | POLayoutDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POLayoutDetailId | int IDENTITY | No |  | PK |
| 2 | POLayoutId | int | No |  |  |
| 3 | POLayoutFieldId | int | Yes |  |  |
| 4 | VerticalPos | int | Yes |  |  |
| 5 | HorizontalPos | int | Yes |  |  |
| 6 | MaxWidth | int | Yes |  |  |
| 7 | MaxHeight | int | Yes |  |  |
| 8 | WrapAround | tinyint | Yes |  |  |
| 9 | Literal | varchar(512) | Yes |  |  |
| 11 | PrintWhen | tinyint | Yes |  |  |
| 12 | Image | varbinary(MAX) | Yes |  |  |

### POLayoutFields {dbo-polayoutfields}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 56 |
| **Created** | 2006-08-30 18:12:59.363000 |
| **Modified** | 2024-06-21 22:33:13.053000 |
| **Primary Key** | POLayoutFieldId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POLayoutFieldId | int IDENTITY | No |  | PK |
| 2 | POLayoutField | varchar(50) | Yes |  |  |
| 3 | POLayoutSource | varchar(4096) | Yes |  |  |
| 4 | POLayoutFieldType | tinyint | Yes |  |  |
| 5 | DetailField | tinyint | Yes |  |  |

### POLayouts {dbo-polayouts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 635 |
| **Created** | 2006-08-30 18:12:37.443000 |
| **Modified** | 2024-06-21 22:33:13.363000 |
| **Primary Key** | POLayoutId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POLayoutId | int IDENTITY | No |  | PK |
| 2 | Name | varchar(50) | Yes |  |  |
| 3 | FormLength | int | Yes |  |  |
| 4 | FormWidth | int | Yes |  |  |
| 5 | ContinuousFeed | tinyint | Yes |  |  |
| 6 | Copies | int | Yes |  |  |
| 8 | FormType | int | Yes |  |  |

### POPageSummary {dbo-popagesummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 73,456 |
| **Created** | 2006-08-29 12:23:15.897000 |
| **Modified** | 2024-06-21 22:33:13.507000 |
| **Primary Key** | POPageId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POPageId | uniqueidentifier | No | (newsequentialid()) | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | POId | int | No |  |  |
| 5 | LineCount | int | Yes |  |  |
| 6 | PageCount | int | No |  |  |

### POPrintTaggedPOFile {dbo-poprinttaggedpofile}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 120,948 |
| **Created** | 2007-06-19 17:48:19.937000 |
| **Modified** | 2022-05-18 22:44:42.647000 |
| **Primary Key** | SysId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RSID | int | Yes |  |  |
| 2 | DISTRICTID | int | Yes |  |  |
| 3 | PONUMBER | varchar(24) | Yes |  |  |
| 4 | POID | int | Yes |  |  |
| 5 | POOrderSeq | int | Yes |  |  |
| 6 | AccountId | int | Yes |  |  |
| 7 | AwardsBidHeaderId | int | Yes |  |  |
| 8 | BudgetName | varchar(30) | Yes |  |  |
| 9 | BudgetId | int | Yes |  |  |
| 10 | SysId | int IDENTITY | No |  | PK |

### POQueue {dbo-poqueue}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 26,973 |
| **Created** | 2019-04-28 12:44:15.940000 |
| **Modified** | 2026-03-07 09:58:56.233000 |
| **Primary Key** | POQueueId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POQueueId | int IDENTITY | No |  | PK |
| 2 | UserId | int | No |  |  |
| 3 | VendorId | int | No |  |  |
| 4 | SessionId | int | No |  |  |
| 5 | RequestDate | datetime | No | (getdate()) |  |
| 6 | SendStarted | datetime | Yes |  |  |
| 7 | SendEnded | datetime | Yes |  |  |
| 8 | SendAddress | varchar(512) | Yes |  |  |
| 9 | SendStatus | varchar(50) | Yes |  |  |
| 11 | EarliestDeliveryDate | date | Yes |  |  |
| 12 | RequestedDeliveryDate | date | Yes |  |  |
| 13 | OrderComments | varchar(4096) | Yes |  |  |
| 16 | ScheduledSendDate | date | Yes |  |  |

### POQueueItems {dbo-poqueueitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 398,712 |
| **Created** | 2019-04-28 12:44:15.940000 |
| **Modified** | 2024-07-03 05:07:46.387000 |
| **Primary Key** | POQueueItemId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POQueueItemId | int IDENTITY | No |  | PK |
| 2 | POQueueId | int | No |  |  |
| 3 | POId | int | No |  |  |
| 4 | SendStarted | datetime | Yes |  |  |
| 5 | SendEnded | datetime | Yes |  |  |
| 6 | SendStatus | varchar(255) | Yes |  |  |
| 7 | PayloadId | varchar(255) | Yes |  |  |

### POStatus {dbo-postatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 411,125 |
| **Created** | 2019-04-28 12:44:15.937000 |
| **Modified** | 2026-03-07 09:59:07.123000 |
| **Primary Key** | POStatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POStatusId | int IDENTITY | No |  | PK |
| 2 | POId | int | No |  |  |
| 3 | StatusDate | datetime | No | (getdate()) |  |
| 4 | StatusId | int | No |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | Comments | varchar(512) | Yes |  |  |

### POStatusTable {dbo-postatustable}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-06-13 23:47:12.677000 |
| **Modified** | 2024-06-21 22:33:44.967000 |
| **Primary Key** | POStatusID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POStatusID | int IDENTITY | No |  | PK |
| 2 | StatusName | varchar(50) | Yes |  |  |

### PostCatalogDetail {dbo-postcatalogdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 42,518 |
| **Created** | 2015-03-27 16:14:59.653000 |
| **Modified** | 2024-06-21 22:33:45.510000 |
| **Primary Key** | PostCatalogDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PostCatalogDetailId | int IDENTITY | No |  | PK |
| 2 | PostCatalogHeaderId | int | Yes |  |  |
| 3 | PostInfoType | int | Yes |  |  |
| 4 | PostInfoDesc | varchar(100) | Yes |  |  |
| 5 | PostInfoValue | int | Yes |  |  |
| 6 | PostDateTime | datetime | Yes |  |  |

### PostCatalogHeader {dbo-postcatalogheader}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3,600 |
| **Created** | 2015-03-27 17:07:27.167000 |
| **Modified** | 2024-06-21 22:33:45.753000 |
| **Primary Key** | PostCatalogHeaderId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PostCatalogHeaderId | int IDENTITY | No |  | PK |
| 2 | CatalogId | int | Yes |  |  |
| 3 | PostDateStart | datetime | Yes |  |  |
| 4 | PostDateComplete | datetime | Yes |  |  |

### POTemp {dbo-potemp}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 37 |
| **Created** | 2012-06-13 23:47:07.127000 |
| **Modified** | 2021-11-08 21:29:55.467000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POTempID | int IDENTITY | No |  |  |
| 2 | SessionID | int | No |  |  |

### POTempDetails {dbo-potempdetails}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4,014 |
| **Created** | 2012-06-13 23:47:00.503000 |
| **Modified** | 2021-11-08 21:29:55.490000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | POTempDetailID | int IDENTITY | No |  |  |
| 2 | POTempID | int | Yes |  |  |
| 3 | RequisitionID | int | No |  |  |
| 4 | VendorID | int | No |  |  |
| 5 | BidHeaderID | int | No |  |  |
| 6 | PONumber | varchar(50) | Yes |  |  |
| 7 | POPrefix | varchar(50) | Yes |  |  |
| 8 | POSuffix | varchar(50) | Yes |  |  |

### PPCatalogs {dbo-ppcatalogs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,665 |
| **Created** | 2001-10-18 10:39:45.020000 |
| **Modified** | 2024-06-21 22:33:45.993000 |
| **Primary Key** | PPCatalogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PPCatalogId | int IDENTITY | No |  | PK |
| 2 | PricePlanId | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | CatalogId | int | Yes |  |  |
| 5 | DiscountRate | decimal(5,2) | Yes |  |  |
| 6 | AwardId | int | Yes |  |  |

### PPCategory {dbo-ppcategory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,458 |
| **Created** | 2006-08-30 18:11:06.317000 |
| **Modified** | 2024-06-21 22:33:46.337000 |
| **Primary Key** | PPCategoryId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PPCategoryId | int IDENTITY | No |  | PK |
| 2 | PricePlanId | int | No |  |  |
| 3 | CategoryId | int | No |  |  |
| 4 | AllowAddenda | int | Yes |  |  |

### PriceHolds {dbo-priceholds}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-04-09 10:18:15.567000 |
| **Modified** | 2024-06-21 22:33:46.537000 |
| **Primary Key** | PriceHoldId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PriceHoldId | int IDENTITY | No |  | PK |
| 2 | DetailId | int | No |  |  |
| 3 | BidPrice | money | Yes |  |  |
| 4 | Quantity | int | Yes |  |  |

### PriceListTypes {dbo-pricelisttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2013-09-16 15:45:57.803000 |
| **Modified** | 2024-06-21 22:33:46.907000 |
| **Primary Key** | PriceListTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PriceListTypeId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Name | varchar(50) | No |  |  |

### PricePlans {dbo-priceplans}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 585 |
| **Created** | 2006-08-30 18:10:25.693000 |
| **Modified** | 2024-06-21 22:33:47.093000 |
| **Primary Key** | PricePlanId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PricePlanId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Code | varchar(20) | Yes |  |  |
| 4 | Description | varchar(255) | Yes |  |  |
| 5 | LastAltered | datetime | Yes |  |  |
| 6 | LastUpdated | datetime | Yes |  |  |
| 8 | stateid | int | Yes |  |  |

### PriceRanges {dbo-priceranges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 120,619 |
| **Created** | 2013-09-23 16:02:36.553000 |
| **Modified** | 2024-06-21 22:33:47.393000 |
| **Primary Key** | PriceRangeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PriceRangeId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | CategoryId | int | No |  |  |
| 4 | ManufacturerId | int | Yes |  |  |
| 5 | ManufacturerProductLineId | int | Yes |  |  |
| 6 | RangeBase | money | Yes |  |  |
| 7 | RangeWeight | decimal(9,5) | Yes |  |  |
| 8 | MSRPOptionId | int | Yes |  |  |

### Prices {dbo-prices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2016-11-27 16:10:54.967000 |
| **Modified** | 2024-06-21 22:41:21.730000 |
| **Primary Key** | PriceId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ItemId | int | No |  |  |
| 2 | PackedCode | varchar(50) | Yes |  |  |
| 3 | CrossRefId | int | Yes |  |  |
| 4 | CrossRefIdBid | int | Yes |  |  |
| 5 | BidPrice | decimal(34,13) | Yes |  |  |
| 6 | GrossPrice | money | Yes |  |  |
| 7 | CatalogPrice | money | Yes |  |  |
| 8 | AwardId | int | No |  |  |
| 9 | VendorId | int | No |  |  |
| 10 | PricePlanId | int | Yes |  |  |
| 11 | CatalogId | int | Yes |  |  |
| 12 | VendorItemCode | varchar(50) | Yes |  |  |
| 13 | ParentCatalogId | int | Yes |  |  |
| 14 | ItemCode | varchar(50) | Yes |  |  |
| 15 | Description | varchar(1024) | Yes |  |  |
| 16 | UnitId | int | Yes |  |  |
| 17 | UnitCode | varchar(20) | Yes |  |  |
| 18 | PriceId | uniqueidentifier | No | (newid()) | PK |
| 19 | Page | char(4) | Yes |  |  |
| 20 | DiscountRate | decimal(9,5) | Yes |  |  |
| 21 | Name | varchar(50) | Yes |  |  |
| 22 | VendorName | varchar(50) | Yes |  |  |
| 23 | CategoryId | int | Yes |  |  |
| 24 | PackedItemCode | varchar(50) | Yes |  |  |
| 25 | BidItemId | int | Yes |  | FK → dbo.BidItems_Old.BidItemId |
| 26 | Alternate | varchar(1024) | Yes |  |  |
| 27 | PackedVendorItemCode | varchar(255) | Yes |  |  |
| 28 | CatalogYear | char(2) | Yes |  |  |
| 29 | RedirectedItemId | int | Yes |  |  |
| 30 | BidHeaderId | int | Yes |  |  |

### PricingAddenda {dbo-pricingaddenda}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 208,894 |
| **Created** | 2018-08-08 00:00:51.937000 |
| **Modified** | 2026-03-07 09:59:07.683000 |
| **Primary Key** | PricingAddendaId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PricingAddendaId | bigint IDENTITY | No |  | PK |
| 2 | CrossRefId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | HeadingId | int | Yes |  |  |
| 5 | KeywordId | int | Yes |  |  |
| 6 | CategoryId | int | Yes |  |  |
| 7 | ItemId | int | Yes |  |  |
| 8 | VendorId | int | Yes |  |  |
| 9 | DistrictId | int | Yes |  |  |
| 10 | HeadingKeywordId | bigint | Yes |  |  |
| 11 | ListPrice | money | Yes |  |  |
| 12 | LastBidPrice | money | Yes |  |  |
| 13 | CatalogPrice | money | Yes |  |  |
| 14 | CatalogPage | char(4) | Yes |  |  |
| 15 | AwardId | int | Yes |  |  |
| 16 | BidType | tinyint | Yes |  |  |
| 17 | ItemBidType | varchar(32) | Yes |  |  |
| 18 | UnitId | int | Yes |  |  |
| 19 | Unitcode | varchar(20) | Yes |  |  |
| 20 | SortSeq | varchar(64) | Yes |  |  |
| 21 | FullDescription | varchar(4096) | Yes |  |  |
| 22 | PackedItemCode | varchar(50) | Yes |  |  |
| 23 | ItemCode | varchar(50) | Yes |  |  |
| 24 | VendorItemCode | varchar(50) | Yes |  |  |
| 25 | Manufacturer | varchar(50) | Yes |  |  |
| 26 | ManufacturerPartNumber | varchar(50) | Yes |  |  |
| 27 | ItemHeading | varchar(255) | Yes |  |  |
| 28 | ItemKeyword | varchar(50) | Yes |  |  |
| 29 | AllStringFields | varchar(6000) | Yes |  |  |

### PricingConsolidatedOrderCounts {dbo-pricingconsolidatedordercounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 401,387 |
| **Created** | 2019-01-30 14:35:04.380000 |
| **Modified** | 2021-11-09 18:46:47.393000 |
| **Primary Key** | PCOCId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PCOCId | bigint IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ItemId | int | No |  |  |
| 4 | OrderCount | int | No |  |  |

### PricingMap {dbo-pricingmap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2015-09-08 16:05:09.493000 |
| **Modified** | 2024-06-21 22:33:50.157000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | ItemId | int | No |  |  |
| 4 | MappedItemId | int | No |  |  |
| 5 | ItemCode | varchar(50) | Yes |  |  |
| 6 | PackedItemCode | varchar(50) | Yes |  |  |
| 7 | BidPrice | money | No |  |  |
| 8 | CatalogPrice | money | No |  |  |
| 9 | BidItemId | int | Yes |  |  |
| 10 | VendorId | int | No |  |  |
| 11 | VendorItemCode | varchar(50) | Yes |  |  |
| 12 | PackedVendorItemCode | varchar(50) | Yes |  |  |
| 13 | ManufacturerPartNumber | varchar(50) | Yes |  |  |
| 14 | PackedManufacturerPartNumber | varchar(50) | Yes |  |  |
| 15 | UnitId | int | No |  |  |
| 16 | UnitCode | varchar(16) | No |  |  |
| 17 | Alternate | varchar(512) | Yes |  |  |
| 18 | ItemDescription | varchar(1024) | Yes |  |  |
| 19 | SortSeq | varchar(64) | Yes |  |  |

### PricingUpdate {dbo-pricingupdate}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 59,987 |
| **Created** | 2018-09-11 14:14:32.963000 |
| **Modified** | 2024-06-21 22:33:50.790000 |
| **Primary Key** | PricingUpdateId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PricingUpdateId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | No |  |  |
| 3 | LastUpdated | datetime | Yes |  |  |

### PrintDocuments {dbo-printdocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-10-04 15:39:24.453000 |
| **Modified** | 2024-06-21 22:33:50.923000 |
| **Primary Key** | PrintDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PrintDocumentId | int IDENTITY | No |  | PK |
| 2 | Created | datetime | Yes | (getdate()) |  |
| 3 | Printed | datetime | Yes |  |  |
| 4 | RequestedBy | int | Yes |  |  |
| 5 | DistrictId | int | Yes |  |  |
| 6 | SchoolId | int | Yes |  |  |
| 7 | UserId | int | Yes |  |  |
| 8 | DocumentName | varchar(50) | Yes |  |  |
| 9 | DocumentType | varchar(50) | Yes |  |  |
| 10 | DocumentLength | int | Yes |  |  |
| 11 | DocumentPages | int | Yes |  |  |
| 12 | DocumentBody | varbinary(MAX) | Yes |  |  |

### Printers {dbo-printers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 18 |
| **Created** | 2006-08-30 18:09:48.350000 |
| **Modified** | 2025-11-26 20:55:58.167000 |
| **Primary Key** | PrinterId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PrinterId | int IDENTITY | No |  | PK |
| 2 | Name | varchar(50) | Yes |  |  |
| 3 | PrintPrefix | varchar(255) | Yes |  |  |
| 4 | PrintSuffix | varchar(255) | Yes |  |  |
| 5 | PrinterType | varchar(50) | Yes |  |  |
| 6 | PrintQueue | varchar(255) | Yes |  |  |
| 21 | Active | bit | Yes | ((1)) |  |
| 22 | IsOkiPrinter | bit | Yes | ((1)) |  |

### ProductVerificationResults {dbo-productverificationresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 206,645 |
| **Created** | 2025-10-31 17:14:37.973000 |
| **Modified** | 2026-03-07 10:00:28.087000 |
| **Primary Key** | VerificationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VerificationId | int IDENTITY | No |  | PK |
| 2 | EntryId | nvarchar(255) | No |  |  |
| 3 | QueryType | nvarchar(100) | No |  |  |
| 4 | VerificationResult | nvarchar(50) | No |  |  |
| 5 | DataChecked | nvarchar(MAX) | Yes |  |  |
| 6 | Reasoning | nvarchar(MAX) | Yes |  |  |
| 7 | VerifiedAt | datetime2 | Yes | (getdate()) |  |

### ProjectTasks {dbo-projecttasks}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14 |
| **Created** | 2006-08-30 18:09:24.567000 |
| **Modified** | 2024-06-21 22:33:53.837000 |
| **Primary Key** | ProjectTasksId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ProjectTasksId | int IDENTITY | No |  | PK |
| 2 | TaskSeqNum | int | Yes |  |  |
| 3 | TaskDescription | varchar(60) | Yes |  |  |
| 4 | PreReqSeqNum | int | Yes |  |  |
| 5 | OnlineTask | tinyint | Yes |  |  |
| 6 | BookletTask | tinyint | Yes |  |  |

### QuestionnaireResponses {dbo-questionnaireresponses}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-09-25 12:55:48.420000 |
| **Modified** | 2024-06-21 22:33:54.317000 |
| **Primary Key** | qrid |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | qrid | int IDENTITY | No |  | PK |
| 2 | districtid | int | No |  |  |
| 3 | userid | int | No |  |  |
| 4 | qr1 | varchar(500) | Yes |  |  |
| 5 | qr2 | varchar(500) | Yes |  |  |
| 6 | qr3 | varchar(500) | Yes |  |  |
| 7 | qr4 | varchar(500) | Yes |  |  |
| 8 | qr5 | varchar(500) | Yes |  |  |
| 9 | qr6 | varchar(500) | Yes |  |  |
| 10 | qr7 | varchar(500) | Yes |  |  |
| 11 | qr8 | varchar(500) | Yes |  |  |
| 12 | qr9 | varchar(500) | Yes |  |  |
| 13 | qr10 | varchar(500) | Yes |  |  |
| 14 | qActionDate | datetime | No |  |  |

### Rates {dbo-rates}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-04-16 13:30:40.200000 |
| **Modified** | 2024-06-21 22:33:55.123000 |
| **Primary Key** | RateId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RateId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | ServiceId | int | No |  |  |
| 4 | BidId | int | No |  |  |
| 5 | BidQuantity | decimal(9,5) | No |  |  |
| 6 | RateTypeId | tinyint | No |  |  |
| 7 | RateUnitId | int | No |  |  |
| 8 | Rate | decimal(9,5) | Yes |  |  |
| 9 | BidCost | decimal(11,5) | Yes |  |  |
| 10 | Comments | text | Yes |  |  |

### RateTypes {dbo-ratetypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-04-16 13:30:40.183000 |
| **Modified** | 2024-06-21 22:33:56.660000 |
| **Primary Key** | RateTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RateTypeId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Description | varchar(50) | No |  |  |

### RateUnits {dbo-rateunits}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-04-16 13:30:40.200000 |
| **Modified** | 2024-06-21 22:33:56.957000 |
| **Primary Key** | RateUnitId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RateUnitId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Description | varchar(50) | Yes |  |  |

### Receiving {dbo-receiving}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-30 18:08:41.550000 |
| **Modified** | 2024-06-21 22:33:57.067000 |
| **Primary Key** | ReceivingId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ReceivingId | int | No |  | PK |
| 2 | POId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | Quantity | int | Yes |  |  |
| 5 | DateReceived | datetime | Yes |  |  |
| 6 | Comments | varchar(1023) | Yes |  |  |

### ReportSession {dbo-reportsession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,365,057 |
| **Created** | 2006-08-30 18:08:23.160000 |
| **Modified** | 2024-06-21 22:34:54.313000 |
| **Primary Key** | RSId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RSId | int IDENTITY | No |  | PK |
| 2 | RSData | varchar(4096) | Yes |  |  |
| 3 | ReportStarted | datetime | Yes |  |  |
| 4 | ReportEnded | datetime | Yes |  |  |
| 5 | ReportProcessorId | int | Yes |  |  |
| 6 | ReportOption | int | Yes |  |  |
| 7 | ReportRequestedBy | varchar(50) | Yes |  |  |
| 8 | ReportFile | varchar(255) | Yes |  |  |
| 9 | LastPrinted | datetime | Yes |  |  |
| 10 | PrintPages | int | Yes |  |  |
| 11 | PrintCopies | int | Yes |  |  |

### ReportSessionLinks {dbo-reportsessionlinks}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 52,333,457 |
| **Created** | 2006-08-30 18:07:49.473000 |
| **Modified** | 2024-06-21 21:57:15.410000 |
| **Primary Key** | RSLId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RSLId | int IDENTITY | No |  | PK |
| 2 | RSId | int | Yes |  |  |
| 3 | IntId | int | Yes |  |  |
| 5 | AuxId | int | Yes |  |  |

### ReqAudit {dbo-reqaudit}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-30 18:07:18.333000 |
| **Modified** | 2024-06-21 22:34:54.877000 |
| **Primary Key** | ReqAuditId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ReqAuditId | int IDENTITY | No |  | PK |
| 2 | RequisitionId | int | Yes |  |  |
| 3 | DetailId | int | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | FieldName | varchar(50) | Yes |  |  |
| 6 | PreviousValue | varchar(255) | Yes |  |  |
| 7 | NewValue | varchar(255) | Yes |  |  |

### RequisitionChangeLog {dbo-requisitionchangelog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,938,491 |
| **Created** | 2006-08-29 22:56:42.493000 |
| **Modified** | 2024-06-21 22:02:01.147000 |
| **Primary Key** | RequisitionChangeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionChangeId | int IDENTITY | No |  | PK |
| 2 | RequisitionId | int | No |  |  |
| 3 | OrigSchoolId | int | Yes |  |  |
| 4 | OrigUserId | int | Yes |  |  |
| 5 | OrigBudgetId | int | Yes |  |  |
| 6 | OrigBudgetAccountId | int | Yes |  |  |
| 7 | OrigUserAccountId | int | Yes |  |  |
| 8 | OrigCategoryId | int | Yes |  |  |
| 9 | OrigShippingId | int | Yes |  |  |
| 10 | OrigAttention | varchar(50) | Yes |  |  |
| 11 | OrigAccountCode | varchar(50) | Yes |  |  |
| 12 | OrigBidHeaderId | int | Yes |  |  |
| 13 | NewSchoolId | int | Yes |  |  |
| 14 | NewUserId | int | Yes |  |  |
| 15 | NewBudgetId | int | Yes |  |  |
| 16 | NewBudgetAccountId | int | Yes |  |  |
| 17 | NewUserAccountId | int | Yes |  |  |
| 18 | NewCategoryId | int | Yes |  |  |
| 19 | NewShippingId | int | Yes |  |  |
| 20 | NewAttention | varchar(50) | Yes |  |  |
| 21 | NewAccountCode | varchar(50) | Yes |  |  |
| 22 | NewBidHeaderId | int | Yes |  |  |
| 23 | UserId | int | Yes |  |  |
| 24 | SessionId | int | Yes |  |  |
| 25 | ChangeDate | datetime | Yes |  |  |

### RequisitionNoteEmails {dbo-requisitionnoteemails}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 16,417 |
| **Created** | 2012-06-13 23:49:20.300000 |
| **Modified** | 2024-06-21 22:34:57.953000 |
| **Primary Key** | RequisitionNoteEmailID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionNoteEmailID | int IDENTITY | No |  | PK |
| 2 | RequisitionNoteID | int | No |  |  |
| 3 | UserID | int | No |  |  |

### RequisitionNotes {dbo-requisitionnotes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 25,174 |
| **Created** | 2012-06-13 23:48:58.080000 |
| **Modified** | 2025-04-06 21:19:41.813000 |
| **Primary Key** | RequisitionNoteID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionNoteID | int IDENTITY | No |  | PK |
| 2 | RequisitionID | int | No |  |  |
| 3 | Note | varchar(MAX) | Yes |  |  |
| 4 | CreateDate | datetime | No |  |  |
| 5 | CreatedByUserID | int | No |  |  |

### Requisitions {dbo-requisitions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,148,602 |
| **Created** | 2015-11-16 21:52:27.663000 |
| **Modified** | 2026-03-07 10:02:48.580000 |
| **Primary Key** | RequisitionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | RequisitionNumber | varchar(24) | Yes |  |  |
| 4 | SchoolId | int | Yes |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | BudgetId | int | Yes |  | FK → dbo.Budgets.BudgetId |
| 7 | BudgetAccountId | int | Yes |  |  |
| 8 | UserAccountId | int | Yes |  |  |
| 9 | CategoryId | int | Yes |  | FK → dbo.Category.CategoryId |
| 10 | ShippingId | int | Yes |  |  |
| 11 | Attention | varchar(50) | Yes |  |  |
| 12 | AccountCode | varchar(50) | Yes |  |  |
| 13 | DateEntered | datetime | Yes |  |  |
| 14 | ShippingPercent | decimal(9,5) | Yes |  |  |
| 15 | DiscountPercent | decimal(9,5) | Yes |  |  |
| 16 | ShippingCost | money | Yes |  |  |
| 17 | TotalItemsCost | money | Yes |  |  |
| 18 | TotalRequisitionCost | money | Yes |  |  |
| 19 | Comments | varchar(1023) | Yes |  |  |
| 20 | ApprovalRequired | tinyint | Yes |  |  |
| 21 | ApprovalId | int | Yes |  |  |
| 22 | ApprovalLevel | tinyint | Yes |  |  |
| 23 | StatusId | int | Yes |  |  |
| 24 | OrderDate | datetime | Yes |  |  |
| 25 | DateExported | datetime | Yes |  |  |
| 26 | BidId | int | Yes |  |  |
| 27 | BookId | int | Yes |  |  |
| 28 | SourceId | int | Yes |  |  |
| 29 | BidHeaderId | int | Yes |  |  |
| 30 | LastAlteredSessionId | int | Yes |  |  |
| 31 | DateUpdated | datetime | Yes | (getdate()) |  |
| 32 | OrderType | tinyint | Yes |  |  |
| 33 | NotesCount | int | Yes |  |  |
| 34 | AddendaTotal | money | Yes |  |  |
| 35 | ApprovalCount | int | Yes |  |  |
| 46 | AdditionalFreight | tinyint | Yes |  |  |
| 48 | HistoryCount | int | Yes |  |  |
| 49 | POCount | int | Yes |  |  |
| 50 | LowPOCount | int | Yes |  |  |
| 55 | AdditionalShippingCost | money | Yes |  |  |

### ResetPasswordTracking {dbo-resetpasswordtracking}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 105,046 |
| **Created** | 2024-12-22 23:20:10.793000 |
| **Modified** | 2026-03-21 03:51:26.707000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UserIds | varchar(255) | No |  |  |
| 2 | SchoolId | int | No |  |  |
| 3 | DistrictId | int | No |  |  |
| 4 | Email | varchar(255) | Yes |  |  |
| 5 | ResetPasswordCode | varchar(8) | Yes |  |  |
| 6 | Action | varchar(100) | Yes |  |  |
| 7 | InsertAt | datetime | Yes | (getdate()) |  |
| 8 | ErrorMsg | varchar(MAX) | Yes |  |  |
| 9 | Description | varchar(MAX) | Yes |  |  |

### Rights {dbo-rights}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:57:41.730000 |
| **Modified** | 2024-06-21 22:35:00.920000 |
| **Primary Key** | RightsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RightsId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Code | varchar(255) | Yes |  |  |
| 4 | Description | varchar(255) | Yes |  |  |

### RightsLink {dbo-rightslink}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 22:57:50.323000 |
| **Modified** | 2024-06-21 22:35:01.773000 |
| **Primary Key** | RightsLinkId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RightsLinkId | int IDENTITY | No |  | PK |
| 2 | RightsId | int | Yes |  |  |
| 3 | LinkId | int | Yes |  |  |
| 4 | Value | varchar(255) | Yes |  |  |

### RTK_2010NJHSL {dbo-rtk-2010njhsl}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3,322 |
| **Created** | 2017-03-17 15:33:23.103000 |
| **Modified** | 2021-11-08 21:29:55.617000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Substance Number | nvarchar(255) | Yes |  |  |
| 2 | Common Name | nvarchar(255) | Yes |  |  |
| 3 | Chemical Name | nvarchar(255) | Yes |  |  |
| 4 | CAS Number | nvarchar(255) | Yes |  |  |
| 5 | DOT Number | nvarchar(255) | Yes |  |  |
| 6 | SHHS List | nvarchar(255) | Yes |  |  |
| 7 | synonym | nvarchar(255) | Yes |  |  |
| 8 | Source 1 | nvarchar(255) | Yes |  |  |
| 9 | CA | nvarchar(255) | Yes |  |  |
| 10 | CO | nvarchar(255) | Yes |  |  |
| 11 | MU | nvarchar(255) | Yes |  |  |
| 12 | TE | nvarchar(255) | Yes |  |  |
| 13 | F4 | nvarchar(255) | Yes |  |  |
| 14 | F3 | nvarchar(255) | Yes |  |  |
| 15 | F2 | nvarchar(255) | Yes |  |  |
| 16 | R4 | nvarchar(255) | Yes |  |  |
| 17 | R3 | nvarchar(255) | Yes |  |  |
| 18 | R2 | nvarchar(255) | Yes |  |  |
| 19 | R1 | nvarchar(255) | Yes |  |  |
| 20 | Source 2 | nvarchar(255) | Yes |  |  |
| 21 | Source 3 | nvarchar(255) | Yes |  |  |
| 22 | Source 4 | nvarchar(255) | Yes |  |  |
| 23 | Source 5 | nvarchar(255) | Yes |  |  |
| 24 | Source 6 | nvarchar(255) | Yes |  |  |
| 25 | Source 7 | nvarchar(255) | Yes |  |  |
| 26 | Source 8 | nvarchar(255) | Yes |  |  |
| 27 | Source 14 | nvarchar(255) | Yes |  |  |
| 28 | Source 15 | nvarchar(255) | Yes |  |  |
| 29 | Source 17 | nvarchar(255) | Yes |  |  |
| 30 | Source 18 | nvarchar(255) | Yes |  |  |
| 31 | Source 19 | nvarchar(255) | Yes |  |  |
| 32 | Source 20 | nvarchar(255) | Yes |  |  |
| 33 | Source 21 | nvarchar(255) | Yes |  |  |
| 34 | Source 22 | nvarchar(255) | Yes |  |  |
| 35 | non prefix | nvarchar(255) | Yes |  |  |

### RTK_CASFile {dbo-rtk-casfile}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 7,881 |
| **Created** | 2012-05-16 13:16:15.870000 |
| **Modified** | 2024-06-21 22:35:01.910000 |
| **Primary Key** | RTK_CASFileId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_CASFileId | int IDENTITY | No |  | PK |
| 2 | CASRegNo | varchar(11) | No |  |  |
| 3 | CASChemicalName | varchar(50) | Yes |  |  |
| 4 | DOT_Id | char(4) | Yes |  |  |
| 5 | SubstanceNo | char(4) | Yes |  |  |
| 6 | TradeSecretNo | varchar(20) | Yes |  |  |
| 7 | LegacyCASRegNo | varchar(12) | Yes |  |  |
| 8 | CompoundContaining | varchar(11) | Yes |  |  |
| 9 | SpecialHealthHazard | tinyint | Yes |  |  |
| 10 | Carcinogen | tinyint | Yes |  |  |
| 11 | Mutagen | tinyint | Yes |  |  |
| 12 | Teratogen | tinyint | Yes |  |  |
| 13 | Corrosive | tinyint | Yes |  |  |
| 14 | F4_Flammable4th | tinyint | Yes |  |  |
| 15 | F3_Flammable3rd | tinyint | Yes |  |  |
| 16 | R4_Reactive4th | tinyint | Yes |  |  |
| 17 | R3_Reactive3rd | tinyint | Yes |  |  |
| 18 | R2_Reactive2nd | tinyint | Yes |  |  |
| 19 | SpecialHealthHazardCodes | varchar(30) | Yes |  |  |

### RTK_ContainerCodes {dbo-rtk-containercodes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 21 |
| **Created** | 2006-08-29 22:58:14.493000 |
| **Modified** | 2024-06-21 22:35:02.230000 |
| **Primary Key** | ContainerCodesID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ContainerCodesID | int IDENTITY | No |  | PK |
| 2 | ContainerCode | char(2) | No |  |  |
| 3 | ContainerAltCode | char(2) | Yes |  |  |
| 4 | ContainerDesc | varchar(30) | Yes |  |  |

### RTK_Documents {dbo-rtk-documents}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-03-09 08:50:42.320000 |
| **Modified** | 2024-06-21 22:35:02.343000 |
| **Primary Key** | RTKDocumentId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTKDocumentId | uniqueidentifier | No | (newid()) | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | FacilityId | int | Yes |  |  |
| 4 | SchoolId | int | Yes |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | DocumentId | uniqueidentifier | No |  |  |
| 7 | Description | varchar(1024) | No |  |  |
| 8 | ValidFrom | datetime | Yes |  |  |
| 9 | ValidUntil | datetime | Yes |  |  |
| 10 | Created | datetime | No | (getdate()) |  |
| 11 | Updated | datetime | Yes |  |  |
| 12 | Deleted | datetime | Yes |  |  |

### RTK_FactSheets {dbo-rtk-factsheets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,459 |
| **Created** | 2017-03-17 15:44:04.577000 |
| **Modified** | 2024-06-21 22:35:02.810000 |
| **Primary Key** | RTKFactSheetId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTKFactSheetId | uniqueidentifier | No | (newid()) | PK |
| 2 | SubstanceNumber | int | No |  |  |
| 3 | CommonName | varchar(255) | No |  |  |
| 4 | ChemicalName | varchar(255) | No |  |  |
| 5 | CASNumber | varchar(20) | Yes |  |  |
| 6 | DOTNumber | varchar(10) | Yes |  |  |
| 7 | HazardCodes | varchar(50) | Yes |  |  |
| 8 | Created | datetime | No | (getdate()) |  |
| 9 | Updated | datetime | No | (getdate()) |  |
| 10 | Deleted | datetime | Yes |  |  |

### RTK_HealthHazardCodes {dbo-rtk-healthhazardcodes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9 |
| **Created** | 2006-08-29 22:58:29.540000 |
| **Modified** | 2024-06-21 22:35:02.943000 |
| **Primary Key** | HealthHazardCodesID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | HealthHazardCodesID | int IDENTITY | No |  | PK |
| 2 | HealthHazardCode | char(2) | No |  |  |
| 3 | Description | varchar(30) | Yes |  |  |

### RTK_Inventories {dbo-rtk-inventories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 658 |
| **Created** | 2018-05-31 12:13:17.983000 |
| **Modified** | 2024-06-21 22:35:03.080000 |
| **Primary Key** | RTK_InventoryId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_InventoryId | int IDENTITY | No |  | PK |
| 2 | RTK_SiteId | int | No |  |  |
| 3 | RTK_InventoryDate | date | Yes |  |  |
| 4 | RTK_InventoryYear | int | Yes |  |  |
| 5 | RTK_InventoryBy | varchar(255) | Yes |  |  |
| 6 | RTK_InventoryNotes | varchar(MAX) | Yes |  |  |

### RTK_InventoryRangeCodes {dbo-rtk-inventoryrangecodes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12 |
| **Created** | 2006-08-29 22:58:39.883000 |
| **Modified** | 2024-06-21 22:35:03.227000 |
| **Primary Key** | InventoryRangeCodesID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | InventoryRangeCodesID | int IDENTITY | No |  | PK |
| 2 | RangeCode | char(2) | No |  |  |
| 3 | BegRange | int | Yes |  |  |
| 4 | EndRange | int | Yes |  |  |
| 5 | Description | varchar(25) | Yes |  |  |

### RTK_Items {dbo-rtk-items}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 64,627 |
| **Created** | 2015-12-21 00:52:16.813000 |
| **Modified** | 2024-06-21 22:35:04.177000 |
| **Primary Key** | RTK_ItemsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_ItemsId | int IDENTITY | No |  | PK |
| 2 | CategoryId | int | Yes |  |  |
| 3 | ItemId | int | Yes |  |  |
| 4 | LegacyCometCode | varchar(16) | Yes |  |  |
| 5 | AlternateDesc | varchar(60) | Yes |  |  |
| 6 | CaseCount | int | Yes |  |  |
| 7 | MeasurePct | decimal(9,5) | Yes |  |  |
| 8 | ContainerCodesId | int | Yes |  |  |
| 9 | UOMCodesId | int | Yes |  |  |
| 10 | OtherContainerDesc | varchar(20) | Yes |  |  |
| 11 | LegacyCometDesc | varchar(60) | Yes |  |  |
| 12 | MSDSId | int | Yes |  |  |
| 13 | ItemCode | varchar(50) | Yes |  |  |
| 14 | RTK_PurposeId | int | Yes |  |  |
| 15 | Manufacturer | varchar(50) | Yes |  |  |

### RTK_LegacyDistrictCodesMap {dbo-rtk-legacydistrictcodesmap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 78 |
| **Created** | 2006-08-29 22:58:50.353000 |
| **Modified** | 2024-06-21 22:35:04.500000 |
| **Primary Key** | RTK_DistrictCodesMapId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_DistrictCodesMapId | int IDENTITY | No |  | PK |
| 2 | Legacy_DistrictCode | char(2) | No |  |  |
| 3 | SQL_DistrictCode | char(2) | No |  |  |
| 4 | DistrictId | int | No |  |  |

### RTK_LegacySchoolFile {dbo-rtk-legacyschoolfile}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,766 |
| **Created** | 2006-08-29 22:58:59.790000 |
| **Modified** | 2024-06-21 22:35:05.013000 |
| **Primary Key** | LegacySchoolFileId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | LegacySchoolFileId | int IDENTITY | No |  | PK |
| 2 | LegacyDistrictCode | char(2) | Yes |  |  |
| 3 | LegacySchoolCode | char(5) | Yes |  |  |
| 4 | SchoolName | varchar(30) | Yes |  |  |
| 5 | SchoolAddr | varchar(30) | Yes |  |  |
| 6 | CityStZip | varchar(30) | Yes |  |  |
| 7 | NJEIN | varchar(20) | Yes |  |  |
| 8 | ExposedEmployees | int | Yes |  |  |
| 9 | DistrictId | int | Yes |  |  |
| 10 | RTK_SitesId | int | Yes |  |  |

### RTK_MixtureCodes {dbo-rtk-mixturecodes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11 |
| **Created** | 2006-08-29 22:59:08.823000 |
| **Modified** | 2024-06-21 22:35:05.523000 |
| **Primary Key** | MixtureCodesID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | MixtureCodesID | int IDENTITY | No |  | PK |
| 2 | MixtureCode | char(2) | No |  |  |
| 3 | Description | varchar(12) | Yes |  |  |

### RTK_MSDSDetail {dbo-rtk-msdsdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 151,665 |
| **Created** | 2006-08-29 22:59:39.980000 |
| **Modified** | 2024-06-21 22:35:07.547000 |
| **Primary Key** | RTK_MSDSDetailID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_MSDSDetailID | int IDENTITY | No |  | PK |
| 2 | RTK_ItemsID | int | Yes |  |  |
| 3 | SeqNum | int | Yes |  |  |
| 4 | RTK_CASFileId | int | Yes |  |  |
| 5 | MixturePercent | decimal(9,5) | Yes |  |  |
| 6 | LegacyCASRegNo | varchar(12) | Yes |  |  |
| 7 | MixturePercentCode | char(2) | Yes |  |  |

### RTK_Purposes {dbo-rtk-purposes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 35 |
| **Created** | 2015-01-05 15:42:52.847000 |
| **Modified** | 2024-06-21 22:35:07.730000 |
| **Primary Key** | RTK_PurposeID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_PurposeID | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |

### RTK_ReportItems {dbo-rtk-reportitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,006,140 |
| **Created** | 2006-08-29 23:00:23.697000 |
| **Modified** | 2026-03-07 10:04:06.940000 |
| **Primary Key** | RTK_ReportItemsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_ReportItemsId | int IDENTITY | No |  | PK |
| 2 | Year | int | Yes |  |  |
| 3 | DistrictId | int | Yes |  |  |
| 4 | RTK_SitesId | int | Yes |  |  |
| 5 | CategoryId | int | Yes |  |  |
| 6 | ItemId | int | Yes |  |  |
| 7 | Quantity | int | Yes |  |  |
| 8 | LegacyLocnCode | char(5) | Yes |  |  |
| 9 | LegacyCometItemCode | char(8) | Yes |  |  |
| 10 | DetailId | int | Yes |  |  |
| 11 | ManuallyEntered | int | Yes |  |  |
| 15 | ExactLocationOnSite | varchar(50) | Yes |  |  |
| 17 | MSDSId | int | Yes |  |  |
| 18 | RTK_ItemsId | int | Yes |  |  |

### RTK_Sites {dbo-rtk-sites}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 823 |
| **Created** | 2012-05-21 18:55:17.467000 |
| **Modified** | 2024-06-21 22:35:13.220000 |
| **Primary Key** | RTK_SitesId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTK_SitesId | int IDENTITY | No |  | PK |
| 2 | Active | int | Yes |  |  |
| 3 | DistrictId | int | Yes |  |  |
| 4 | NJEIN | varchar(20) | Yes |  |  |
| 5 | ExposedEmployeesCount | int | Yes |  |  |
| 6 | CoMunCode | varchar(5) | Yes |  |  |
| 7 | FacilityName | varchar(50) | Yes |  |  |
| 8 | MailingAddress1 | varchar(100) | Yes |  |  |
| 9 | MailingAddress2 | varchar(100) | Yes |  |  |
| 10 | MailingAddress3 | varchar(100) | Yes |  |  |
| 11 | MailingAddress4 | varchar(100) | Yes |  |  |
| 12 | FacilityLocation1 | varchar(100) | Yes |  |  |
| 13 | FacilityLocation2 | varchar(100) | Yes |  |  |
| 14 | FacilityLocation3 | varchar(100) | Yes |  |  |
| 15 | FacilityLocation4 | varchar(100) | Yes |  |  |
| 16 | ChemicalInventoryStatus | tinyint | Yes |  |  |
| 17 | FacilityEmergencyContact | varchar(100) | Yes |  |  |
| 18 | EmergencyPhone | varchar(50) | Yes |  |  |
| 19 | ResponsibleOfficial | varchar(100) | Yes |  |  |
| 20 | TitleResponsibleOfficial | varchar(100) | Yes |  |  |
| 21 | EmailResponsibleOfficial | varchar(200) | Yes |  |  |
| 22 | PhoneResponsibleOfficial | varchar(50) | Yes |  |  |

### RTK_Surveys {dbo-rtk-surveys}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-03-09 08:50:42.330000 |
| **Modified** | 2024-06-21 22:35:13.527000 |
| **Primary Key** | RTKSurveyId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTKSurveyId | uniqueidentifier | No | (newid()) | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | SchoolId | int | Yes |  |  |
| 4 | FacilityId | int | Yes |  |  |
| 5 | FacilityNumber | varchar(20) | Yes |  |  |
| 6 | FacilityName | varchar(50) | Yes |  |  |
| 7 | ReportYear | int | No |  |  |
| 8 | DocumentId | uniqueidentifier | No |  |  |
| 9 | Description | varchar(1024) | No |  |  |
| 10 | ValidFrom | datetime | Yes |  |  |
| 11 | ValidUntil | datetime | Yes |  |  |
| 12 | Created | datetime | No | (getdate()) |  |
| 13 | Updated | datetime | Yes |  |  |
| 14 | Deleted | datetime | Yes |  |  |

### RTK_Training {dbo-rtk-training}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-03-09 08:50:42.317000 |
| **Modified** | 2024-06-21 22:35:13.687000 |
| **Primary Key** | RTKTrainingId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTKTrainingId | uniqueidentifier | No | (newid()) | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | FacilityId | int | Yes |  |  |
| 4 | SchoolId | int | Yes |  |  |
| 5 | UserId | int | Yes |  |  |
| 6 | DocumentId | uniqueidentifier | Yes |  |  |
| 7 | Description | varchar(1024) | No |  |  |
| 8 | ValidFrom | datetime | Yes |  |  |
| 9 | ValidUntil | datetime | Yes |  |  |
| 10 | Created | datetime | No | (getdate()) |  |
| 11 | Updated | datetime | Yes |  |  |
| 12 | Deleted | datetime | Yes |  |  |

### RTK_UOMCodes {dbo-rtk-uomcodes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3 |
| **Created** | 2006-08-29 23:00:43.713000 |
| **Modified** | 2024-06-21 22:35:13.873000 |
| **Primary Key** | UOMCodesID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UOMCodesID | int IDENTITY | No |  | PK |
| 2 | UOMCode | char(1) | No |  |  |
| 3 | Description | varchar(20) | Yes |  |  |

### RTK_VendorLinks {dbo-rtk-vendorlinks}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-03-09 08:50:42.327000 |
| **Modified** | 2024-06-21 22:35:14.010000 |
| **Primary Key** | RTKVendorLinkId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RTKVendorLinkId | uniqueidentifier | No | (newid()) | PK |
| 2 | VendorId | int | No |  |  |
| 3 | VendorName | varchar(50) | No |  |  |
| 4 | Description | varchar(4096) | Yes |  |  |
| 5 | Link | varchar(1024) | Yes |  |  |
| 6 | Created | datetime | No | (getdate()) |  |
| 7 | Updated | datetime | Yes |  |  |
| 8 | Deleted | datetime | Yes |  |  |

### SafetyDataSheets {dbo-safetydatasheets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 157,912 |
| **Created** | 2021-07-23 13:51:01.410000 |
| **Modified** | 2026-03-07 10:04:29.527000 |
| **Primary Key** | SafetyDataSheetId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SafetyDataSheetId | bigint IDENTITY | No |  | PK |
| 2 | SDSURL | varchar(512) | No |  |  |
| 3 | Seq | bigint | Yes |  |  |
| 4 | Created | datetime | No | (getdate()) |  |
| 5 | Updated | datetime | Yes |  |  |
| 6 | Deleted | datetime | Yes |  |  |

### Salutations {dbo-salutations}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5 |
| **Created** | 2011-08-24 15:09:50.197000 |
| **Modified** | 2024-06-21 22:35:14.137000 |
| **Primary Key** | SalutationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SalutationId | int IDENTITY | No |  | PK |
| 2 | Title | varchar(20) | No |  |  |

### SaxDups {dbo-saxdups}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 31,171 |
| **Created** | 2007-04-19 15:19:05.607000 |
| **Modified** | 2021-11-08 21:29:55.637000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BidHeaderId | int | No |  |  |
| 2 | PackedCode | varchar(255) | Yes |  |  |
| 3 | ItemId | int | Yes |  |  |

### SaxNotifications {dbo-saxnotifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 78 |
| **Created** | 2019-04-03 13:05:34.860000 |
| **Modified** | 2021-11-08 21:29:55.657000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RepName | varchar(30) | Yes |  |  |
| 2 | DistrictName | varchar(50) | Yes |  |  |
| 3 | BudgetName | varchar(30) | Yes |  |  |
| 4 | SchoolName | varchar(50) | Yes |  |  |
| 5 | CometId | int | Yes |  |  |
| 6 | UserId | int | No |  |  |
| 7 | EMail | varchar(255) | Yes |  |  |
| 8 | Attention | varchar(50) | Yes |  |  |
| 9 | RequisitionNumber | varchar(24) | Yes |  |  |
| 10 | ItemCode | varchar(50) | Yes |  |  |
| 11 | VendorItemCode | varchar(50) | Yes |  |  |
| 12 | Quantity | int | Yes |  |  |
| 13 | Description | varchar(1024) | Yes |  |  |
| 14 | BidPrice | money | Yes |  |  |
| 15 | RequestedVendorItemCode | varchar(50) | Yes |  |  |
| 16 | RequestedDescription | varchar(1156) | Yes |  |  |

### ScanEvents {dbo-scanevents}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 393,111 |
| **Created** | 2014-04-17 14:37:23.190000 |
| **Modified** | 2024-06-21 22:36:09.003000 |
| **Primary Key** | ScanEventId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ScanEventId | int IDENTITY | No |  | PK |
| 2 | ScanJobId | int | No |  |  |
| 3 | EventStamp | datetime | No | (getdate()) |  |
| 4 | SourceFile | varchar(512) | No |  |  |
| 5 | IndexData | varchar(MAX) | Yes |  |  |
| 6 | EventStatus | varchar(255) | Yes |  |  |

### ScanJobs {dbo-scanjobs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3 |
| **Created** | 2014-04-23 22:28:42.617000 |
| **Modified** | 2021-11-08 07:01:01.550000 |
| **Primary Key** | ScanJobId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ScanJobId | int IDENTITY | No |  | PK |
| 2 | CaptureName | varchar(50) | No |  |  |
| 3 | CabinetName | varchar(50) | No |  |  |
| 4 | SourceFolder | varchar(512) | No |  |  |
| 5 | SplitFolder | varchar(512) | No |  |  |
| 6 | ProcessedFolder | varchar(512) | Yes |  |  |
| 7 | RejectedFolder | varchar(512) | Yes |  |  |
| 8 | CCCaptureJobId | uniqueidentifier | Yes |  |  |
| 9 | CatalogName | varchar(50) | Yes |  |  |

### ScannerZones {dbo-scannerzones}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 10 |
| **Created** | 2014-04-17 11:02:14.320000 |
| **Modified** | 2021-11-08 07:01:01.577000 |
| **Primary Key** | ScannerZoneId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ScannerZoneId | int IDENTITY | No |  | PK |
| 2 | ScanJobId | int | No |  |  |
| 3 | DocTypeFieldRecognitionZoneId | uniqueidentifier | No |  |  |
| 4 | LeftPosition | decimal(7,2) | No |  |  |
| 5 | TopPosition | decimal(7,2) | No |  |  |
| 6 | Width | decimal(7,2) | No |  |  |
| 7 | Height | decimal(7,2) | No |  |  |
| 8 | HorizontalTolerance | decimal(7,2) | No |  |  |
| 9 | VerticalTolerance | decimal(7,2) | No |  |  |

### ScheduledTask {dbo-scheduledtask}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12 |
| **Created** | 2024-12-10 22:48:48.540000 |
| **Modified** | 2024-12-10 22:48:48.540000 |
| **Primary Key** | TaskId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TaskId | int IDENTITY | No |  | PK |
| 2 | TaskName | nvarchar(255) | No |  |  |
| 3 | Description | nvarchar(MAX) | Yes |  |  |
| 4 | ScheduleExpression | nvarchar(255) | No |  |  |
| 5 | TaskType | nvarchar(50) | No |  |  |
| 6 | Status | nvarchar(50) | No | ('Pending') |  |
| 7 | LastRunTime | datetime | Yes |  |  |
| 8 | NextRunTime | datetime | Yes |  |  |
| 9 | MaxRetries | int | No | ((3)) |  |
| 10 | CurrentRetries | int | No | ((0)) |  |
| 11 | CreatedBy | nvarchar(100) | No |  |  |
| 12 | CreatedAt | datetime | No | (getdate()) |  |
| 13 | UpdatedBy | nvarchar(100) | Yes |  |  |
| 14 | UpdatedAt | datetime | Yes |  |  |

### ScheduleTypes {dbo-scheduletypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 10 |
| **Created** | 2006-08-29 23:01:02.853000 |
| **Modified** | 2024-06-21 22:36:10.853000 |
| **Primary Key** | ScheduleId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ScheduleId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Name | varchar(50) | Yes |  |  |
| 5 | StateId | int | Yes |  |  |

### School {dbo-school}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,623 |
| **Created** | 2006-08-30 17:33:09.910000 |
| **Modified** | 2024-06-21 22:41:22.077000 |
| **Primary Key** | SchoolId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SchoolId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  | FK → dbo.District.DistrictId |
| 3 | Active | tinyint | Yes |  |  |
| 4 | Name | varchar(50) | Yes |  |  |
| 5 | Address1 | varchar(30) | Yes |  |  |
| 6 | Address2 | varchar(30) | Yes |  |  |
| 7 | Address3 | varchar(30) | Yes |  |  |
| 8 | City | varchar(25) | Yes |  |  |
| 9 | State | varchar(2) | Yes |  |  |
| 10 | Zipcode | varchar(10) | Yes |  |  |
| 11 | BillingId | int | Yes |  |  |
| 12 | ShippingId | int | Yes |  |  |
| 13 | PhoneNumber | varchar(20) | Yes |  |  |
| 14 | Fax | varchar(20) | Yes |  |  |
| 15 | EMail | varchar(255) | Yes |  |  |
| 16 | LocationCode | varchar(32) | Yes |  |  |
| 18 | AddressId | int | Yes |  |  |

### SDS_Rpt_Bridge {dbo-sds-rpt-bridge}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 100 |
| **Created** | 2022-02-22 07:57:48.353000 |
| **Modified** | 2022-02-22 07:59:18.443000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SessionId | int | No |  |  |
| 2 | ItemId | int | No |  |  |
| 3 | SDSDoc | varchar(500) | No |  |  |

### SDSDocs {dbo-sdsdocs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 161,387 |
| **Created** | 2019-02-19 16:36:23.917000 |
| **Modified** | 2024-06-21 22:36:11.233000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | uniqueidentifier | No | (newid()) | PK |
| 2 | ItemId | int | No |  |  |
| 3 | CrossRefId | int | Yes |  |  |
| 4 | MSDSId | int | Yes |  |  |
| 5 | OrigURL | varchar(1024) | Yes |  |  |
| 6 | DateLoaded | datetime | Yes | (getdate()) |  |
| 7 | DateChecked | datetime | Yes | (getdate()) |  |
| 8 | Checksum | bigint | Yes |  |  |
| 9 | DocType | varchar(50) | Yes |  |  |
| 10 | Document | varbinary(MAX) | Yes |  |  |
| 11 | Description | varchar(255) | Yes |  |  |
| 12 | Manufacturer | varchar(255) | Yes |  |  |

### SDSErrors {dbo-sdserrors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2021-06-07 12:36:52.913000 |
| **Modified** | 2024-06-21 22:36:12.560000 |
| **Primary Key** | sdsErrorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | sdsErrorId | bigint IDENTITY | No |  | PK |
| 2 | sdsURL | varchar(512) | Yes |  |  |
| 3 | error | varchar(MAX) | Yes |  |  |
| 4 | logDate | datetime | Yes | (getdate()) |  |

### SDSLog {dbo-sdslog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2021-06-07 12:36:52.920000 |
| **Modified** | 2024-06-21 22:36:14.577000 |
| **Primary Key** | sdsLogId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | sdsLogId | bigint IDENTITY | No |  | PK |
| 2 | sdsURL | varchar(512) | Yes |  |  |
| 3 | statusCode | int | Yes |  |  |
| 4 | statusText | varchar(512) | Yes |  |  |
| 5 | contentType | varchar(50) | Yes |  |  |
| 6 | headers | varchar(MAX) | Yes |  |  |
| 7 | testDate | datetime | Yes | (getdate()) |  |
| 8 | writeStatus | int | Yes |  |  |
| 9 | writeDate | datetime | Yes |  |  |

### SDSResults {dbo-sdsresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 116,893 |
| **Created** | 2025-05-02 13:47:54.090000 |
| **Modified** | 2025-05-02 13:47:54.090000 |
| **Primary Key** | SDSResultsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SDSResultsId | int IDENTITY | No |  | PK |
| 2 | SafetyDataSheetId | int | No |  |  |
| 3 | SDSURL | varchar(512) | Yes |  |  |
| 4 | SDSCacheURL | varchar(512) | Yes |  |  |
| 5 | DocumentType | varchar(128) | Yes |  |  |
| 6 | DocumentURL | varchar(512) | Yes |  |  |
| 7 | ValidCache | bit | Yes |  |  |
| 8 | ValidSDSUrl | bit | Yes |  |  |
| 9 | ValidDocumentURL | bit | Yes |  |  |
| 10 | ValidElasticText | bit | Yes |  |  |
| 11 | SDSCacheError | varchar(1024) | Yes |  |  |
| 12 | SDSURLError | varchar(1024) | Yes |  |  |
| 13 | DocumentURLError | varchar(1024) | Yes |  |  |
| 14 | ElasticError | varchar(1024) | Yes |  |  |

### SDSs {dbo-sdss}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2021-06-07 12:36:52.910000 |
| **Modified** | 2024-06-21 22:36:14.817000 |
| **Primary Key** | sdsId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | sdsId | bigint IDENTITY | No |  | PK |
| 2 | sdsURL | varchar(512) | Yes |  |  |
| 3 | sdsPath | varchar(512) | Yes |  |  |
| 4 | sdsHash | bigint | Yes |  |  |
| 5 | dateLoaded | datetime | Yes | (getdate()) |  |
| 6 | dateChecked | datetime | Yes | (getdate()) |  |
| 7 | dateDeleted | datetime | Yes |  |  |

### SDSSyncStatus {dbo-sdssyncstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 26,483 |
| **Created** | 2024-12-15 19:31:46 |
| **Modified** | 2024-12-16 23:12:04.147000 |
| **Primary Key** | SafetyDataSheetId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SafetyDataSheetId | int | No |  | PK |
| 2 | TotalItems | int | Yes |  |  |
| 3 | TotalRequisitions | int | Yes |  |  |
| 4 | SyncedItems | int | No | ((0)) |  |
| 5 | SyncedRequisitions | int | No | ((0)) |  |
| 6 | SyncStatus | varchar(50) | No | ('New') |  |
| 7 | CreatedAt | datetime | No | (getdate()) |  |
| 8 | UpdatedAt | datetime | Yes |  |  |
| 9 | LastSyncedAt | datetime | Yes |  |  |
| 10 | ItemSyncStatus | varchar(50) | Yes |  |  |
| 11 | RequisitionSyncStatus | varchar(50) | Yes |  |  |
| 12 | StartSyncAt | datetime | Yes |  |  |
| 13 | EndSyncAt | datetime | Yes |  |  |

### SearchKeywords {dbo-searchkeywords}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2017-12-06 07:12:56.547000 |
| **Modified** | 2024-06-21 22:36:15.370000 |
| **Primary Key** | SearchKeywordId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SearchKeywordId | uniqueidentifier | No | (newid()) | PK |
| 2 | ItemId | int | No |  |  |
| 3 | CrossRefId | int | No |  |  |
| 4 | Keyword | varchar(50) | Yes |  |  |

### SearchSets {dbo-searchsets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 44,292 |
| **Created** | 2006-08-30 17:32:05.753000 |
| **Modified** | 2021-11-08 21:29:55.680000 |
| **Primary Key** | SSId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SSId | int IDENTITY | No |  | PK |
| 2 | SessionId | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 4 | CatalogId | int | Yes |  |  |
| 5 | SearchBy | int | Yes |  |  |
| 6 | SearchStart | varchar(255) | Yes |  |  |
| 7 | SearchEnd | varchar(255) | Yes |  |  |

### Sections {dbo-sections}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 18 |
| **Created** | 2006-08-30 17:31:35.333000 |
| **Modified** | 2024-06-21 22:36:15.470000 |
| **Primary Key** | SectionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SectionId | int IDENTITY | No |  | PK |
| 2 | CategoryId | int | Yes |  |  |
| 3 | Description | varchar(50) | Yes |  |  |

### SecurityKeys {dbo-securitykeys}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14 |
| **Created** | 2012-06-01 17:30:29.887000 |
| **Modified** | 2024-06-21 22:36:15.773000 |
| **Primary Key** | SecurityKeyID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SecurityKeyID | int IDENTITY | No |  | PK |
| 2 | KeyName | varchar(100) | No |  |  |
| 3 | KeyDescription | varchar(255) | Yes |  |  |

### SecurityRoleKeys {dbo-securityrolekeys}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 65 |
| **Created** | 2012-06-01 17:29:16.367000 |
| **Modified** | 2024-06-21 22:36:15.947000 |
| **Primary Key** | SecurityRoleKeyID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SecurityRoleKeyID | int IDENTITY | No |  | PK |
| 2 | SecurityKeyID | int | Yes |  |  |
| 3 | SecurityRoleID | int | Yes |  |  |

### SecurityRoles {dbo-securityroles}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5 |
| **Created** | 2010-01-08 13:49:41.680000 |
| **Modified** | 2024-06-21 22:36:16.167000 |
| **Primary Key** | SecurityRoleId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SecurityRoleId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Name | varchar(50) | No |  |  |

### SecurityRoleUsers {dbo-securityroleusers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 361,518 |
| **Created** | 2011-07-15 17:43:46.190000 |
| **Modified** | 2024-06-21 22:36:30.163000 |
| **Primary Key** | SecurityRoleUserId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SecurityRoleUserId | int IDENTITY | No |  | PK |
| 2 | SecurityRoleId | int | No |  |  |
| 3 | UserId | int | No |  |  |

### Services {dbo-services}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-04-16 13:30:40.170000 |
| **Modified** | 2024-06-21 22:36:30.393000 |
| **Primary Key** | ServiceId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ServiceId | int IDENTITY | No |  | PK |
| 2 | ParentId | int | Yes |  |  |
| 3 | TradeId | int | Yes |  |  |
| 4 | Active | tinyint | Yes |  |  |
| 5 | Description | varchar(50) | Yes |  |  |
| 6 | BidQuantity | decimal(9,5) | No |  |  |
| 7 | RateTypeId | tinyint | No |  |  |
| 8 | RateUnitId | int | No |  |  |
| 9 | Comments | text | Yes |  |  |

### SessionCmds {dbo-sessioncmds}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-01-12 12:24:49.063000 |
| **Modified** | 2024-06-21 22:36:30.727000 |
| **Primary Key** | SessionCmdId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SessionCmdId | int IDENTITY | No |  | PK |
| 2 | SessionId | int | No |  |  |
| 3 | EventDate | datetime | Yes | (getdate()) |  |
| 4 | Command | varchar(4096) | Yes |  |  |

### SessionTable {dbo-sessiontable}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 12,606,615 |
| **Created** | 2006-08-29 23:01:57.947000 |
| **Modified** | 2025-04-16 02:54:40.350000 |
| **Primary Key** | SessionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SessionId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | SchoolId | int | Yes |  |  |
| 4 | UserId | int | No |  |  |
| 5 | RequisitionId | int | Yes |  |  |
| 6 | POId | int | Yes |  |  |
| 7 | BudgetId | int | Yes |  |  |
| 8 | ReqMode | int | Yes |  |  |
| 9 | OrderBy | int | Yes |  |  |
| 10 | CatalogId | int | Yes |  |  |
| 11 | Mode | int | Yes |  |  |
| 12 | SessionStart | datetime | Yes | (getdate()) |  |
| 13 | SessionEnd | datetime | Yes |  |  |
| 14 | SessionLast | datetime | Yes |  |  |
| 15 | CSRepId | int | Yes |  |  |
| 16 | RepUserId | int | Yes |  |  |
| 17 | ApprovalLevel | tinyint | Yes |  |  |
| 18 | Attention | varchar(50) | Yes |  |  |
| 19 | ResolutionX | int | Yes |  |  |
| 20 | ResolutionY | int | Yes |  |  |
| 21 | TabSelected | varchar(32) | Yes |  |  |
| 22 | ReloadPage | tinyint | Yes |  |  |
| 23 | TempUserId | int | Yes |  |  |
| 24 | CurrentBudgetId | int | Yes |  |  |
| 25 | NextBudgetId | int | Yes |  |  |
| 26 | AllowIncidentals | tinyint | Yes |  |  |
| 30 | VendorId | int | Yes |  |  |

### ShipLocations {dbo-shiplocations}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,909 |
| **Created** | 2009-08-31 11:56:26.453000 |
| **Modified** | 2024-06-21 22:39:14.830000 |
| **Primary Key** | ShippingId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ShippingId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | Name | varchar(50) | Yes |  |  |
| 5 | Address1 | varchar(30) | Yes |  |  |
| 6 | Address2 | varchar(30) | Yes |  |  |
| 7 | Address3 | varchar(30) | Yes |  |  |
| 8 | City | varchar(25) | Yes |  |  |
| 9 | State | varchar(2) | Yes |  |  |
| 10 | ZipCode | varchar(10) | Yes |  |  |
| 11 | Phone | varchar(20) | Yes |  |  |
| 12 | Fax | varchar(14) | Yes |  |  |
| 13 | EMail | varchar(255) | Yes |  |  |
| 14 | LocationCode | varchar(32) | Yes |  |  |
| 15 | RTK_SitesId | int | Yes |  |  |

### ShippingCosts {dbo-shippingcosts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,045 |
| **Created** | 2022-01-30 23:02:02.520000 |
| **Modified** | 2024-06-21 21:35:32.707000 |
| **Primary Key** | ShippingCostId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ShippingCostId | int IDENTITY | No |  | PK |
| 2 | DetailId | int | No |  |  |
| 3 | RequisitionId | int | No |  |  |
| 4 | ShippingRequestId | int | Yes |  |  |
| 5 | DateUpdated | datetime | No | (getdate()) |  |
| 6 | Quantity | int | Yes |  |  |
| 7 | Cost | decimal(9,2) | Yes |  |  |
| 8 | UpdatedBy | varchar(50) | Yes |  |  |

### ShippingRequests {dbo-shippingrequests}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 694 |
| **Created** | 2022-01-30 23:02:02.897000 |
| **Modified** | 2024-06-21 21:35:38.097000 |
| **Primary Key** | ShippingRequestId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ShippingRequestId | int IDENTITY | No |  | PK |
| 2 | ShippingRequestUniqueId | uniqueidentifier | No | (newid()) |  |
| 3 | RequisitionId | int | No |  |  |
| 4 | VendorId | int | No |  |  |
| 5 | EmailAddresses | varchar(4096) | No |  |  |
| 6 | Comments | varchar(4096) | Yes |  |  |
| 7 | RequestSent | datetime | No | (getdate()) |  |
| 8 | RequestCompleted | datetime | Yes |  |  |
| 9 | CompletedBy | varchar(50) | Yes |  |  |
| 10 | RequestStatus | varchar(50) | Yes |  |  |
| 11 | loadingDock | tinyint | Yes |  |  |

### ShippingVendor {dbo-shippingvendor}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 38,754 |
| **Created** | 2009-04-13 20:46:41.360000 |
| **Modified** | 2024-06-21 22:39:16.673000 |
| **Primary Key** | ShippingVendorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | ShippingVendorId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | VendorId | int | No |  |  |
| 4 | ShippingId | int | No |  |  |
| 5 | ShippingCode | varchar(50) | Yes |  |  |

### SSOLoginTracking {dbo-ssologintracking}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 156,019 |
| **Created** | 2025-01-15 21:59:00.060000 |
| **Modified** | 2026-03-21 03:52:07.930000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SSOProvider | varchar(50) | No |  |  |
| 2 | Email | varchar(255) | Yes |  |  |
| 3 | Action | varchar(100) | Yes |  |  |
| 4 | InsertAt | datetime | Yes | (getdate()) |  |
| 5 | ErrorMsg | varchar(255) | Yes |  |  |
| 6 | Description | varchar(MAX) | Yes |  |  |

### States {dbo-states}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3 |
| **Created** | 2006-08-29 23:02:35.417000 |
| **Modified** | 2024-06-21 22:39:17.680000 |
| **Primary Key** | StateId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | StateId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Name | varchar(50) | Yes |  |  |
| 5 | code | char(2) | Yes |  |  |

### StatusTable {dbo-statustable}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 53 |
| **Created** | 2006-08-30 17:29:08.240000 |
| **Modified** | 2024-06-21 22:39:17.897000 |
| **Primary Key** | StatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | StatusId | int IDENTITY | No |  | PK |
| 2 | StatusCode | char(1) | Yes |  |  |
| 3 | Name | varchar(50) | Yes |  |  |
| 4 | RequiredLevel | tinyint | Yes |  |  |
| 5 | OptionValue | int | Yes |  |  |
| 6 | UserVisibilityLevel | int | Yes |  |  |
| 8 | IsPrint | bit | Yes |  |  |
| 9 | ScriptURL | varchar(1024) | Yes |  |  |

### Sulphite {dbo-sulphite}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 49 |
| **Created** | 2018-03-26 15:45:17.037000 |
| **Modified** | 2021-11-08 21:29:55.707000 |
| **Primary Key** | SulphiteId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SulphiteId | int IDENTITY | No |  | PK |
| 2 | VendorItemCode | varchar(50) | No |  |  |
| 3 | ItemCode | varchar(50) | No |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | Z2Exclude | tinyint | Yes |  |  |

### SulphiteDetail {dbo-sulphitedetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,280 |
| **Created** | 2018-03-26 17:14:24.290000 |
| **Modified** | 2021-11-08 21:29:55.727000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | DetailId | int | No |  |  |
| 2 | vendorItemCode | varchar(50) | Yes |  |  |
| 3 | ItemCode | varchar(50) | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |

### SulphiteImport {dbo-sulphiteimport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 49 |
| **Created** | 2018-03-26 15:37:54.043000 |
| **Modified** | 2021-11-08 21:29:55.753000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Cascade item number | nvarchar(255) | Yes |  |  |
| 2 | Description | nvarchar(255) | Yes |  |  |
| 3 | Ed Data code number | nvarchar(255) | Yes |  |  |
| 4 | Suggested alternate | nvarchar(255) | Yes |  |  |
| 5 | ED-DATA item code | nvarchar(255) | Yes |  |  |

### SulphiteUsers {dbo-sulphiteusers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,209 |
| **Created** | 2018-03-26 17:05:05.260000 |
| **Modified** | 2021-11-08 21:29:55.783000 |
| **Primary Key** | SulphiteUserId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SulphiteUserId | int IDENTITY | No |  | PK |
| 2 | UserId | int | No |  |  |

### Suppression {dbo-suppression}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,301 |
| **Created** | 2024-08-10 03:07:42.553000 |
| **Modified** | 2024-08-10 03:07:42.990000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | int IDENTITY | No |  | PK |
| 2 | Email | varchar(100) | Yes |  |  |
| 3 | Type | varchar(50) | Yes |  |  |
| 4 | District | varchar(100) | Yes |  |  |
| 5 | Locator | varchar(200) | Yes |  |  |
| 6 | Phone | varchar(20) | Yes |  |  |
| 7 | Reason | varchar(300) | Yes |  |  |
| 8 | Handled | bit | Yes | ((1)) |  |
| 9 | CreatedAt | datetime | Yes | (getdate()) |  |
| 10 | UpdatedAt | datetime | Yes |  |  |
| 11 | CreatedBy | int | Yes | ((0)) |  |
| 12 | UpdatedBy | int | Yes | ((0)) |  |
| 13 | BelongsTo | varchar(50) | Yes |  |  |
| 14 | SuppressionType | varchar(50) | Yes |  |  |
| 15 | SuppressionAt | datetime | Yes |  |  |

### sysdiagrams {dbo-sysdiagrams}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 9 |
| **Created** | 2009-03-26 16:18:10.473000 |
| **Modified** | 2021-11-08 07:01:22.873000 |
| **Primary Key** | diagram_id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | name | sysname | No |  |  |
| 2 | principal_id | int | No |  |  |
| 3 | diagram_id | int IDENTITY | No |  | PK |
| 4 | version | int | Yes |  |  |
| 5 | definition | varbinary(MAX) | Yes |  |  |

### TableOfContents {dbo-tableofcontents}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2007-09-06 23:53:16.937000 |
| **Modified** | 2024-06-21 22:39:18.417000 |
| **Primary Key** | TCId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TCId | int IDENTITY | No |  | PK |
| 2 | Title | varchar(255) | Yes |  |  |
| 3 | PageNbr | int | Yes |  |  |
| 4 | OrderBookId | int | Yes |  |  |

### TagFile_ {dbo-tagfile-}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,235 |
| **Created** | 2001-08-24 14:40:32.357000 |
| **Modified** | 2020-11-17 18:15:56.337000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Usr | int | Yes |  |  |
| 2 | Tbl | int | Yes |  |  |
| 3 | Ptr | int | Yes |  |  |
| 4 | Val | char(10) | Yes |  |  |

### TAGFILEP {dbo-tagfilep}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2001-08-24 14:40:32.337000 |
| **Modified** | 2020-11-17 18:15:57.263000 |
| **Primary Key** | USR, TBL, POS |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | USR | int | No |  | PK |
| 2 | TBL | smallint | No |  | PK |
| 3 | POS | char(256) | No |  | PK |
| 4 | VAL | char(10) | Yes |  |  |

### TagFilePos_ {dbo-tagfilepos-}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,259 |
| **Created** | 2001-08-24 14:40:32.347000 |
| **Modified** | 2020-11-17 18:15:57.450000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Usr | int | Yes |  |  |
| 2 | Tbl | int | Yes |  |  |
| 3 | Pos | char(256) | Yes |  |  |
| 4 | Val | char(10) | Yes |  |  |

### TagSet_ {dbo-tagset-}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2001-08-24 14:40:32.367000 |
| **Modified** | 2020-11-17 18:15:57.607000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Tbl | int | Yes |  |  |
| 2 | Usr | int | Yes |  |  |
| 3 | Source | char(50) | Yes |  |  |
| 4 | Date | int | Yes |  |  |
| 5 | Count | int | Yes |  |  |
| 6 | Description | char(250) | Yes |  |  |

### TaskEvent {dbo-taskevent}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 122,104 |
| **Created** | 2006-08-29 23:03:04.713000 |
| **Modified** | 2024-06-21 22:39:20.327000 |
| **Primary Key** | TaskEventId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TaskEventId | int IDENTITY | No |  | PK |
| 2 | ProjectTaskId | int | Yes |  |  |
| 3 | EventDate | datetime | Yes |  |  |
| 4 | BidDate | datetime | Yes |  |  |
| 5 | DistrictId | int | Yes |  |  |
| 6 | CategoryId | int | Yes |  |  |
| 7 | UserId | int | Yes |  |  |
| 8 | ValueField | varchar(20) | Yes |  |  |

### TaskSchedule {dbo-taskschedule}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,554,438 |
| **Created** | 2006-08-30 17:28:00.503000 |
| **Modified** | 2024-06-21 21:57:49.723000 |
| **Primary Key** | TaskScheduleId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TaskScheduleId | int IDENTITY | No |  | PK |
| 2 | ProjectTasksId | int | No |  |  |
| 3 | TaskSeqNum | int | No |  |  |
| 4 | StartDateOrig | datetime | Yes |  |  |
| 5 | EndDateOrig | datetime | Yes |  |  |
| 6 | StartDateProjected | datetime | Yes |  |  |
| 7 | EndDateProjected | datetime | Yes |  |  |
| 8 | StartDateActual | datetime | Yes |  |  |
| 9 | EndDateActual | datetime | Yes |  |  |
| 10 | BidCycleDate | datetime | Yes |  |  |
| 11 | DistrictId | int | Yes |  |  |
| 12 | CategoryId | int | Yes |  |  |
| 13 | UserId | int | Yes |  |  |
| 14 | PricePlanId | int | Yes |  |  |
| 15 | SessionId | int | Yes |  |  |

### TempIrvingtonWincap {dbo-tempirvingtonwincap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 860 |
| **Created** | 2016-03-09 17:35:37.703000 |
| **Modified** | 2024-06-21 22:39:20.483000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Approver | nvarchar(255) | Yes |  |  |
| 2 | Rqst ID | nvarchar(255) | Yes |  |  |
| 3 | F3 | nvarchar(255) | Yes |  |  |
| 4 | Description | nvarchar(255) | Yes |  |  |
| 5 | Employee ID | nvarchar(255) | Yes |  |  |
| 6 | Req ID | nvarchar(255) | Yes |  |  |
| 7 | F7 | nvarchar(255) | Yes |  |  |
| 8 | F8 | nvarchar(255) | Yes |  |  |
| 9 | F9 | nvarchar(255) | Yes |  |  |
| 10 | Building | nvarchar(255) | Yes |  |  |
| 11 | F11 | nvarchar(255) | Yes |  |  |
| 12 | Dept for Apprvl | nvarchar(255) | Yes |  |  |
| 13 | Position (Linked)e | nvarchar(255) | Yes |  |  |
| 14 | HR Location | nvarchar(255) | Yes |  |  |
| 15 | Grade/Level | nvarchar(255) | Yes |  |  |
| 16 | Supervisor | nvarchar(255) | Yes |  |  |
| 17 | Default Fund | nvarchar(255) | Yes |  |  |
| 18 | Default Budgetcode | nvarchar(255) | Yes |  |  |
| 19 | Invoice Address | nvarchar(255) | Yes |  |  |
| 20 | F20 | nvarchar(255) | Yes |  |  |
| 21 | Shipping Address | nvarchar(255) | Yes |  |  |
| 22 | Stock Request Ship To | nvarchar(255) | Yes |  |  |
| 23 | F23 | nvarchar(255) | Yes |  |  |
| 24 | F24 | nvarchar(255) | Yes |  |  |
| 25 | Email | nvarchar(255) | Yes |  |  |
| 26 | EOL | nvarchar(255) | Yes |  |  |

### TM_UOM {dbo-tm-uom}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 77 |
| **Created** | 2011-11-03 15:13:08.063000 |
| **Modified** | 2024-06-21 22:39:20.720000 |
| **Primary Key** | TM_UOMId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TM_UOMId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(50) | No |  |  |

### TMAwards {dbo-tmawards}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 94,281 |
| **Created** | 2012-03-02 09:32:44.080000 |
| **Modified** | 2026-03-20 11:38:59.790000 |
| **Primary Key** | TMAwardId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMAwardId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | BidHeaderId | int | No |  |  |
| 4 | BidTradeCountyId | int | No |  |  |
| 5 | BidImportId | int | Yes |  |  |
| 6 | VendorId | int | Yes |  |  |
| 7 | AwardType | varchar(50) | Yes |  |  |
| 8 | DateModified | datetime | Yes | (getdate()) |  |
| 9 | AwardAmount | money | Yes |  |  |

### TMImport {dbo-tmimport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3,114 |
| **Created** | 2011-10-14 11:44:20.223000 |
| **Modified** | 2024-06-21 21:57:25.300000 |
| **Primary Key** | TMImportId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMImportId | int IDENTITY | No |  | PK |
| 2 | State | char(2) | No |  |  |
| 3 | County | varchar(50) | No |  |  |
| 4 | Package | varchar(50) | No |  |  |
| 5 | Level | int | No |  |  |
| 6 | VendorName | varchar(255) | No |  |  |
| 7 | TradeId | int | Yes |  |  |

### TMImport1 {dbo-tmimport1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,885 |
| **Created** | 2011-10-27 15:35:27.777000 |
| **Modified** | 2018-03-19 17:18:48.310000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMImportId | int IDENTITY | No |  |  |
| 2 | State | char(2) | No |  |  |
| 3 | County | varchar(50) | No |  |  |
| 4 | Package | varchar(50) | No |  |  |
| 5 | Level | int | No |  |  |
| 6 | VendorName | varchar(255) | No |  |  |
| 7 | TradeId | int | Yes |  |  |

### TMImport2 {dbo-tmimport2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 147 |
| **Created** | 2011-10-27 15:56:41.680000 |
| **Modified** | 2018-03-19 17:18:48.350000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMImportId | int IDENTITY | No |  |  |
| 2 | State | char(2) | No |  |  |
| 3 | County | varchar(50) | No |  |  |
| 4 | Package | varchar(50) | No |  |  |
| 5 | Level | int | No |  |  |
| 6 | VendorName | varchar(255) | No |  |  |
| 7 | TradeId | int | Yes |  |  |

### TMImport3 {dbo-tmimport3}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 833 |
| **Created** | 2011-10-27 16:33:44.750000 |
| **Modified** | 2018-03-19 17:18:48.383000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMImportId | int IDENTITY | No |  |  |
| 2 | State | char(2) | No |  |  |
| 3 | County | varchar(50) | No |  |  |
| 4 | Package | varchar(50) | No |  |  |
| 5 | Level | int | No |  |  |
| 6 | VendorName | varchar(255) | No |  |  |
| 7 | TradeId | int | Yes |  |  |

### TMImport5 {dbo-tmimport5}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,889 |
| **Created** | 2011-10-31 22:28:01.823000 |
| **Modified** | 2018-03-19 17:18:48.417000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMImportId | int IDENTITY | No |  |  |
| 2 | State | char(2) | No |  |  |
| 3 | County | varchar(50) | No |  |  |
| 4 | Package | varchar(50) | No |  |  |
| 5 | Level | int | No |  |  |
| 6 | VendorName | varchar(255) | No |  |  |
| 7 | TradeId | int | Yes |  |  |

### TMImport6 {dbo-tmimport6}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2,134 |
| **Created** | 2011-10-31 22:48:02.790000 |
| **Modified** | 2018-03-19 17:18:48.457000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMImportId | int IDENTITY | No |  |  |
| 2 | State | char(2) | No |  |  |
| 3 | County | varchar(50) | No |  |  |
| 4 | Package | varchar(50) | No |  |  |
| 5 | Level | int | No |  |  |
| 6 | VendorName | varchar(255) | No |  |  |
| 7 | TradeId | int | Yes |  |  |

### TmpLog {dbo-tmplog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 461 |
| **Created** | 2021-08-14 09:42:05.550000 |
| **Modified** | 2021-08-14 09:42:05.557000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TmpLogID | int IDENTITY | No |  |  |
| 2 | LogDateTime | datetime | Yes | (getdate()) |  |

### TmpTaskSchedule {dbo-tmptaskschedule}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4,898 |
| **Created** | 2004-11-08 19:44:04.367000 |
| **Modified** | 2021-11-08 07:01:25.447000 |
| **Primary Key** | TmpTaskScheduleId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TmpTaskScheduleId | int IDENTITY | No |  | PK |
| 2 | SessionId | int | No |  |  |
| 3 | ProjectTasksId | int | No |  |  |
| 4 | TaskSeqNum | int | Yes |  |  |
| 5 | TaskDescription | varchar(60) | Yes |  |  |
| 6 | StartDate | datetime | Yes |  |  |
| 7 | EndDate | datetime | Yes |  |  |

### TMSurvey {dbo-tmsurvey}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 862 |
| **Created** | 2011-10-13 17:10:18.097000 |
| **Modified** | 2024-06-21 22:39:20.873000 |
| **Primary Key** | TMSurveyId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMSurveyId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | No |  |  |
| 3 | Submitter | varchar(255) | Yes |  |  |
| 4 | Title | varchar(255) | Yes |  |  |
| 5 | Email | varchar(255) | Yes |  |  |
| 6 | Started | datetime | Yes |  |  |
| 7 | Finished | datetime | Yes |  |  |
| 8 | CountyId | int | Yes |  |  |

### TMSurveyNewTrades {dbo-tmsurveynewtrades}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 89 |
| **Created** | 2011-10-13 16:53:52.583000 |
| **Modified** | 2024-06-21 22:39:21.100000 |
| **Primary Key** | TMSurveyNewTradeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMSurveyNewTradeId | int IDENTITY | No |  | PK |
| 2 | TMSurveyId | int | No |  |  |
| 3 | TradeName | varchar(255) | Yes |  |  |
| 4 | TradeDescription | varchar(MAX) | Yes |  |  |

### TMSurveyNewVendors {dbo-tmsurveynewvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 202 |
| **Created** | 2011-10-13 16:53:52.600000 |
| **Modified** | 2024-06-21 22:39:21.437000 |
| **Primary Key** | TMSurveyNewVendorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMSurveyNewVendorId | int IDENTITY | No |  | PK |
| 2 | TMSurveyId | int | No |  |  |
| 3 | TradeName | varchar(50) | Yes |  |  |
| 4 | VendorName | varchar(50) | Yes |  |  |
| 5 | Address1 | varchar(50) | Yes |  |  |
| 6 | Address2 | varchar(50) | Yes |  |  |
| 7 | City | varchar(50) | Yes |  |  |
| 8 | State | char(2) | Yes |  |  |
| 9 | Zipcode | varchar(10) | Yes |  |  |
| 10 | ContactName | varchar(50) | Yes |  |  |
| 11 | EMail | varchar(255) | Yes |  |  |
| 12 | Phone | varchar(20) | Yes |  |  |
| 13 | Fax | varchar(20) | Yes |  |  |

### TMSurveyResults {dbo-tmsurveyresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 98,340 |
| **Created** | 2018-07-25 21:32:41.437000 |
| **Modified** | 2024-06-21 21:57:34.887000 |
| **Primary Key** | TMSurveyResultId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMSurveyResultId | int IDENTITY | No |  | PK |
| 2 | TMSurveyId | int | No |  |  |
| 3 | TMVendorId | int | No |  |  |
| 4 | BidTradeCountyId | int | Yes |  |  |
| 5 | Rating | int | Yes |  |  |
| 6 | Comments | varchar(MAX) | Yes |  |  |
| 7 | Updated | datetime | Yes |  |  |

### TMVendors {dbo-tmvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 16,173 |
| **Created** | 2011-10-13 16:53:52.463000 |
| **Modified** | 2024-06-21 21:57:38.230000 |
| **Primary Key** | TMVendorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TMVendorId | int IDENTITY | No |  | PK |
| 2 | TMYear | int | No |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | VendorName | varchar(50) | Yes |  |  |
| 5 | TradeId | int | No |  |  |
| 6 | CountyId | int | No |  |  |
| 7 | Sequence | int | Yes |  |  |
| 18 | BidTradeId | int | Yes |  |  |

### TopUOM {dbo-topuom}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 4,579 |
| **Created** | 2006-08-31 11:08:40.277000 |
| **Modified** | 2024-06-21 22:39:21.933000 |
| **Primary Key** | TopUOMId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TopUOMId | int IDENTITY | No |  | PK |
| 2 | CategoryId | int | Yes |  |  |
| 3 | UnitId | int | Yes |  |  |

### Trades {dbo-trades}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 107 |
| **Created** | 2011-10-13 18:22:28.323000 |
| **Modified** | 2026-03-20 11:46:21.857000 |
| **Primary Key** | TradeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TradeId | int IDENTITY | No |  | PK |
| 2 | ParentId | int | Yes |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | Description | varchar(255) | Yes |  |  |
| 5 | Comments | text | Yes |  |  |
| 6 | PackageNumber | int | Yes |  |  |
| 20 | pwRequired | tinyint | Yes |  |  |

### TransactionLog_HISTORY {dbo-transactionlog-history}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 112,818,137 |
| **Created** | 2020-08-10 09:12:14.540000 |
| **Modified** | 2026-03-14 04:52:24.497000 |
| **Primary Key** | SysId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SysId | uniqueidentifier | No |  | PK |
| 2 | RequestStart | datetime2 | No |  |  |
| 3 | RequestEnd | datetime2 | Yes |  |  |
| 4 | SessionId | varchar(64) | Yes |  |  |
| 5 | TargetServer | varchar(64) | Yes |  |  |
| 6 | URL | varchar(2014) | Yes |  |  |
| 7 | Headers | varchar(MAX) | Yes |  |  |
| 8 | Content | varchar(MAX) | Yes |  |  |
| 9 | Method | varchar(50) | Yes |  |  |
| 10 | Protocol | varchar(255) | Yes |  |  |

### TransactionLogCF {dbo-transactionlogcf}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 33,060,183 |
| **Created** | 2016-04-11 21:11:33.247000 |
| **Modified** | 2026-03-14 11:16:00.187000 |
| **Primary Key** | SysId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SysId | uniqueidentifier | No | (newid()) | PK |
| 2 | RequestStart | datetime2 | Yes | (sysdatetime()) |  |
| 3 | RequestEnd | datetime2 | Yes |  |  |
| 4 | SessionId | varchar(64) | Yes |  |  |
| 5 | TargetServer | varchar(64) | Yes |  |  |
| 6 | URL | varchar(2014) | Yes |  |  |
| 7 | Headers | varchar(MAX) | Yes |  |  |
| 8 | Content | varchar(MAX) | Yes |  |  |
| 9 | Method | varchar(50) | Yes |  |  |
| 10 | Protocol | varchar(255) | Yes |  |  |

### TransactionTypes {dbo-transactiontypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 23:03:43.230000 |
| **Modified** | 2024-06-21 22:39:22.177000 |
| **Primary Key** | TransactionTypeId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TransactionTypeId | int IDENTITY | No |  | PK |
| 2 | Description | varchar(255) | No |  |  |
| 3 | Credit | tinyint | Yes |  |  |

### TransmitLog {dbo-transmitlog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 152,627 |
| **Created** | 2018-11-28 15:13:00.157000 |
| **Modified** | 2026-03-14 09:47:32.447000 |
| **Primary Key** | TransmitId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TransmitId | uniqueidentifier | No | (newid()) | PK |
| 2 | DateStamp | datetime2 | Yes | (getdate()) |  |
| 3 | RequestURL | varchar(1024) | Yes |  |  |
| 4 | RequestParams | varchar(2048) | Yes |  |  |
| 5 | RequestData | varchar(MAX) | Yes |  |  |

### Units {dbo-units}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11,233 |
| **Created** | 2006-08-30 17:23:23.077000 |
| **Modified** | 2024-06-21 22:39:23.587000 |
| **Primary Key** | UnitId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UnitId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Code | varchar(20) | Yes |  |  |

### UNSPSCs {dbo-unspscs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 50,317 |
| **Created** | 2020-12-17 11:33:06.787000 |
| **Modified** | 2021-11-08 21:29:55.830000 |
| **Primary Key** | UNSPSCId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UNSPSCId | int | No |  | PK |
| 2 | Code | varchar(10) | No |  |  |
| 3 | Description | varchar(255) | No |  |  |

### UnsubscriptionEmail {dbo-unsubscriptionemail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2024-07-26 04:36:05.763000 |
| **Modified** | 2024-08-01 03:14:55.203000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | int IDENTITY | No |  | PK |
| 2 | Email | varchar(255) | Yes |  |  |
| 3 | CreatedAt | datetime | Yes | (getdate()) |  |

### UserAccounts {dbo-useraccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 3,368,190 |
| **Created** | 2006-08-30 17:16:20.997000 |
| **Modified** | 2026-03-14 09:59:15.480000 |
| **Primary Key** | UserAccountId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UserAccountId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | AccountId | int | Yes |  | FK → dbo.Accounts.AccountId |
| 4 | BudgetId | int | Yes |  | FK → dbo.Budgets.BudgetId |
| 5 | BudgetAccountId | int | Yes |  | FK → dbo.BudgetAccounts.BudgetAccountId |
| 6 | UserId | int | Yes |  |  |
| 7 | AllocationAmount | money | Yes |  |  |
| 8 | AllocationAvailable | money | Yes |  |  |
| 9 | UseAllocations | tinyint | Yes |  |  |

### UserAdminLog {dbo-useradminlog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,466 |
| **Created** | 2012-09-25 19:11:28.790000 |
| **Modified** | 2024-06-21 22:39:24.347000 |
| **Primary Key** | logID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | logID | int IDENTITY | No |  | PK |
| 2 | submituserid | int | No |  |  |
| 3 | targetuserid | int | Yes |  |  |
| 4 | action | varchar(50) | No |  |  |
| 5 | commitString | nvarchar(MAX) | Yes |  |  |
| 6 | actionDate | datetime | No |  |  |

### UserCategory {dbo-usercategory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2006-08-29 23:04:32.853000 |
| **Modified** | 2024-06-21 22:39:24.977000 |
| **Primary Key** | UserCategoryId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UserCategoryId | int IDENTITY | No |  | PK |
| 2 | UserId | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |

### UserImports {dbo-userimports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 328 |
| **Created** | 2022-02-07 15:51:38 |
| **Modified** | 2022-02-07 15:51:38.530000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | School | nvarchar(255) | Yes |  |  |
| 2 | User # | nvarchar(255) | Yes |  |  |
| 3 | Attention | nvarchar(255) | Yes |  |  |
| 4 | Approval Level (Teacher/Principal/BA) | nvarchar(255) | Yes |  |  |
| 5 | Approver User # | nvarchar(255) | Yes |  |  |
| 6 | Account Code | nvarchar(255) | Yes |  |  |
| 7 | Amount | float | Yes |  |  |
| 8 | SysId | int IDENTITY | No |  |  |

### Users {dbo-users}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 343,075 |
| **Created** | 2019-12-22 07:50:43.910000 |
| **Modified** | 2026-03-14 10:01:00.120000 |
| **Primary Key** | UserId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UserId | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | SchoolId | int | Yes |  |  |
| 4 | ShippingId | int | Yes |  |  |
| 5 | Active | tinyint | Yes |  |  |
| 6 | UserName | varchar(50) | Yes |  |  |
| 7 | Password | varchar(100) | Yes |  |  |
| 8 | Attention | varchar(50) | Yes |  |  |
| 9 | ApprovalLevel | tinyint | Yes |  |  |
| 10 | CometId | int | Yes |  |  |
| 11 | DisableNewRequisition | tinyint | Yes |  |  |
| 12 | DistrictAcctgCode | varchar(20) | Yes |  |  |
| 13 | ApproverId | int | Yes |  |  |
| 14 | NewRequisitionButton | int | Yes |  |  |
| 15 | AllowIncidentals | tinyint | Yes |  |  |
| 16 | AllowVendorChanges | tinyint | Yes |  |  |
| 17 | AllowShipToChanges | tinyint | Yes |  |  |
| 18 | AllowTM | tinyint | Yes |  |  |
| 19 | Email | varchar(255) | Yes |  |  |
| 20 | SecurityRoleId | int | Yes |  |  |
| 21 | Use20 | tinyint | Yes |  |  |
| 22 | FirstName | varchar(20) | Yes |  |  |
| 23 | LastName | varchar(30) | Yes |  |  |
| 24 | allowMSRP | tinyint | Yes |  |  |
| 25 | EmailByPassDate | date | Yes |  |  |
| 26 | AllowExport | bit | Yes |  |  |
| 27 | HasAdminAccess | bit | Yes |  |  |
| 28 | AllowAddenda | bit | Yes |  |  |
| 29 | UseCF | int | Yes |  |  |
| 30 | IBTypeId | int | Yes |  |  |
| 31 | AllowAccountCodeMgmt | tinyint | Yes |  |  |
| 32 | AllowEarlyAccess | tinyint | Yes |  |  |
| 33 | POAccess | int | Yes |  |  |
| 34 | NotificationType | int | Yes |  |  |
| 38 | PasswordOld | varchar(100) | Yes |  |  |
| 39 | SSOID | varchar(255) | Yes |  |  |
| 40 | SSOProvider | varchar(50) | Yes |  |  |
| 41 | ResetPasswordCode | varchar(8) | Yes |  |  |
| 42 | ResetPasswordCodeExpiration | datetime | Yes |  |  |
| 43 | AllowVendorCodeMaintenance | tinyint | Yes |  |  |
| 45 | PositionData | nvarchar(4000) | Yes |  |  |
| 46 | LastLogin | datetime | Yes |  |  |

### UserTrees {dbo-usertrees}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 56,920 |
| **Created** | 2006-08-29 12:25:05.170000 |
| **Modified** | 2024-06-21 22:40:40.043000 |
| **Primary Key** | utid |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | utid | int IDENTITY | No |  | PK |
| 2 | DistrictId | int | Yes |  |  |
| 3 | UserId | int | Yes |  |  |
| 4 | ApproverId | int | Yes |  |  |
| 5 | ApprovalLevel | int | Yes |  |  |
| 6 | Level | int | Yes |  |  |
| 7 | Status | int | Yes |  |  |
| 8 | SortKey | varchar(512) | Yes |  |  |

### VendorCatalogNote {dbo-vendorcatalognote}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11 |
| **Created** | 2015-05-08 16:38:59.143000 |
| **Modified** | 2024-06-21 22:40:40.253000 |
| **Primary Key** | VendorCatalogNoteId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorCatalogNoteId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | Yes |  |  |
| 3 | CatalogId | int | Yes |  |  |
| 4 | NoteTitle | varchar(80) | Yes |  |  |
| 5 | Note | varchar(4000) | Yes |  |  |
| 6 | NoteDateTime | datetime | Yes |  |  |

### VendorCategory {dbo-vendorcategory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6,883 |
| **Created** | 2006-08-29 23:05:42.040000 |
| **Modified** | 2024-06-21 22:40:40.703000 |
| **Primary Key** | VCId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VCId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | Yes |  |  |
| 3 | CategoryId | int | Yes |  |  |
| 16 | VendorName | varchar(50) | Yes |  |  |
| 18 | WebLink | varchar(512) | Yes |  |  |

### VendorCategoryPP {dbo-vendorcategorypp}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 17,844 |
| **Created** | 2006-08-29 23:05:52.447000 |
| **Modified** | 2024-06-21 22:40:40.997000 |
| **Primary Key** | VCPId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VCPId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | No |  |  |
| 3 | CategoryId | int | No |  |  |
| 4 | DistrictId | int | Yes |  |  |
| 5 | PricePlanId | int | Yes |  |  |

### VendorCertificates {dbo-vendorcertificates}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-01-19 11:47:07.067000 |
| **Modified** | 2024-06-21 22:40:41.113000 |
| **Primary Key** | VendorCertificateId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorCertificateId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | VendorId | int | No |  |  |
| 4 | CertificateAuthorityId | int | No |  |  |
| 5 | Certificate | varchar(50) | Yes |  |  |
| 6 | DateOfIssuance | datetime | Yes |  |  |
| 7 | ExpirationDate | datetime | Yes |  |  |

### VendorContacts {dbo-vendorcontacts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 23,441 |
| **Created** | 2011-08-24 15:02:23.017000 |
| **Modified** | 2024-06-21 22:40:42.193000 |
| **Primary Key** | VendorContactId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorContactId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | No |  |  |
| 3 | Active | tinyint | Yes |  |  |
| 4 | SalutationId | int | Yes |  |  |
| 5 | FirstName | varchar(50) | Yes |  |  |
| 6 | LastName | varchar(50) | Yes |  |  |
| 7 | Suffix | varchar(20) | Yes |  |  |
| 8 | Address1 | varchar(50) | Yes |  |  |
| 9 | Address2 | varchar(50) | Yes |  |  |
| 10 | City | varchar(50) | Yes |  |  |
| 11 | State | char(2) | Yes |  |  |
| 12 | Zipcode | varchar(10) | Yes |  |  |
| 13 | Phone | varchar(25) | Yes |  |  |
| 14 | Fax | varchar(20) | Yes |  |  |
| 15 | EMail | varchar(255) | Yes |  |  |
| 16 | Comments | varchar(1024) | Yes |  |  |
| 17 | Password | varchar(50) | Yes |  |  |
| 18 | LastModified | datetime | Yes |  |  |
| 19 | BidContact | tinyint | Yes |  |  |
| 20 | POContact | tinyint | Yes |  |  |
| 22 | FullName | varchar(150) | Yes |  |  |
| 35 | FreightContact | tinyint | Yes |  |  |
| 36 | CSContact | tinyint | Yes |  |  |
| 37 | ARContact | tinyint | Yes |  |  |

### VendorDeliveryRule {dbo-vendordeliveryrule}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1 |
| **Created** | 2024-02-06 15:19:21.020000 |
| **Modified** | 2024-02-06 15:19:21.480000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorDeliveryRuleId | int IDENTITY | No |  |  |
| 2 | Name | varchar(50) | Yes | ('') |  |
| 3 | Description | varchar(500) | Yes | ('') |  |
| 4 | DeliveryDays | varchar(100) | Yes | ('') |  |
| 5 | DeliveryTime | int | Yes |  |  |
| 6 | AllowGapDay | bit | Yes | ((0)) |  |

### VendorDocRequest {dbo-vendordocrequest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14 |
| **Created** | 2020-12-08 20:46:35.963000 |
| **Modified** | 2024-06-21 22:40:42.833000 |
| **Primary Key** | VendorDocRequestId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorDocRequestId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorDocRequestNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorDocRequestDetail {dbo-vendordocrequestdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 52 |
| **Created** | 2020-12-08 20:46:35.970000 |
| **Modified** | 2024-06-21 22:40:43.327000 |
| **Primary Key** | VendorDocRequestDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorDocRequestDetailId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidImportId | int | Yes |  |  |
| 4 | BidHeaderCheckListId | int | Yes |  |  |
| 5 | VendorDocRequestId | int | Yes |  |  |
| 6 | AddDate | datetime | Yes |  |  |
| 7 | SendDate | datetime | Yes |  |  |
| 8 | CommentsRejectReason | varchar(1024) | Yes |  |  |
| 9 | VendorId | int | Yes |  |  |
| 10 | DistrictName | varchar(50) | Yes |  |  |
| 11 | ResolvedFlag | tinyint | Yes |  |  |

### VendorDocRequestStatus {dbo-vendordocrequeststatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 14 |
| **Created** | 2020-12-08 20:46:35.973000 |
| **Modified** | 2024-06-21 22:40:43.460000 |
| **Primary Key** | VendorDocRequestStatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorDocRequestStatusId | int IDENTITY | No |  | PK |
| 2 | VendorDocRequestId | int | Yes |  |  |
| 3 | StatusId | int | Yes |  |  |
| 4 | StatusDate | datetime | Yes |  |  |
| 5 | FollowUpDate | datetime | Yes |  |  |

### VendorLocations {dbo-vendorlocations}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2007-01-23 12:30:43.100000 |
| **Modified** | 2024-06-21 22:40:43.650000 |
| **Primary Key** | VendorLocationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorLocationId | int IDENTITY | No |  | PK |
| 2 | ShippingId | int | No |  |  |
| 3 | VendorId | int | No |  |  |
| 4 | LocationCode | varchar(50) | Yes |  |  |

### VendorLogoDisplays {dbo-vendorlogodisplays}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2012-06-14 00:09:27.170000 |
| **Modified** | 2024-06-21 22:40:43.767000 |
| **Primary Key** | VendorLogoDisplayID |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorLogoDisplayID | int IDENTITY | No |  | PK |
| 2 | Sequence | int | No |  |  |
| 3 | VendorID | int | No |  |  |

### VendorOrders {dbo-vendororders}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5,741 |
| **Created** | 2025-06-05 13:13:30.080000 |
| **Modified** | 2025-06-12 12:21:45.440000 |
| **Primary Key** | VendorOrderId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorOrderId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | No |  |  |
| 3 | POId | int | No |  |  |
| 4 | LastUpdated | datetime | Yes |  |  |
| 5 | VendorData | nvarchar(MAX) | Yes |  |  |
| 6 | VendorStatus | varchar(MAX) | Yes |  |  |

### VendorOverrideMessages {dbo-vendoroverridemessages}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 5 |
| **Created** | 2007-03-07 09:50:24.320000 |
| **Modified** | 2024-06-21 22:40:44.157000 |
| **Primary Key** | VOMId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VOMId | int IDENTITY | No |  | PK |
| 2 | Message | varchar(50) | No |  |  |
| 3 | RequiredLevel | int | Yes |  |  |

### VendorPOtags {dbo-vendorpotags}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2009-04-06 22:37:58.580000 |
| **Modified** | 2024-06-21 22:40:44.227000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | SysId | uniqueidentifier | No | (newsequentialid()) |  |
| 2 | SessionId | int | No |  |  |
| 3 | ScreenId | varchar(50) | No |  |  |
| 4 | TagId | int | No |  |  |
| 5 | Tagged | tinyint | Yes |  |  |

### VendorQuery {dbo-vendorquery}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 11,828 |
| **Created** | 2020-11-17 18:19:37.677000 |
| **Modified** | 2024-06-21 22:40:45.597000 |
| **Primary Key** | VendorQueryId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorQueryNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorQueryDetail {dbo-vendorquerydetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 132,721 |
| **Created** | 2011-10-27 13:13:28.967000 |
| **Modified** | 2024-06-21 22:40:48.167000 |
| **Primary Key** | VendorQueryDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryDetailId | int IDENTITY | No |  | PK |
| 2 | BidResultsId | int | Yes |  |  |
| 3 | BidHeaderId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | VendorQueryId | int | Yes |  |  |
| 6 | AddDate | datetime | Yes |  |  |
| 7 | SendDate | datetime | Yes |  |  |
| 8 | ItemQuery | varchar(4000) | Yes |  |  |
| 9 | ItemQueryNotes | varchar(1000) | Yes |  |  |
| 10 | VendorId | int | Yes |  |  |
| 11 | DistrictName | varchar(50) | Yes |  |  |
| 12 | ResolvedFlag | tinyint | Yes |  |  |
| 19 | CommonVendorQueryId | int | Yes |  |  |

### VendorQueryMSRP {dbo-vendorquerymsrp}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 140 |
| **Created** | 2020-11-17 18:18:01.723000 |
| **Modified** | 2024-06-21 22:40:48.967000 |
| **Primary Key** | VendorQueryMSRPId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryMSRPId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorQueryMSRPNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorQueryMSRPDetail {dbo-vendorquerymsrpdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2015-12-21 00:52:56.627000 |
| **Modified** | 2024-06-21 22:41:22.427000 |
| **Primary Key** | VendorQueryMSRPDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryMSRPDetailId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidImportId | int | Yes |  |  |
| 4 | VendorQueryMSRPId | int | Yes |  | FK → dbo.VendorQueryMSRP.VendorQueryMSRPId |
| 5 | AddDate | datetime | Yes |  |  |
| 6 | SendDate | datetime | Yes |  |  |
| 7 | MSRPQueryType | int | Yes |  |  |
| 8 | MSRPQuery | varchar(4000) | Yes |  |  |
| 9 | MSRPQueryManufacturers | varchar(MAX) | Yes |  |  |
| 10 | MSRPQueryNotes | varchar(1000) | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | ResolvedFlag | tinyint | Yes |  |  |
| 13 | AllowReply | tinyint | Yes |  |  |
| 14 | ManufacturerSelection | int | Yes |  |  |

### VendorQueryMSRPStatus {dbo-vendorquerymsrpstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 2 |
| **Created** | 2015-12-21 00:53:30.987000 |
| **Modified** | 2024-06-21 22:41:22.547000 |
| **Primary Key** | VendorQueryMSRPStatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryMSRPStatusId | int IDENTITY | No |  | PK |
| 2 | VendorQueryMSRPId | int | Yes |  | FK → dbo.VendorQueryMSRP.VendorQueryMSRPId |
| 3 | StatusId | int | Yes |  |  |
| 4 | StatusDate | datetime | Yes |  |  |
| 5 | FollowUpDate | datetime | Yes |  |  |

### VendorQueryStatus {dbo-vendorquerystatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 30,618 |
| **Created** | 2011-07-29 16:17:31.887000 |
| **Modified** | 2024-06-21 22:40:51.010000 |
| **Primary Key** | VendorQueryStatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryStatusId | int IDENTITY | No |  | PK |
| 2 | VendorQueryId | int | Yes |  |  |
| 3 | StatusId | int | Yes |  |  |
| 4 | StatusDate | datetime | Yes |  |  |
| 5 | FollowUpDate | datetime | Yes |  |  |

### VendorQueryTandM {dbo-vendorquerytandm}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,930 |
| **Created** | 2020-11-17 18:18:54.207000 |
| **Modified** | 2024-06-21 22:40:51.180000 |
| **Primary Key** | VendorQueryTandMId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryTandMId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | VendorId | int | Yes |  |  |
| 4 | BidImportId | int | Yes |  |  |
| 5 | EmailAddress | varchar(4000) | Yes |  |  |
| 6 | Fax | varchar(20) | Yes |  |  |
| 7 | AddDate | datetime | Yes |  |  |
| 8 | SendDate | datetime | Yes |  |  |
| 9 | EmailAddress2 | varchar(255) | Yes |  |  |
| 10 | EmailCCAddress | varchar(255) | Yes |  |  |
| 11 | MessageContent | varchar(MAX) | Yes |  |  |
| 12 | MessageReceiptConfirmed | datetime | Yes |  |  |
| 13 | VendorQueryTandMNotes | varchar(1000) | Yes |  |  |
| 14 | ContactName | varchar(4000) | Yes |  |  |

### VendorQueryTandMDetail {dbo-vendorquerytandmdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,197 |
| **Created** | 2015-12-21 00:54:01.380000 |
| **Modified** | 2024-06-21 22:41:22.737000 |
| **Primary Key** | VendorQueryTandMDetailId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryTandMDetailId | int IDENTITY | No |  | PK |
| 2 | BidHeaderId | int | Yes |  |  |
| 3 | BidImportId | int | Yes |  |  |
| 4 | VendorQueryTandMId | int | Yes |  | FK → dbo.VendorQueryTandM.VendorQueryTandMId |
| 5 | AddDate | datetime | Yes |  |  |
| 6 | SendDate | datetime | Yes |  |  |
| 7 | TandMQueryType | int | Yes |  |  |
| 8 | TandMQuery | varchar(4000) | Yes |  |  |
| 9 | TandMQueryCounties | varchar(1000) | Yes |  |  |
| 10 | TandMQueryNotes | varchar(1000) | Yes |  |  |
| 11 | VendorId | int | Yes |  |  |
| 12 | ResolvedFlag | tinyint | Yes |  |  |

### VendorQueryTandMStatus {dbo-vendorquerytandmstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,870 |
| **Created** | 2015-12-21 00:54:28.077000 |
| **Modified** | 2024-06-21 22:41:23.030000 |
| **Primary Key** | VendorQueryTandMStatusId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorQueryTandMStatusId | int IDENTITY | No |  | PK |
| 2 | VendorQueryTandMId | int | Yes |  | FK → dbo.VendorQueryTandM.VendorQueryTandMId |
| 3 | StatusId | int | Yes |  |  |
| 4 | StatusDate | datetime | Yes |  |  |
| 5 | FollowUpDate | datetime | Yes |  |  |

### Vendors {dbo-vendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 19,012 |
| **Created** | 2026-01-22 20:16:07.093000 |
| **Modified** | 2026-01-23 13:21:47.817000 |
| **Primary Key** | VendorId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | Code | varchar(16) | Yes |  |  |
| 4 | Name | varchar(50) | Yes |  |  |
| 5 | Address1 | varchar(50) | Yes |  |  |
| 6 | Address2 | varchar(50) | Yes |  |  |
| 7 | Address3 | varchar(50) | Yes |  |  |
| 8 | City | varchar(25) | Yes |  |  |
| 9 | State | varchar(2) | Yes |  |  |
| 10 | ZipCode | varchar(10) | Yes |  |  |
| 11 | Phone | varchar(20) | Yes |  |  |
| 12 | Fax | varchar(20) | Yes |  |  |
| 13 | EMail | varchar(255) | Yes |  |  |
| 14 | UseGrossPrices | tinyint | Yes |  |  |
| 15 | ShippingPercentage | decimal(9,5) | Yes |  |  |
| 16 | DistrictId | int | Yes |  |  |
| 17 | Password | varchar(50) | Yes |  |  |
| 18 | HostURL | varchar(255) | Yes |  |  |
| 19 | HostPort | int | Yes |  |  |
| 20 | HostDirectory | varchar(255) | Yes |  |  |
| 21 | HostUserName | varchar(255) | Yes |  |  |
| 22 | HostPassword | varchar(255) | Yes |  |  |
| 23 | UploadEMailList | varchar(4096) | Yes |  |  |
| 24 | UploadType | int | Yes |  |  |
| 25 | BusinessUnit | varchar(17) | Yes |  |  |
| 26 | POPassword | varchar(50) | Yes |  |  |
| 27 | cXMLAddress | varchar(1024) | Yes |  |  |
| 28 | VendorLogo | varbinary(MAX) | Yes |  |  |
| 29 | cXMLFromDomain | varchar(50) | Yes |  |  |
| 30 | cXMLFromIdentity | varchar(50) | Yes |  |  |
| 31 | cXMLToDomain | varchar(50) | Yes |  |  |
| 32 | cXMLToIdentity | varchar(50) | Yes |  |  |
| 33 | cXMLSenderDomain | varchar(50) | Yes |  |  |
| 34 | cXMLSenderIdentity | varchar(50) | Yes |  |  |
| 35 | cXMLSenderSharedSecret | varchar(50) | Yes |  |  |
| 36 | AllowElectronicPOs | int | Yes |  |  |
| 37 | VendorDeliveryRuleId | int | Yes | ((1)) |  |
| 38 | DisplayAs | varchar(50) | Yes |  |  |
| 39 | incXMLFromDomain | varchar(20) | Yes |  |  |
| 40 | incXMLFromIdentity | varchar(50) | Yes |  |  |
| 41 | incXMLSharedSecret | varchar(255) | Yes |  |  |
| 42 | incXMLEnabled | tinyint | Yes |  |  |
| 43 | VendorComplianceFlag | tinyint | No | ((0)) |  |

### VendorSessions {dbo-vendorsessions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 10,870 |
| **Created** | 2009-02-27 11:50:34.517000 |
| **Modified** | 2024-06-21 22:40:53.983000 |
| **Primary Key** | VendorSessionId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VendorSessionId | int IDENTITY | No |  | PK |
| 2 | VendorId | int | No |  |  |
| 3 | UserName | varchar(50) | Yes |  |  |
| 4 | jSession | varchar(255) | Yes |  |  |
| 5 | StartTime | datetime | Yes |  |  |
| 6 | EndTime | datetime | Yes |  |  |
| 7 | IPAddress | varchar(50) | Yes |  |  |
| 8 | VPORegistrationId | int | Yes |  |  |

### VendorUploads {dbo-vendoruploads}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 1,534,545 |
| **Created** | 2006-08-29 23:06:33.370000 |
| **Modified** | 2024-06-21 22:41:14.743000 |
| **Primary Key** | UploadId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | UploadId | int IDENTITY | No |  | PK |
| 2 | FileName | varchar(255) | Yes |  |  |
| 3 | DateCreated | datetime | Yes |  |  |
| 4 | DateUploaded | datetime | Yes |  |  |
| 5 | Status | varchar(255) | Yes |  |  |
| 7 | cxmlsessionid | int | Yes |  |  |
| 8 | poid | int | Yes |  |  |
| 9 | PayloadID | varchar(255) | Yes |  |  |

### VPOLoginAttempts {dbo-vpologinattempts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-03-23 12:55:54.663000 |
| **Modified** | 2024-06-21 22:41:15.377000 |
| **Primary Key** | VPOLoginAttemptId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VPOLoginAttemptId | int IDENTITY | No |  | PK |
| 2 | VPOUserCode | varchar(50) | No |  |  |
| 3 | VPORegistrationId | int | Yes |  |  |
| 4 | VPOEventDate | datetime | No | (getdate()) |  |
| 5 | IPAddress | varchar(50) | Yes |  |  |
| 6 | LoginStatus | int | No | ((2)) |  |

### VPORegistrations {dbo-vporegistrations}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 6 |
| **Created** | 2010-03-23 12:55:54.540000 |
| **Modified** | 2024-06-21 22:41:15.683000 |
| **Primary Key** | VPORegistrationId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VPORegistrationId | int IDENTITY | No |  | PK |
| 2 | Active | tinyint | Yes |  |  |
| 3 | VPOUserCode | varchar(50) | No |  |  |
| 4 | VPOPassword | varchar(50) | No |  |  |
| 5 | VPOLastChange | datetime | No | (getdate()) |  |
| 6 | VPOEMail | varchar(255) | Yes |  |  |
| 7 | VPOName | varchar(50) | Yes |  |  |
| 8 | VPOPhone | varchar(50) | Yes |  |  |
| 9 | VPOAllowedRetries | int | No | ((5)) |  |
| 10 | VPOParentId | int | Yes |  |  |
| 11 | VPOCanCreateUser | tinyint | Yes |  |  |

### VPOVendorLinks {dbo-vpovendorlinks}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 10 |
| **Created** | 2010-03-23 12:55:54.640000 |
| **Modified** | 2024-06-21 22:41:16.060000 |
| **Primary Key** | VPOVendorLinkId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | VPOVendorLinkId | int IDENTITY | No |  | PK |
| 2 | VPORegistrationId | int | No |  |  |
| 3 | VendorId | int | No |  |  |
| 4 | LastChange | datetime | No | (getdate()) |  |

### WizHelpFile {dbo-wizhelpfile}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2001-08-24 14:40:32.417000 |
| **Modified** | 2021-11-08 07:01:38.257000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | int | Yes |  |  |
| 2 | Proc | varchar(64) | Yes |  |  |
| 3 | Field | varchar(64) | Yes |  |  |
| 4 | HelpText | char(1024) | Yes |  |  |

### YearlyTotals {dbo-yearlytotals}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 10,432 |
| **Created** | 2015-11-01 03:00:01.453000 |
| **Modified** | 2024-06-21 21:57:17.913000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | BudgetId | int | No |  |  |
| 2 | Name | varchar(30) | Yes |  |  |
| 3 | DistrictId | int | Yes |  |  |
| 4 | DistrictName | varchar(189) | Yes |  |  |
| 5 | TotalBidCost | money | Yes |  |  |
| 6 | TotalCatalogCost | numeric(38,6) | Yes |  |  |
| 7 | TotalStateContractCost | numeric(38,6) | Yes |  |  |
| 8 | StateContractDiscount | decimal(13,9) | Yes |  |  |
| 9 | OverallSavings | numeric(38,6) | Yes |  |  |
| 10 | OverallDiscount | numeric(38,6) | Yes |  |  |
| 11 | IncludedCatalogCost | numeric(38,6) | Yes |  |  |
| 12 | IncludedBidCost | money | Yes |  |  |
| 13 | ExcludedCatalogCost | numeric(38,6) | Yes |  |  |
| 14 | ExcludedBidCost | money | Yes |  |  |
| 15 | IncludedSavings | numeric(38,6) | Yes |  |  |
| 16 | ExcludedSavings | numeric(38,6) | Yes |  |  |
| 17 | IncludedDiscount | numeric(38,6) | Yes |  |  |
| 18 | ExcludedDiscount | numeric(38,6) | Yes |  |  |

### z4zbBidFix {dbo-z4zbbidfix}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-04-14 22:35:33.773000 |
| **Modified** | 2018-03-19 17:18:50.693000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | PackedCode | varchar(50) | Yes |  |  |
| 2 | ItemId | int | Yes |  |  |
| 3 | DoNotDiscount | int | Yes |  |  |
| 4 | GrossPrice | money | Yes |  |  |
| 5 | z4ItemId | int | Yes |  |  |
| 6 | z4Price | decimal(33,13) | Yes |  |  |
| 7 | z4BidQuantity | int | Yes |  |  |
| 8 | z4GrossPrice | money | Yes |  |  |
| 9 | zbItemId | int | Yes |  |  |
| 10 | zbPrice | decimal(33,13) | Yes |  |  |
| 11 | zbBidQuantity | int | Yes |  |  |
| 12 | zbGrossPrice | money | Yes |  |  |

### z4zbReqDetail {dbo-z4zbreqdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Rows** | 0 |
| **Created** | 2010-04-14 21:44:10.663000 |
| **Modified** | 2018-03-19 17:18:50.720000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | RequisitionId | int | No |  |  |
| 2 | DetailId | int | No |  |  |
| 3 | BidPrice | money | Yes |  |  |
| 4 | ItemId | int | Yes |  |  |
| 5 | BidItemId | int | Yes |  |  |
| 6 | z4ItemId | int | Yes |  |  |
| 7 | zbItemId | int | Yes |  |  |
| 8 | Filtered | int | Yes |  |  |

### migratorversions {edsiqwebuser-migratorversions}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Rows** | 0 |
| **Created** | 2023-07-26 14:16:11.640000 |
| **Modified** | 2023-07-26 14:16:11.640000 |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | version | varchar(25) | Yes |  |  |

### TableOfContents {edsiqwebuser-tableofcontents}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Rows** | 6,664 |
| **Created** | 2002-09-05 16:02:10.140000 |
| **Modified** | 2021-11-08 21:29:55.807000 |
| **Primary Key** | TCId |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | TCId | int IDENTITY | No |  | PK |
| 2 | Title | varchar(255) | Yes |  |  |
| 4 | PageNbr | int | Yes |  |  |
| 5 | OrderBookId | int | Yes |  |  |

### UnsubscriptionEmail {edsiqwebuser-unsubscriptionemail}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Rows** | 0 |
| **Created** | 2024-07-26 04:36:14.983000 |
| **Modified** | 2024-07-26 04:36:15.260000 |
| **Primary Key** | Id |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | Id | int IDENTITY | No |  | PK |
| 2 | Email | varchar(100) | No |  |  |
| 3 | CreatedAt | datetime | Yes | (getdate()) |  |

### REPMAN_GROUPS {edswebrpts-repman-groups}

| Property | Value |
|----------|-------|
| **Schema** | EDSWebRpts |
| **Rows** | 1 |
| **Created** | 2005-02-09 17:28:16.617000 |
| **Modified** | 2021-11-08 21:29:55.570000 |
| **Primary Key** | GROUP_CODE |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | GROUP_CODE | int | No |  | PK |
| 2 | GROUP_NAME | varchar(100) | Yes |  |  |
| 3 | PARENT_GROUP | int | No |  |  |

### REPMAN_REPORTS {edswebrpts-repman-reports}

| Property | Value |
|----------|-------|
| **Schema** | EDSWebRpts |
| **Rows** | 1 |
| **Created** | 2005-02-09 17:28:50.117000 |
| **Modified** | 2021-11-08 21:29:55.593000 |
| **Primary Key** | REPORT_NAME |

#### Columns

| # | Column | Type | Nullable | Default | Key |
|---|--------|------|----------|---------|-----|
| 1 | REPORT_NAME | varchar(100) | No |  | PK |
| 2 | REPORT | BLOB | No |  |  |
| 3 | REPORT_GROUP | int | Yes |  |  |
| 4 | USER_FLAG | int | Yes |  |  |

---

## Views

### Schema: EDSIQEndUser

#### Sessions {view-edsiqenduser-sessions}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQEndUser |
| **Created** | 2011-03-01 16:45:50.610000 |
| **Modified** | 2018-01-21 20:26:48.603000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | UserId | int | No |
| 3 | DistrictId | int | Yes |
| 4 | SchoolId | int | Yes |
| 5 | Attention | varchar(50) | Yes |
| 6 | AllowIncidentals | tinyint | Yes |
| 7 | CurrentBudgetId | int | Yes |
| 8 | NextBudgetId | int | Yes |
| 9 | jSession | varchar(255) | No |
| 10 | IPAddress | varchar(50) | Yes |

### Schema: EDSIQWebUser

#### CategoryPP {view-edsiqwebuser-categorypp}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2003-01-09 18:03:22.873000 |
| **Modified** | 2018-01-21 20:26:46.557000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | Yes |
| 2 | PricePlanId | int | Yes |

#### CoverView {view-edsiqwebuser-coverview}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2005-08-19 08:20:39.653000 |
| **Modified** | 2018-01-21 20:26:48.610000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |
| 30 | UsesBooklet | int | Yes |
| 31 | UsesOnline | int | Yes |

#### CoverViewSrc {view-edsiqwebuser-coverviewsrc}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2002-09-20 13:01:36.153000 |
| **Modified** | 2009-03-25 06:55:28.223000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(2) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |

#### MissingCoverView {view-edsiqwebuser-missingcoverview}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2006-11-14 21:09:46.007000 |
| **Modified** | 2018-01-21 20:26:48.627000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |

#### OrderBookDetailView {view-edsiqwebuser-orderbookdetailview}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2002-10-17 11:02:36.467000 |
| **Modified** | 2018-01-21 20:26:48.633000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | OrderBookDetailId | int | No |
| 2 | OrderBookId | int | No |
| 3 | ItemCode | varchar(50) | Yes |
| 4 | UnitCode | varchar(20) | Yes |
| 5 | GrossPrice | money | Yes |
| 6 | CatalogPage | varchar(4) | Yes |
| 7 | CatalogYear | varchar(2) | Yes |
| 8 | VendorName | varchar(255) | Yes |
| 9 | VendorItemCode | varchar(50) | Yes |
| 10 | TotalQuantity | int | No |
| 11 | TotalRequisitions | int | No |
| 12 | ExpandAll | tinyint | Yes |
| 13 | Weight | int | No |
| 14 | SortSeq | varchar(64) | Yes |
| 15 | Active | tinyint | Yes |
| 16 | Alternate | varchar(1024) | Yes |
| 17 | VendorId | int | Yes |
| 18 | VendorCode | varchar(16) | Yes |
| 19 | ItemDescription | varchar(512) | Yes |
| 20 | HeadingId | int | Yes |
| 21 | HeadingCode | varchar(16) | Yes |
| 22 | HeadingTitle | varchar(255) | Yes |
| 23 | HeadingDescription | varchar(4096) | Yes |

#### OrderBookView {view-edsiqwebuser-orderbookview}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2002-10-16 11:23:57.530000 |
| **Modified** | 2018-01-21 20:26:48.637000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | OrderBookId | int | No |
| 2 | PricePlanDescription | varchar(255) | Yes |
| 3 | Category | varchar(255) | Yes |
| 4 | PricePlanId | int | Yes |
| 5 | CategoryId | int | Yes |
| 6 | AwardId | int | Yes |
| 7 | BookType | varchar(11) | No |
| 8 | Active | int | Yes |
| 9 | BidHeaderId | int | Yes |
| 10 | DistrictId | int | Yes |

#### POAccountList {view-edsiqwebuser-poaccountlist}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2003-04-03 16:06:08.653000 |
| **Modified** | 2018-01-21 20:26:48.640000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | PONumber | varchar(24) | Yes |
| 3 | AccountCode | varchar(50) | Yes |
| 4 | POAmount | money | Yes |

#### POAccountsUsed {view-edsiqwebuser-poaccountsused}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2003-04-03 16:08:28.450000 |
| **Modified** | 2018-01-21 20:26:48.647000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | PONumber | varchar(24) | Yes |
| 3 | AccountCode | varchar(50) | Yes |
| 4 | POAmount | money | Yes |

#### ScheduledByPricePlanCategory {view-edsiqwebuser-scheduledbypriceplancategory}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2003-01-14 12:51:29 |
| **Modified** | 2018-01-21 20:26:46.563000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PricePlanDescription | varchar(278) | No |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | PercentIn | float | Yes |
| 4 | PercentOut | float | Yes |
| 5 | DistrictsIn | int | Yes |
| 6 | TotalDistricts | int | Yes |

#### ScheduledByPricePlanCategoryRep {view-edsiqwebuser-scheduledbypriceplancategoryrep}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2003-01-14 13:30:48.687000 |
| **Modified** | 2018-01-21 20:26:46.633000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PricePlanDescription | varchar(278) | No |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | PercentIn | float | Yes |
| 4 | PercentOut | float | Yes |
| 5 | DistrictsIn | int | Yes |
| 6 | TotalDistricts | int | Yes |
| 7 | RepName | varchar(30) | Yes |

#### ScheduledDistrictsByPricePlanCategory {view-edsiqwebuser-scheduleddistrictsbypriceplancategory}

| Property | Value |
|----------|-------|
| **Schema** | EDSIQWebUser |
| **Created** | 2003-01-14 12:56:35.310000 |
| **Modified** | 2018-01-21 20:26:46.630000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PricePlanDescription | varchar(278) | No |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | DistrictCode | varchar(4) | Yes |
| 4 | DistrictName | varchar(50) | Yes |
| 5 | PercentIn | float | Yes |
| 6 | PercentOut | float | Yes |
| 7 | DistrictsIn | int | Yes |
| 8 | TotalDistricts | int | Yes |
| 9 | RepName | varchar(30) | Yes |

### Schema: VMS

#### vw_BidsByVendor {view-vms-vw-bidsbyvendor}

| Property | Value |
|----------|-------|
| **Schema** | VMS |
| **Created** | 2016-07-08 21:44:25.697000 |
| **Modified** | 2018-01-21 20:26:48.650000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | CategoryId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | Description | varchar(512) | Yes |
| 5 | BidMessage | varchar(1024) | Yes |
| 6 | EffectiveFrom | datetime | Yes |
| 7 | EffectiveUntil | datetime | Yes |
| 8 | ClosingDate | datetime | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | PK | int | No |

#### vw_Login {view-vms-vw-login}

| Property | Value |
|----------|-------|
| **Schema** | VMS |
| **Created** | 2016-07-05 11:14:01.383000 |
| **Modified** | 2018-01-21 20:26:48.653000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorContactId | int | No |
| 2 | VendorId | int | No |
| 3 | FullName | varchar(150) | Yes |
| 4 | LastName | varchar(50) | Yes |
| 5 | FirstName | varchar(50) | Yes |
| 6 | EMail | varchar(255) | Yes |
| 7 | Password | varchar(50) | Yes |

### Schema: dbo

#### BidAnalysisDetail {view-dbo-bidanalysisdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-09-19 15:58:33.990000 |
| **Modified** | 2018-01-21 20:26:47.137000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | PricePlanName | varchar(278) | No |
| 3 | BidHeaderId | int | Yes |
| 4 | BidRequestItemId | int | No |
| 5 | DistrictId | int | Yes |
| 6 | DistrictName | varchar(50) | No |
| 7 | ItemCode | varchar(50) | Yes |
| 8 | Description | varchar(1024) | Yes |
| 9 | UnitCode | varchar(20) | Yes |
| 10 | VendorName | varchar(50) | No |
| 11 | VendorCode | varchar(16) | No |
| 12 | BidUnits | varchar(16) | Yes |
| 13 | BidRequest | int | Yes |
| 14 | BidType | varchar(13) | Yes |
| 15 | QuantityBid | int | Yes |
| 16 | UnitPrice | decimal(34,13) | Yes |
| 17 | ExtendedCost | decimal(38,6) | Yes |
| 18 | Alternate | varchar(MAX) | Yes |
| 19 | VendorItemCode | varchar(50) | Yes |
| 20 | BidRequestStatus | varchar(50) | Yes |
| 21 | Status | varchar(51) | Yes |
| 22 | ResultsStatus | int | No |
| 23 | BidResultsId | int | Yes |
| 24 | Comments | varchar(1024) | Yes |
| 25 | ItemComments | varchar(1024) | Yes |
| 26 | PriceVarianceLevel | decimal(9,5) | Yes |
| 27 | FirstPrice | decimal(34,13) | Yes |
| 28 | FirstPriceBidResultsId | int | Yes |
| 29 | SecondPrice | decimal(34,13) | Yes |
| 30 | SecondPriceBidResultsId | int | Yes |
| 31 | Compliant1st | int | Yes |
| 32 | SortKey | varchar(124) | Yes |
| 33 | Variance | decimal(38,6) | Yes |
| 34 | ItemStatus | varchar(MAX) | Yes |
| 35 | PageNo | int | Yes |
| 36 | BidResultsItemsPerUnit | varchar(50) | Yes |
| 37 | ItemsItemsPerUnit | varchar(50) | Yes |

#### BidAnalysisDetailReq {view-dbo-bidanalysisdetailreq}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-12-21 17:19:47.267000 |
| **Modified** | 2018-01-21 20:26:47.140000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | PricePlanName | varchar(278) | No |
| 3 | BidHeaderId | int | Yes |
| 4 | BidRequestItemId | int | No |
| 5 | DistrictId | int | Yes |
| 6 | DistrictName | varchar(50) | No |
| 7 | ItemCode | varchar(50) | Yes |
| 8 | Description | varchar(1024) | Yes |
| 9 | UnitCode | varchar(20) | Yes |
| 10 | VendorName | varchar(50) | No |
| 11 | VendorCode | varchar(16) | No |
| 12 | BidUnits | varchar(16) | Yes |
| 13 | BidRequest | int | Yes |
| 14 | BidType | varchar(13) | Yes |
| 15 | QuantityBid | int | Yes |
| 16 | UnitPrice | decimal(34,13) | Yes |
| 17 | ExtendedCost | decimal(38,6) | Yes |
| 18 | Alternate | varchar(MAX) | Yes |
| 19 | VendorItemCode | varchar(50) | Yes |
| 20 | BidRequestStatus | varchar(50) | Yes |
| 21 | Status | varchar(51) | Yes |
| 22 | BidResultsId | int | Yes |
| 23 | Comments | varchar(1024) | Yes |
| 24 | ItemComments | varchar(1024) | Yes |
| 25 | PriceVarianceLevel | decimal(9,5) | Yes |
| 26 | FirstPrice | decimal(34,13) | Yes |
| 27 | FirstPriceBidResultsId | int | Yes |
| 28 | SecondPrice | decimal(34,13) | Yes |
| 29 | SecondPriceBidResultsId | int | Yes |
| 30 | Compliant1st | int | Yes |
| 31 | OtherReqs | int | No |
| 32 | SortKey | varchar(124) | Yes |
| 33 | Variance | decimal(38,6) | Yes |
| 34 | ItemStatus | varchar(MAX) | Yes |

#### BidHeadersView {view-dbo-bidheadersview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-06-06 01:42:34.983000 |
| **Modified** | 2018-01-21 20:26:47.147000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | Active | tinyint | Yes |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | PricePlanCode | varchar(20) | Yes |
| 5 | PricePlanName | varchar(255) | Yes |
| 6 | DistrictCode | varchar(4) | Yes |
| 7 | DistrictName | varchar(50) | Yes |
| 8 | BidDate | datetime | Yes |
| 9 | BidAwardDate | datetime | Yes |
| 10 | BidMessage | varchar(1024) | Yes |
| 11 | BidReportName | varchar(27) | No |

#### BidItemView {view-dbo-biditemview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-10-11 11:45:13.633000 |
| **Modified** | 2018-01-21 20:26:47.157000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Title | varchar(255) | Yes |
| 2 | Keyword | varchar(50) | Yes |
| 3 | ItemCode | varchar(50) | Yes |
| 4 | Description | varchar(1024) | Yes |
| 5 | UnitCode | varchar(20) | Yes |
| 6 | Alternate | varchar(512) | Yes |
| 7 | VendorItemCode | varchar(50) | Yes |
| 8 | SortSeq | varchar(64) | Yes |
| 9 | HeadingId | int | Yes |
| 10 | KeywordId | int | Yes |
| 11 | ItemId | int | No |
| 12 | BidHeaderId | int | Yes |
| 13 | BidPrice | decimal(29,9) | Yes |

#### BidItemsView {view-dbo-biditemsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-06-06 01:42:36.327000 |
| **Modified** | 2018-01-21 20:26:47.150000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidItemId | int | No |
| 2 | BidId | int | Yes |
| 3 | ItemCode | varchar(50) | Yes |
| 4 | ItemDescription | varchar(512) | Yes |
| 5 | Price | money | Yes |
| 6 | Alternate | varchar(512) | Yes |
| 7 | BidQuantity | int | Yes |
| 8 | AwardId | int | Yes |
| 9 | VendorItemCode | varchar(50) | Yes |
| 10 | SortSeq | varchar(64) | Yes |

#### BidMgrBidRankingMSRPView {view-dbo-bidmgrbidrankingmsrpview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-10-04 18:20:52.340000 |
| **Modified** | 2018-01-21 20:26:45.840000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ActiveBid | int | No |
| 2 | VendorName | varchar(50) | Yes |
| 3 | DiscountRate | decimal(9,5) | Yes |
| 4 | DiscountRateString | char(10) | Yes |
| 5 | ManufacturerId | int | No |
| 6 | ManufacturerName | varchar(100) | No |
| 7 | WriteInFlag | tinyint | Yes |
| 8 | WriteInManufacturer | varchar(100) | No |
| 9 | BidHeaderId | int | No |
| 10 | BidImportId | int | No |
| 11 | BidMSRPResultsId | int | No |
| 12 | WinningBidFlag | int | No |
| 13 | TieBid | int | No |
| 14 | VendorNotes | varchar(1000) | Yes |
| 15 | VendorId | int | No |
| 16 | VendorCode | varchar(16) | Yes |
| 17 | WinningBidOverride | tinyint | No |

#### BidMgrBidRequestAndWriteInMSRPView {view-dbo-bidmgrbidrequestandwriteinmsrpview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-10-04 17:20:27.853000 |
| **Modified** | 2018-01-21 20:26:47.160000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | WriteIn | int | No |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerId | int | Yes |
| 5 | BidRequestManufacturerId | int | No |
| 6 | SequenceNumber | int | Yes |
| 7 | UniqueIdString | varchar(60) | Yes |

#### BidMgrBidRequestDetail {view-dbo-bidmgrbidrequestdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-05-01 15:41:19.483000 |
| **Modified** | 2018-01-21 20:26:46.973000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestItemId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | CategoryId | int | Yes |
| 5 | DistrictId | int | Yes |
| 6 | RequisitionCount | int | Yes |
| 7 | ItemId | int | No |
| 8 | ItemCode | varchar(50) | Yes |
| 9 | ItemDescription | varchar(512) | Yes |
| 10 | UnitCode | varchar(20) | Yes |
| 11 | CrossReferencesText | varchar(1024) | Yes |
| 12 | BidRequest | int | Yes |
| 13 | BrandName | varchar(50) | Yes |
| 14 | ManufacturorNumber | varchar(50) | Yes |
| 15 | VendorName | varchar(50) | Yes |
| 16 | VendorPartNumber | varchar(50) | Yes |
| 17 | Keyword | varchar(50) | Yes |
| 18 | Title | varchar(255) | Yes |
| 19 | ExtraDetail | varchar(1024) | Yes |
| 20 | ItemsPerUnit | varchar(50) | Yes |
| 21 | SortSeq | varchar(64) | Yes |
| 22 | Status | varchar(50) | Yes |
| 23 | Comments | varchar(1024) | Yes |
| 24 | FullDescription | varchar(1156) | Yes |
| 25 | DistrictName | varchar(50) | Yes |
| 26 | CategoryType | int | Yes |
| 27 | Weight | real | Yes |

#### BidMgrBidRequestMSRPView {view-dbo-bidmgrbidrequestmsrpview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-09-24 15:02:21.510000 |
| **Modified** | 2018-01-21 20:26:47.167000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | Active | tinyint | Yes |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerId | int | Yes |
| 5 | BidRequestManufacturerId | int | No |
| 6 | SequenceNumber | int | Yes |

#### BidMgrBidResultsMSRPView {view-dbo-bidmgrbidresultsmsrpview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-09-24 16:17:29.973000 |
| **Modified** | 2018-01-21 20:26:45.830000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ManufacturerName | varchar(100) | No |
| 2 | ActiveBid | int | No |
| 3 | BidHeaderId | int | No |
| 4 | BidImportId | int | No |
| 5 | ManufacturerId | int | Yes |
| 6 | DiscountRate | decimal(9,5) | Yes |
| 7 | DiscountRateString | char(10) | Yes |
| 8 | WriteInFlag | tinyint | Yes |
| 9 | WriteInManufacturer | varchar(100) | Yes |
| 10 | Modified | datetime | No |
| 11 | BidMSRPResultsId | int | No |
| 12 | WinningBidFlag | int | No |
| 13 | BidRequestManufacturerId | int | Yes |
| 14 | WinningBidOverride | tinyint | No |

#### BidMgrBidTradeCountiesView {view-dbo-bidmgrbidtradecountiesview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-12-28 17:09:48.983000 |
| **Modified** | 2018-01-21 20:26:47.170000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CountyName | varchar(50) | No |
| 2 | State | char(2) | No |
| 3 | BidTradeCountyId | int | No |
| 4 | BidTradeId | int | No |
| 5 | CountyId | int | No |
| 6 | StateId | int | Yes |

#### BidMgrBidTradeCountyTotals {view-dbo-bidmgrbidtradecountytotals}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-03 18:14:49.147000 |
| **Modified** | 2018-01-21 20:26:46.137000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | BidTradeId | int | No |
| 4 | CountyId | int | No |
| 5 | Name | varchar(50) | No |
| 6 | State | char(2) | No |
| 7 | CountyTotalUsedInAward | money | Yes |
| 8 | ActiveBidImport | tinyint | Yes |
| 9 | ActiveCounty | tinyint | Yes |
| 10 | BidImportCountyId | int | No |
| 11 | ActiveBidAndCounty | tinyint | Yes |

#### BidMgrBidTradeLowBidder {view-dbo-bidmgrbidtradelowbidder}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-07 19:16:51.023000 |
| **Modified** | 2018-01-21 20:26:46.140000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidTradeId | int | No |
| 3 | CountyId | int | No |
| 4 | BidImportId | int | No |
| 5 | CountyTotalUsedInAward | money | Yes |
| 6 | VendorId | int | Yes |
| 7 | VendorName | varchar(50) | Yes |
| 8 | CountyName | varchar(50) | No |
| 9 | VendorCode | varchar(16) | Yes |
| 10 | State | char(2) | No |
| 11 | Active | tinyint | Yes |
| 12 | Comments | varchar(1024) | Yes |
| 13 | ActiveCounty | tinyint | Yes |
| 14 | BidImportCountyId | int | No |
| 15 | ActiveBidAndCounty | tinyint | Yes |
| 16 | CommentsCounty | varchar(4096) | Yes |

#### BidMgrMSRP2ResultsView {view-dbo-bidmgrmsrp2resultsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-16 14:05:10.050000 |
| **Modified** | 2018-01-21 20:26:46.333000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerProductLineId | int | No |
| 5 | ProductLineName | varchar(100) | No |
| 6 | MSRPOptionId | int | No |
| 7 | OptionName | varchar(50) | No |
| 8 | BidMSRPResultsId | int | Yes |
| 9 | BidMSRPResultsProductLineId | int | Yes |
| 10 | WriteInManufacturer | varchar(100) | Yes |
| 11 | WriteInFlag | tinyint | Yes |
| 12 | WinningBidOverride | tinyint | Yes |
| 13 | DiscountRate | decimal(38,6) | Yes |
| 14 | PriceListTypeId | int | Yes |
| 15 | TotalAward | tinyint | Yes |
| 16 | TotalAwardDiscount | decimal(9,5) | Yes |
| 17 | ProductLineWeight | decimal(9,5) | Yes |
| 18 | TotalAwardManufacturerWeight | decimal(38,6) | Yes |
| 19 | TotalAwardProductLineWeight | decimal(38,6) | Yes |
| 20 | SortKey | varchar(15) | Yes |
| 21 | PriceListType | varchar(50) | Yes |
| 22 | VendorId | int | Yes |
| 23 | VendorName | varchar(50) | Yes |
| 24 | PriceListWarning | varchar(28) | No |
| 25 | WinningBidFlag | int | No |
| 26 | AllFlag | int | No |

#### BidMgrMSRP2VendorReportView {view-dbo-bidmgrmsrp2vendorreportview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-17 16:31:38.380000 |
| **Modified** | 2018-01-21 20:26:46.193000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | ActiveBidImport | tinyint | Yes |
| 4 | VendorsCode | varchar(16) | Yes |
| 5 | VendorsName | varchar(50) | Yes |
| 6 | VendorId | int | Yes |
| 7 | WriteInFlag | tinyint | No |
| 8 | ManufacturerName | varchar(100) | No |
| 9 | ActiveManufBid | int | No |
| 10 | AuthorizationLetter | tinyint | No |
| 11 | SubmittedExcel | tinyint | No |
| 12 | ProductCatalog | tinyint | No |
| 13 | TotalAward | tinyint | No |
| 14 | VendorPriceFile | tinyint | No |
| 15 | TotalAwardString | varchar(20) | Yes |
| 16 | TotalAwardDiscount | decimal(9,5) | Yes |
| 17 | BidMSRPResultsId | int | No |
| 18 | BidRequestManufacturerId | int | Yes |
| 19 | ManufacturerId | int | Yes |
| 20 | PriceListTypeId | int | No |
| 21 | PriceListType | varchar(50) | No |
| 22 | WriteInManufacturer | varchar(100) | Yes |
| 23 | BidMSRPResultsProductLineId | int | No |
| 24 | ActiveProdLine | tinyint | Yes |
| 25 | ProdLineOrWriteIn | varchar(100) | No |
| 26 | WriteInProductLineFlag | tinyint | Yes |
| 27 | BidRequestProductLineId | int | Yes |
| 28 | BidRequestOptionId | int | Yes |
| 29 | MSRPOptionId | int | Yes |
| 30 | OptionName | varchar(50) | Yes |
| 31 | WeightedDiscount | decimal(9,5) | Yes |
| 32 | ProdLineSortKey | varchar(512) | Yes |
| 33 | ManufacturerProductLineId | int | No |
| 34 | AllActive | int | No |
| 35 | WinningBidFlag | int | No |
| 36 | AllProductLine | int | No |
| 37 | FakeRecord | int | No |
| 38 | VendorALLWinner | int | No |

#### BidMgrMSRP2VendorReportViewTemp {view-dbo-bidmgrmsrp2vendorreportviewtemp}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-04-14 16:13:16.263000 |
| **Modified** | 2018-01-21 20:26:46.117000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | ActiveBidImport | tinyint | Yes |
| 4 | VendorsCode | varchar(16) | Yes |
| 5 | VendorsName | varchar(50) | Yes |
| 6 | VendorId | int | Yes |
| 7 | WriteInFlag | tinyint | No |
| 8 | ManufacturerName | varchar(100) | No |
| 9 | ActiveManufBid | int | No |
| 10 | AuthorizationLetter | tinyint | No |
| 11 | SubmittedExcel | tinyint | No |
| 12 | ProductCatalog | tinyint | No |
| 13 | TotalAward | tinyint | No |
| 14 | VendorPriceFile | tinyint | No |
| 15 | TotalAwardString | varchar(20) | Yes |
| 16 | TotalAwardDiscount | decimal(9,5) | Yes |
| 17 | BidMSRPResultsId | int | No |
| 18 | BidRequestManufacturerId | int | Yes |
| 19 | ManufacturerId | int | Yes |
| 20 | PriceListTypeId | int | No |
| 21 | PriceListType | varchar(50) | No |
| 22 | WriteInManufacturer | varchar(100) | Yes |
| 23 | BidMSRPResultsProductLineId | int | No |
| 24 | ActiveProdLine | tinyint | Yes |
| 25 | ProdLineOrWriteIn | varchar(100) | No |
| 26 | WriteInProductLineFlag | tinyint | Yes |
| 27 | BidRequestProductLineId | int | Yes |
| 28 | BidRequestOptionId | int | Yes |
| 29 | MSRPOptionId | int | Yes |
| 30 | OptionName | varchar(50) | Yes |
| 31 | WeightedDiscount | decimal(9,5) | Yes |
| 32 | ProdLineSortKey | varchar(512) | Yes |
| 33 | ManufacturerProductLineId | int | No |
| 34 | AllActive | int | No |
| 35 | WinningBidFlag | int | No |
| 36 | AllProductLine | int | No |
| 37 | TotalAwardManufacturerWeight | decimal(38,6) | Yes |

#### BidMgrMSRPVendorBidsView {view-dbo-bidmgrmsrpvendorbidsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-11-15 17:19:45.503000 |
| **Modified** | 2018-01-21 20:26:46.097000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | VendorsCode | varchar(16) | Yes |
| 5 | VendorsName | varchar(50) | Yes |
| 6 | VendorId | int | Yes |

#### BidMgrView {view-dbo-bidmgrview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-26 17:24:37.840000 |
| **Modified** | 2018-01-21 20:26:47.173000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidResultsId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | BidRequestItemId | int | Yes |
| 4 | BidImportId | int | Yes |
| 5 | VendorName | varchar(50) | Yes |
| 6 | Quantity | int | Yes |
| 7 | QuantityBid | int | Yes |
| 8 | UnitPrice | money | Yes |
| 9 | Cost | money | Yes |
| 10 | VendorItemCode | varchar(50) | Yes |
| 11 | Alternate | varchar(512) | Yes |
| 12 | ItemsPerUnit | varchar(50) | Yes |
| 13 | Status | varchar(51) | Yes |
| 14 | ItemBidType | char(1) | Yes |
| 15 | PageNo | int | Yes |
| 16 | BidResultsActive | int | Yes |
| 17 | BidImportsActive | tinyint | Yes |
| 18 | SortStatus | int | Yes |
| 19 | Compliance | varchar(18) | No |

#### BidMgrView2 {view-dbo-bidmgrview2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-26 17:28:16.140000 |
| **Modified** | 2018-01-21 20:26:47.177000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | BidItemDiscountRate | decimal(9,5) | Yes |
| 5 | VendorBidNumber | varchar(50) | Yes |
| 6 | ItemsBid | int | Yes |
| 7 | AmountBid | money | Yes |
| 8 | VendorsCode | varchar(16) | Yes |
| 9 | VendorsName | varchar(50) | Yes |
| 10 | CatalogName | varchar(50) | Yes |
| 11 | BidId | int | Yes |
| 12 | AwardId | int | Yes |
| 13 | CalculatedItems | int | No |
| 14 | CalculatedAmount | int | No |
| 15 | CalculatedItemsBid | int | No |
| 16 | CalculatedAmountBid | int | No |
| 17 | PercentBid | int | No |
| 18 | CatalogDiscountRate | int | No |
| 19 | ItemsWon | int | No |
| 20 | PercentWon | int | No |
| 21 | POCount | int | No |
| 22 | TotalPOs | int | No |
| 23 | AveragePO | int | No |

#### BidMgrWeightView {view-dbo-bidmgrweightview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-26 13:36:12.207000 |
| **Modified** | 2018-01-21 20:26:47.183000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | weight | decimal(20,0) | Yes |

#### BidProjectAveragePO {view-dbo-bidprojectaveragepo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-12-22 13:52:32.337000 |
| **Modified** | 2018-01-21 20:26:47.187000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | No |
| 3 | VendorCode | varchar(16) | Yes |
| 4 | VendorName | varchar(50) | Yes |
| 5 | VendorInfo | varchar(376) | Yes |
| 6 | Items | int | No |
| 7 | Total | money | No |
| 8 | POCount | int | No |
| 9 | TotalQuantity | int | No |
| 10 | AvgPO | money | No |

#### BidRequestDetail {view-dbo-bidrequestdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2003-06-03 23:23:57.217000 |
| **Modified** | 2018-08-20 14:56:07.650000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestItemId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | CategoryId | int | Yes |
| 5 | DistrictId | int | Yes |
| 6 | RequisitionCount | int | Yes |
| 7 | ItemId | int | No |
| 8 | ItemCode | varchar(50) | Yes |
| 9 | ItemDescription | varchar(512) | Yes |
| 10 | UnitCode | varchar(20) | Yes |
| 11 | CrossReferencesText | varchar(1024) | No |
| 12 | BidRequest | int | Yes |
| 13 | BrandName | varchar(50) | Yes |
| 14 | ManufacturorNumber | varchar(50) | Yes |
| 15 | VendorName | varchar(50) | Yes |
| 16 | VendorPartNumber | varchar(50) | Yes |
| 17 | Keyword | varchar(50) | No |
| 18 | Title | varchar(255) | No |
| 19 | ExtraDetail | varchar(1153) | No |
| 20 | ItemsPerUnit | varchar(50) | Yes |
| 21 | SortSeq | varchar(64) | Yes |
| 22 | Status | varchar(50) | Yes |
| 23 | Comments | varchar(1024) | Yes |
| 24 | FullDescription | varchar(1024) | Yes |
| 25 | DistrictName | varchar(50) | Yes |
| 26 | CategoryType | int | Yes |
| 27 | Weight | real | Yes |
| 28 | HeadingDescription | varchar(4096) | No |

#### BidRequestDetail1 {view-dbo-bidrequestdetail1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-01-05 10:17:37.810000 |
| **Modified** | 2018-01-21 20:26:46.220000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestItemId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | CategoryId | int | Yes |
| 5 | DistrictId | int | Yes |
| 6 | RequisitionCount | int | Yes |
| 7 | ItemId | int | No |
| 8 | ItemCode | varchar(50) | Yes |
| 9 | ItemDescription | varchar(512) | Yes |
| 10 | UnitCode | varchar(20) | Yes |
| 11 | CrossReferencesText | varchar(1024) | Yes |
| 12 | BidRequest | int | Yes |
| 13 | BrandName | varchar(50) | Yes |
| 14 | ManufacturorNumber | varchar(50) | Yes |
| 15 | VendorName | varchar(50) | Yes |
| 16 | VendorPartNumber | varchar(50) | Yes |
| 17 | Keyword | varchar(50) | Yes |
| 18 | Title | varchar(255) | Yes |
| 19 | ExtraDetail | varchar(1153) | No |
| 20 | ItemsPerUnit | varchar(50) | Yes |
| 21 | SortSeq | varchar(64) | Yes |
| 22 | Status | varchar(50) | Yes |
| 23 | Comments | varchar(1024) | Yes |
| 24 | FullDescription | varchar(1024) | Yes |
| 25 | DistrictName | varchar(50) | Yes |
| 26 | CategoryType | int | Yes |
| 27 | Weight | real | Yes |

#### BidRequestDetail2 {view-dbo-bidrequestdetail2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-01-02 12:32:45.983000 |
| **Modified** | 2018-01-21 20:26:46.210000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestItemId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | CategoryId | int | Yes |
| 5 | DistrictId | int | Yes |
| 6 | RequisitionCount | int | Yes |
| 7 | ItemId | int | No |
| 8 | ItemCode | varchar(50) | Yes |
| 9 | ItemDescription | varchar(512) | Yes |
| 10 | UnitCode | varchar(20) | Yes |
| 11 | CrossReferencesText | varchar(1024) | Yes |
| 12 | BidRequest | int | Yes |
| 13 | BrandName | varchar(50) | Yes |
| 14 | ManufacturorNumber | varchar(50) | Yes |
| 15 | VendorName | varchar(50) | Yes |
| 16 | VendorPartNumber | varchar(50) | Yes |
| 17 | Keyword | varchar(50) | Yes |
| 18 | Title | varchar(255) | Yes |
| 19 | ExtraDetail | varchar(1153) | No |
| 20 | ItemsPerUnit | varchar(50) | Yes |
| 21 | SortSeq | varchar(64) | Yes |
| 22 | Status | varchar(50) | Yes |
| 23 | Comments | varchar(1024) | Yes |
| 24 | FullDescription | varchar(3650) | Yes |
| 25 | DistrictName | varchar(50) | Yes |
| 26 | CategoryType | int | Yes |
| 27 | Weight | real | Yes |

#### BidRequestItemsCrossRefsView {view-dbo-bidrequestitemscrossrefsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-06-03 19:20:38.780000 |
| **Modified** | 2018-01-21 20:26:47.190000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | CrossReferencesText | varchar(1024) | Yes |

#### BidRequestItemsView {view-dbo-bidrequestitemsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-06-06 01:42:35.310000 |
| **Modified** | 2018-01-21 20:26:47.193000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemId | int | No |
| 4 | ItemCode | varchar(50) | Yes |
| 5 | Description | varchar(512) | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | BidRequest | int | Yes |
| 8 | RequisitionCount | int | Yes |
| 9 | Active | tinyint | Yes |
| 10 | SortSeq | varchar(64) | Yes |

#### BidRequestItemsView1 {view-dbo-bidrequestitemsview1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-12-11 11:43:54.887000 |
| **Modified** | 2018-01-21 20:26:46.187000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemId | int | No |
| 4 | ItemCode | varchar(50) | Yes |
| 5 | Description | varchar(1665) | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | BidRequest | int | Yes |
| 8 | RequisitionCount | int | Yes |
| 9 | Active | tinyint | Yes |
| 10 | SortSeq | varchar(64) | Yes |
| 11 | Heading | varchar(308) | Yes |
| 12 | DistrictName | varchar(50) | Yes |
| 13 | CrossRefText | varchar(1024) | Yes |

#### BidRequestItemsView1Original {view-dbo-bidrequestitemsview1original}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-09-13 14:00:13.877000 |
| **Modified** | 2018-01-21 20:26:47.207000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemId | int | No |
| 4 | ItemCode | varchar(50) | Yes |
| 5 | Description | varchar(512) | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | BidRequest | int | Yes |
| 8 | RequisitionCount | int | Yes |
| 9 | Active | tinyint | Yes |
| 10 | SortSeq | varchar(64) | Yes |
| 11 | Heading | varchar(308) | Yes |
| 12 | DistrictName | varchar(50) | No |
| 13 | CrossRefText | varchar(1024) | Yes |

#### BidRequestItemsWeightView {view-dbo-bidrequestitemsweightview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-05-18 19:09:18.157000 |
| **Modified** | 2018-01-21 20:26:47.210000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | Weight | real | Yes |

#### BidResultsView {view-dbo-bidresultsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-03-23 22:52:47.440000 |
| **Modified** | 2018-01-21 20:26:47.213000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidResultsId | int | No |
| 2 | BidImportId | int | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | BidRequestItemId | int | Yes |
| 5 | CategoryId | int | Yes |
| 6 | DistrictId | int | Yes |
| 7 | ItemId | int | Yes |
| 8 | ItemCode | varchar(50) | Yes |
| 9 | Units | varchar(16) | Yes |
| 10 | Alternate | varchar(512) | Yes |
| 11 | Quantity | int | Yes |
| 12 | ItemBidType | char(1) | Yes |
| 13 | UnitPrice | money | Yes |
| 14 | Cost | money | Yes |
| 15 | VendorItemCode | varchar(50) | Yes |
| 16 | QuantityBid | int | Yes |
| 17 | ItemsPerUnit | varchar(50) | Yes |
| 18 | UnitId | int | Yes |
| 19 | Status | varchar(51) | Yes |
| 20 | Comments | varchar(1024) | Yes |
| 21 | Active | int | Yes |
| 22 | ItemDescription | varchar(1024) | Yes |
| 23 | SortSeq | varchar(64) | Yes |

#### BidsView {view-dbo-bidsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-06-06 01:44:22.403000 |
| **Modified** | 2018-01-21 20:26:47.220000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | Active | tinyint | Yes |
| 4 | EffectiveFrom | datetime | Yes |
| 5 | EffectiveUntil | datetime | Yes |
| 6 | BidName | varchar(255) | Yes |
| 7 | PricePlanId | int | No |
| 8 | PricePlanCode | varchar(20) | Yes |
| 9 | PricePlanDescription | varchar(255) | Yes |
| 10 | CategoryId | int | No |
| 11 | CategoryName | varchar(50) | Yes |
| 12 | VendorId | int | No |
| 13 | VendorCode | varchar(16) | Yes |
| 14 | VendorName | varchar(50) | Yes |
| 15 | BidDiscountRate | decimal(8,5) | Yes |
| 16 | VendorBidNumber | varchar(50) | Yes |
| 17 | DistrictId | int | No |
| 18 | DistrictCode | varchar(4) | Yes |
| 19 | DistrictName | varchar(50) | Yes |
| 20 | ItemsBid | int | Yes |
| 21 | AmountBid | money | Yes |
| 22 | CatalogId | int | No |
| 23 | CatalogName | varchar(50) | Yes |
| 24 | BidDescription | varchar(511) | Yes |

#### BudgetsView {view-dbo-budgetsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2005-11-15 10:02:04.540000 |
| **Modified** | 2018-01-21 20:26:47.227000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | BudgetId | int | No |
| 3 | Name | varchar(30) | Yes |
| 4 | EndDate | datetime | Yes |

#### CoverViewNew {view-dbo-coverviewnew}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2003-08-22 09:07:53.047000 |
| **Modified** | 2022-11-29 16:31:09.513000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |
| 30 | UsesBooklet | int | Yes |
| 31 | UsesOnline | int | Yes |
| 32 | RepMsg | varchar(237) | Yes |
| 33 | IBTypeId | int | No |
| 34 | BookType | varchar(50) | No |
| 35 | ScheduleGroup | varchar(50) | No |
| 36 | StateName | varchar(50) | No |

#### CoverViewNewSave {view-dbo-coverviewnewsave}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2003-09-15 19:20:24.437000 |
| **Modified** | 2018-01-21 20:26:47.260000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |

#### CoverViewNewTest {view-dbo-coverviewnewtest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-11-29 14:37:46.650000 |
| **Modified** | 2022-11-29 14:43:10.010000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |
| 30 | UsesBooklet | int | Yes |
| 31 | UsesOnline | int | Yes |
| 32 | RepMsg | varchar(237) | Yes |
| 33 | IBTypeId | int | No |
| 34 | BookType | varchar(50) | No |
| 35 | ScheduleGroup | varchar(50) | No |
| 36 | StateName | varchar(50) | No |

#### CoverViewNewTest1 {view-dbo-coverviewnewtest1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-11-29 15:53:52.133000 |
| **Modified** | 2022-11-29 16:01:23.983000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | Yes |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(255) | Yes |
| 29 | PricePlanDescription | varchar(255) | Yes |
| 30 | UsesBooklet | int | Yes |
| 31 | UsesOnline | int | Yes |
| 32 | RepMsg | varchar(237) | Yes |
| 33 | IBTypeId | int | No |
| 34 | BookType | varchar(50) | No |
| 35 | ScheduleGroup | varchar(50) | No |
| 36 | StateName | varchar(50) | No |

#### DetailView {view-dbo-detailview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 15:00:20.280000 |
| **Modified** | 2018-01-21 20:26:47.287000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | RequisitionId | int | Yes |
| 3 | CatalogId | int | Yes |
| 4 | ItemId | int | Yes |
| 5 | AddendumItem | tinyint | Yes |
| 6 | ItemCode | varchar(50) | Yes |
| 7 | Quantity | int | Yes |
| 8 | LastYearsQuantity | int | Yes |
| 9 | Description | varchar(1024) | Yes |
| 10 | UnitId | int | Yes |
| 11 | UnitCode | varchar(20) | Yes |
| 12 | BidPrice | money | Yes |
| 13 | CatalogPrice | money | Yes |
| 14 | GrossPrice | money | Yes |
| 15 | DiscountRate | decimal(9,5) | Yes |
| 16 | CatalogPage | char(4) | Yes |
| 17 | PricePlanId | int | Yes |
| 18 | PriceId | int | Yes |
| 19 | AwardId | int | Yes |
| 20 | VendorId | int | Yes |
| 21 | VendorItemCode | varchar(50) | Yes |
| 22 | Alternate | varchar(1024) | Yes |
| 23 | POId | int | Yes |
| 24 | BatchDetailId | int | Yes |
| 25 | Modified | datetime | Yes |
| 26 | ModifiedById | int | Yes |
| 27 | SourceId | int | Yes |
| 28 | SortSeq | varchar(64) | Yes |
| 29 | BidItemId | int | Yes |
| 30 | ExtraDescription | varchar(1024) | Yes |
| 31 | ReProc | tinyint | Yes |
| 32 | UseGrossPrices | tinyint | Yes |
| 33 | BidHeaderId | int | Yes |
| 34 | DistrictRequisitionNumber | varchar(50) | Yes |
| 35 | HeadingTitle | varchar(255) | Yes |
| 36 | Keyword | varchar(50) | Yes |
| 37 | SectionId | int | Yes |
| 38 | SectionName | varchar(255) | Yes |
| 39 | OriginalItemId | int | Yes |
| 40 | HeadingId | int | Yes |
| 41 | KeywordId | int | Yes |
| 42 | ItemMustBeBid | int | Yes |
| 43 | SessionId | int | Yes |
| 44 | Active | tinyint | Yes |
| 45 | RTK_MSDSId | int | Yes |

#### DistrictContactProblemView {view-dbo-districtcontactproblemview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-20 16:04:43.977000 |
| **Modified** | 2018-01-21 20:26:47.290000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | District | varchar(50) | Yes |
| 2 | ContactType | varchar(50) | No |
| 3 | MissingContact | int | No |
| 4 | MissingEmail | int | No |
| 5 | ErrorMessage | varchar(270) | No |
| 6 | DistrictId | int | No |
| 7 | DistrictContactId | int | Yes |
| 8 | DistrictContactTypeId | int | No |
| 9 | CSRepId | int | Yes |
| 10 | RepName | varchar(30) | Yes |

#### DistrictUsersView {view-dbo-districtusersview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-01-21 12:59:33.153000 |
| **Modified** | 2018-01-21 20:26:47.297000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictCode | varchar(4) | Yes |
| 2 | DistrictName | varchar(50) | Yes |
| 3 | SchoolName | varchar(50) | Yes |
| 4 | UserName | varchar(10) | Yes |
| 5 | CometCode | varchar(5) | Yes |
| 6 | Attention | varchar(50) | Yes |
| 7 | ApprovalLevel | tinyint | Yes |
| 8 | ApproveeCount | int | Yes |
| 9 | ApproverName | varchar(50) | Yes |
| 10 | PriorReqs | int | Yes |

#### InstructionBookCalendar {view-dbo-instructionbookcalendar}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-10-30 13:45:54.530000 |
| **Modified** | 2018-01-21 20:26:47.300000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | IBTypeId | int | No |
| 2 | StateId | int | Yes |
| 3 | GroupId | int | No |
| 4 | IBYear | int | No |
| 5 | EventDescription | varchar(50) | Yes |
| 6 | EventDate | datetime | No |

#### InstructionBookView {view-dbo-instructionbookview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-10-20 22:49:07.090000 |
| **Modified** | 2018-06-01 14:30:17.740000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | No |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(14) | Yes |
| 29 | PricePlanDescription | int | Yes |
| 30 | UsesBooklet | int | No |
| 31 | UsesOnline | int | No |
| 32 | RepMsg | varchar(237) | Yes |
| 33 | IBTypeId | int | No |
| 34 | BookType | varchar(50) | No |
| 35 | StateName | varchar(50) | No |
| 36 | ScheduleGroup | varchar(50) | No |

#### InstructionBookView09 {view-dbo-instructionbookview09}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-10 15:37:07.427000 |
| **Modified** | 2018-01-21 20:26:47.313000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | No |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(15) | Yes |
| 29 | PricePlanDescription | int | Yes |
| 30 | UsesBooklet | int | No |
| 31 | UsesOnline | int | No |
| 32 | RepMsg | varchar(237) | Yes |

#### InstructionBookViewCF {view-dbo-instructionbookviewcf}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-03-04 23:27:54.410000 |
| **Modified** | 2018-01-21 20:26:47.330000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | No |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(14) | Yes |
| 29 | PricePlanDescription | int | Yes |
| 30 | UsesBooklet | int | No |
| 31 | UsesOnline | int | No |
| 32 | RepMsg | varchar(305) | Yes |
| 33 | IBTypeId | int | No |
| 34 | BookType | varchar(50) | No |
| 35 | StateName | varchar(50) | No |
| 36 | ScheduleGroup | varchar(50) | No |

#### InstructionBookViewCF2013 {view-dbo-instructionbookviewcf2013}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-09-26 10:36:41.810000 |
| **Modified** | 2019-10-21 17:51:53.500000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | No |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | varchar(5) | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(14) | Yes |
| 29 | PricePlanDescription | int | Yes |
| 30 | UsesBooklet | int | No |
| 31 | UsesOnline | int | No |
| 32 | RepMsg | varchar(305) | Yes |
| 33 | IBTypeId | int | No |
| 34 | BookType | varchar(50) | No |
| 35 | StateName | varchar(50) | No |
| 36 | ScheduleGroup | varchar(50) | No |
| 37 | AllowAddenda | bit | No |
| 38 | AllowVendorChanges | int | No |
| 39 | BudgetId | int | No |
| 40 | AllowAccountCodeMgmt | tinyint | No |
| 41 | HasAdminAccess | bit | No |

#### InstructionBookViewwork {view-dbo-instructionbookviewwork}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-10-07 22:26:42.057000 |
| **Modified** | 2018-01-21 20:26:47.363000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictAddress1 | varchar(30) | Yes |
| 5 | DistrictAddress2 | varchar(30) | Yes |
| 6 | DistrictAddress3 | varchar(30) | Yes |
| 7 | DistrictCity | varchar(25) | Yes |
| 8 | DistrictState | varchar(2) | Yes |
| 9 | DistrictZipcode | varchar(10) | Yes |
| 10 | SchoolId | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | SchoolAddress1 | varchar(30) | Yes |
| 13 | SchoolAddress2 | varchar(30) | Yes |
| 14 | SchoolAddress3 | varchar(30) | Yes |
| 15 | SchoolCity | varchar(25) | Yes |
| 16 | SchoolState | varchar(2) | Yes |
| 17 | SchoolZipcode | varchar(10) | Yes |
| 18 | UserId | int | No |
| 19 | UserName | varchar(50) | Yes |
| 20 | CometId | int | Yes |
| 21 | AccountCode | varchar(50) | Yes |
| 22 | AccountCount | int | Yes |
| 23 | BudgetStartDate | datetime | Yes |
| 24 | BudgetEndDate | datetime | Yes |
| 25 | ItemCount | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | OrderBookId | int | Yes |
| 28 | CategoryDescription | varchar(15) | Yes |
| 29 | PricePlanDescription | int | Yes |
| 30 | UsesBooklet | int | No |
| 31 | UsesOnline | int | No |
| 32 | RepMsg | varchar(237) | Yes |

#### ItemsBidHeaderView {view-dbo-itemsbidheaderview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-06-06 13:49:42.780000 |
| **Modified** | 2018-01-21 20:26:47.370000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemId | int | No |
| 3 | ItemCode | varchar(565) | Yes |
| 4 | SortSeq | varchar(64) | Yes |

#### Keywords1 {view-dbo-keywords1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-11-14 21:09:45.773000 |
| **Modified** | 2018-01-21 20:26:47.373000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | KeywordId | int | No |
| 2 | Active | int | Yes |
| 3 | CategoryId | int | Yes |
| 4 | HeadingId | int | Yes |
| 5 | DistrictId | int | Yes |
| 6 | Keyword | varchar(50) | Yes |
| 7 | rowguid | uniqueidentifier | No |

#### NewFF1 {view-dbo-newff1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-11-14 21:09:46.163000 |
| **Modified** | 2018-01-21 20:26:47.380000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | ItemCode | varchar(50) | Yes |
| 3 | Description | varchar(512) | Yes |
| 4 | UnitId | int | Yes |
| 5 | Code | varchar(20) | Yes |
| 6 | CrossRefId | int | No |
| 7 | CatalogPrice | money | Yes |
| 8 | VendorItemCode | varchar(50) | Yes |
| 9 | Page | char(4) | Yes |
| 10 | BidPrice | decimal(34,13) | Yes |
| 11 | CatalogId | int | Yes |
| 12 | Name | varchar(50) | Yes |
| 13 | CategoryId | int | Yes |
| 14 | VendorId | int | No |
| 15 | VendorName | varchar(50) | Yes |
| 16 | PricePlanId | int | Yes |
| 17 | AwardId | int | No |
| 18 | DistrictId | int | Yes |
| 19 | DiscountRate | decimal(9,5) | Yes |
| 20 | PriceId | uniqueidentifier | No |
| 21 | PricesDescription | varchar(1024) | Yes |
| 22 | ParentCatalogId | int | Yes |
| 23 | GrossPrice | money | Yes |

#### OrderBookDetailView {view-dbo-orderbookdetailview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-11-07 12:39:48.150000 |
| **Modified** | 2018-01-21 20:26:47.383000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | OrderBookDetailId | int | No |
| 2 | OrderBookId | int | No |
| 3 | ItemCode | varchar(50) | Yes |
| 4 | UnitCode | varchar(20) | Yes |
| 5 | GrossPrice | money | Yes |
| 6 | CatalogPage | varchar(4) | Yes |
| 7 | CatalogYear | varchar(2) | Yes |
| 8 | VendorName | varchar(255) | Yes |
| 9 | VendorItemCode | varchar(50) | Yes |
| 10 | TotalQuantity | int | No |
| 11 | TotalRequisitions | int | No |
| 12 | ExpandAll | tinyint | Yes |
| 13 | Weight | int | No |
| 14 | SortSeq | varchar(64) | Yes |
| 15 | Active | tinyint | Yes |
| 16 | Alternate | varchar(1024) | Yes |
| 17 | VendorId | int | Yes |
| 18 | VendorCode | varchar(16) | Yes |
| 19 | ItemDescription | varchar(512) | Yes |
| 20 | HeadingId | int | Yes |
| 21 | HeadingCode | varchar(16) | Yes |
| 22 | HeadingTitle | varchar(255) | Yes |
| 23 | HeadingDescription | varchar(4096) | Yes |

#### OrderBookView {view-dbo-orderbookview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-11-07 12:36:08.113000 |
| **Modified** | 2018-01-21 20:26:47.390000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | OrderBookId | int | No |
| 2 | PricePlanDescription | varchar(255) | Yes |
| 3 | Category | varchar(255) | Yes |
| 4 | PricePlanId | int | Yes |
| 5 | CategoryId | int | Yes |
| 6 | AwardId | int | Yes |
| 7 | BookType | varchar(11) | No |
| 8 | Active | int | Yes |
| 9 | BidHeaderId | int | Yes |
| 10 | DistrictId | int | Yes |

#### POAttentionList {view-dbo-poattentionlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-04-16 14:58:19.607000 |
| **Modified** | 2018-01-21 20:26:47.420000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | PONumber | varchar(24) | Yes |
| 3 | AttentionName | varchar(50) | Yes |

#### PODetail {view-dbo-podetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-03-29 22:07:00.377000 |
| **Modified** | 2020-05-04 11:53:09.703000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(8000) | Yes |
| 5 | Quantity | int | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(68) | No |
| 12 | Alternate | varchar(17) | No |
| 13 | VendorItemCode | varchar(50) | No |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | Yes |
| 16 | POTotal | money | Yes |
| 17 | POItemCount | int | Yes |
| 18 | DiscountRate | decimal(9,5) | Yes |
| 19 | TotalGross | money | Yes |
| 20 | DiscountAmount | money | Yes |
| 21 | VendorNameAddress | varchar(320) | Yes |
| 22 | VendorPhone | varchar(25) | Yes |
| 23 | VendorFax | varchar(20) | Yes |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | Yes |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | Yes |
| 29 | DistrictUseGross | tinyint | Yes |
| 30 | AccountCode | varchar(50) | Yes |
| 31 | Attention | varchar(50) | Yes |
| 32 | CategoryName | varchar(50) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | Yes |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | Yes |
| 38 | ShippingAmount | money | Yes |
| 39 | VendorId | int | No |
| 40 | DistrictVendorCode | varchar(20) | Yes |
| 41 | BidAwardDate | datetime | Yes |
| 42 | BidHeaderId | int | Yes |
| 43 | VendorName | varchar(50) | Yes |
| 44 | VendorInfo | varchar(249) | Yes |

#### PODetailExport {view-dbo-podetailexport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2005-02-24 12:38:28.057000 |
| **Modified** | 2018-01-21 20:26:46.427000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(3650) | Yes |
| 5 | Quantity | int | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(50) | Yes |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | Yes |
| 16 | POTotal | money | Yes |
| 17 | POItemCount | int | Yes |
| 18 | DiscountRate | decimal(9,5) | Yes |
| 19 | TotalGross | money | Yes |
| 20 | DiscountAmount | money | Yes |
| 21 | VendorNameAddress | varchar(249) | Yes |
| 22 | VendorPhone | varchar(25) | Yes |
| 23 | VendorFax | varchar(20) | Yes |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | Yes |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | Yes |
| 29 | DistrictUseGross | tinyint | Yes |
| 30 | AccountCode | varchar(50) | Yes |
| 31 | Attention | varchar(50) | Yes |
| 32 | CategoryName | varchar(50) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | Yes |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | Yes |
| 38 | ShippingAmount | money | Yes |
| 39 | PODate | datetime | Yes |
| 40 | VendorId | int | No |
| 41 | DistrictName | varchar(50) | Yes |
| 42 | DistrictAddress1 | varchar(30) | Yes |
| 43 | DistrictAddress2 | varchar(30) | Yes |
| 44 | DistrictAddress3 | varchar(30) | Yes |
| 45 | DistrictCity | varchar(25) | Yes |
| 46 | DistrictState | varchar(2) | Yes |
| 47 | DistrictZip | varchar(10) | Yes |
| 48 | DistrictPhone | varchar(20) | Yes |
| 49 | DistrictFax | varchar(20) | Yes |
| 50 | DistrictEMail | varchar(255) | Yes |
| 51 | ShippingName | varchar(50) | Yes |
| 52 | ShippingAddress1 | varchar(30) | Yes |
| 53 | ShippingAddress2 | varchar(30) | Yes |
| 54 | ShippingAddress3 | varchar(30) | Yes |
| 55 | ShippingCity | varchar(25) | Yes |
| 56 | ShippingState | varchar(2) | Yes |
| 57 | ShippingZipCode | varchar(10) | Yes |
| 58 | ShippingPhone | varchar(20) | Yes |
| 59 | ShippingFax | varchar(14) | Yes |
| 60 | ShippingEMail | varchar(255) | Yes |
| 61 | VendorsAccountCode | varchar(50) | Yes |
| 62 | CometId | int | Yes |
| 63 | ShippingId | int | No |
| 64 | BusinessUnit | varchar(17) | Yes |
| 65 | UploadType | int | Yes |
| 66 | DistrictId | int | No |

#### PODetailExport_old {view-dbo-podetailexport-old}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-06-25 11:44:46.400000 |
| **Modified** | 2018-01-21 20:26:47.440000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(1024) | Yes |
| 5 | Quantity | int | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(50) | Yes |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | Yes |
| 16 | POTotal | money | Yes |
| 17 | POItemCount | int | Yes |
| 18 | DiscountRate | decimal(9,5) | Yes |
| 19 | TotalGross | money | Yes |
| 20 | DiscountAmount | money | Yes |
| 21 | VendorNameAddress | varchar(249) | Yes |
| 22 | VendorPhone | varchar(20) | Yes |
| 23 | VendorFax | varchar(20) | Yes |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | Yes |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | Yes |
| 29 | DistrictUseGross | tinyint | Yes |
| 30 | AccountCode | varchar(50) | Yes |
| 31 | Attention | varchar(50) | Yes |
| 32 | CategoryName | varchar(50) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | Yes |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | Yes |
| 38 | ShippingAmount | money | Yes |
| 39 | PODate | datetime | Yes |
| 40 | VendorId | int | No |
| 41 | DistrictName | varchar(50) | Yes |
| 42 | DistrictAddress1 | varchar(30) | Yes |
| 43 | DistrictAddress2 | varchar(30) | Yes |
| 44 | DistrictAddress3 | varchar(30) | Yes |
| 45 | DistrictCity | varchar(25) | Yes |
| 46 | DistrictState | varchar(2) | Yes |
| 47 | DistrictZip | varchar(10) | Yes |
| 48 | DistrictPhone | varchar(20) | Yes |
| 49 | DistrictFax | varchar(20) | Yes |
| 50 | DistrictEMail | varchar(255) | Yes |
| 51 | ShippingName | varchar(50) | Yes |
| 52 | ShippingAddress1 | varchar(30) | Yes |
| 53 | ShippingAddress2 | varchar(30) | Yes |
| 54 | ShippingAddress3 | varchar(30) | Yes |
| 55 | ShippingCity | varchar(25) | Yes |
| 56 | ShippingState | varchar(2) | Yes |
| 57 | ShippingZipCode | varchar(10) | Yes |
| 58 | ShippingPhone | varchar(20) | Yes |
| 59 | ShippingFax | varchar(14) | Yes |
| 60 | ShippingEMail | varchar(255) | Yes |
| 61 | VendorsAccountCode | varchar(50) | Yes |
| 62 | CometId | int | Yes |
| 63 | ShippingId | int | No |
| 64 | BusinessUnit | varchar(17) | Yes |
| 65 | UploadType | int | Yes |
| 66 | DistrictId | int | No |

#### PODetailJavaExport {view-dbo-podetailjavaexport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-04-06 15:11:25.843000 |
| **Modified** | 2025-12-30 10:54:54.407000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | nvarchar(MAX) | Yes |
| 5 | Quantity | int | No |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | No |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(255) | Yes |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | No |
| 16 | POTotal | money | No |
| 17 | POItemCount | int | No |
| 18 | DiscountRate | decimal(9,5) | No |
| 19 | TotalGross | money | No |
| 20 | DiscountAmount | money | No |
| 21 | VendorNameAddress | varchar(249) | Yes |
| 22 | VendorPhone | varchar(25) | No |
| 23 | VendorFax | varchar(20) | No |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | No |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | No |
| 29 | DistrictUseGross | tinyint | No |
| 30 | AccountCode | varchar(50) | No |
| 31 | Attention | varchar(50) | No |
| 32 | CategoryName | varchar(50) | No |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | No |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | No |
| 38 | ShippingAmount | money | No |
| 39 | PODate | datetime | Yes |
| 40 | VendorId | int | No |
| 41 | DistrictName | varchar(50) | No |
| 42 | DistrictAddress1 | varchar(50) | No |
| 43 | DistrictAddress2 | varchar(50) | No |
| 44 | DistrictAddress3 | varchar(1) | No |
| 45 | DistrictCity | varchar(50) | No |
| 46 | DistrictState | varchar(2) | No |
| 47 | DistrictZip | varchar(10) | No |
| 48 | DistrictPhone | nvarchar(MAX) | Yes |
| 49 | DistrictFax | nvarchar(MAX) | Yes |
| 50 | DistrictEMail | varchar(255) | No |
| 51 | ShippingName | varchar(50) | No |
| 52 | ShippingAddress1 | varchar(61) | Yes |
| 53 | ShippingAddress2 | varchar(30) | No |
| 54 | ShippingAddress3 | varchar(30) | No |
| 55 | ShippingCity | varchar(25) | No |
| 56 | ShippingState | varchar(2) | No |
| 57 | ShippingZipCode | varchar(10) | No |
| 58 | ShippingPhone | nvarchar(MAX) | Yes |
| 59 | ShippingFax | nvarchar(MAX) | Yes |
| 60 | ShippingEMail | varchar(255) | Yes |
| 61 | VendorsAccountCode | varchar(50) | Yes |
| 62 | CometId | int | Yes |
| 63 | ShippingId | varchar(50) | Yes |
| 64 | BusinessUnit | varchar(17) | No |
| 65 | UploadType | int | Yes |
| 66 | DistrictId | int | No |
| 67 | cXMLAddress | varchar(255) | No |
| 68 | UploadEmailList | varchar(4096) | No |
| 69 | cXMLFromDomain | varchar(50) | No |
| 70 | cXMLFromIdentity | varchar(50) | No |
| 71 | cXMLToDomain | varchar(50) | No |
| 72 | cXMLToIdentity | varchar(50) | No |
| 73 | cXMLSenderDomain | varchar(50) | No |
| 74 | cXMLSenderIdentity | varchar(50) | No |
| 75 | cXMLSenderSharedSecret | varchar(50) | No |
| 76 | dateSubmitted | datetime | No |
| 77 | isActualNumber | tinyint | No |
| 78 | hostUserName | varchar(255) | No |
| 79 | hostPassword | varchar(255) | No |
| 80 | RequestedDeliveryDate | date | Yes |
| 81 | DistrictContactId | int | Yes |
| 82 | PerishableItem | bit | Yes |

#### PODetailJavaExportNew {view-dbo-podetailjavaexportnew}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-20 10:40:29.500000 |
| **Modified** | 2018-01-21 20:26:46.320000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(3650) | Yes |
| 5 | Quantity | int | No |
| 6 | UnitCode | varchar(20) | No |
| 7 | GrossPrice | money | No |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(255) | Yes |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | No |
| 16 | POTotal | money | No |
| 17 | POItemCount | int | No |
| 18 | DiscountRate | decimal(9,5) | No |
| 19 | TotalGross | money | No |
| 20 | DiscountAmount | money | No |
| 21 | VendorNameAddress | varchar(249) | Yes |
| 22 | VendorPhone | varchar(25) | No |
| 23 | VendorFax | varchar(20) | No |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | No |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | No |
| 29 | DistrictUseGross | tinyint | No |
| 30 | AccountCode | varchar(50) | No |
| 31 | Attention | varchar(50) | No |
| 32 | CategoryName | varchar(50) | No |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | No |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | No |
| 38 | ShippingAmount | money | No |
| 39 | PODate | datetime | Yes |
| 40 | VendorId | int | No |
| 41 | DistrictName | varchar(50) | No |
| 42 | DistrictAddress1 | varchar(30) | No |
| 43 | DistrictAddress2 | varchar(30) | No |
| 44 | DistrictAddress3 | varchar(30) | No |
| 45 | DistrictCity | varchar(25) | No |
| 46 | DistrictState | varchar(2) | No |
| 47 | DistrictZip | varchar(10) | No |
| 48 | DistrictPhone | varchar(20) | No |
| 49 | DistrictFax | varchar(20) | No |
| 50 | DistrictEMail | varchar(255) | No |
| 51 | ShippingName | varchar(50) | No |
| 52 | ShippingAddress1 | varchar(30) | No |
| 53 | ShippingAddress2 | varchar(30) | No |
| 54 | ShippingAddress3 | varchar(30) | No |
| 55 | ShippingCity | varchar(25) | No |
| 56 | ShippingState | varchar(2) | No |
| 57 | ShippingZipCode | varchar(10) | No |
| 58 | ShippingPhone | varchar(20) | No |
| 59 | ShippingFax | varchar(14) | No |
| 60 | ShippingEMail | varchar(255) | No |
| 61 | VendorsAccountCode | varchar(50) | No |
| 62 | CometId | int | Yes |
| 63 | ShippingId | int | No |
| 64 | BusinessUnit | varchar(17) | No |
| 65 | UploadType | int | Yes |
| 66 | DistrictId | int | No |
| 67 | cXMLAddress | varchar(255) | No |
| 68 | UploadEmailList | varchar(4096) | No |

#### PODetailTest {view-dbo-podetailtest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-03-29 21:08:10.923000 |
| **Modified** | 2018-01-21 20:26:45.923000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(3650) | Yes |
| 5 | Quantity | int | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(50) | No |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | Yes |
| 16 | POTotal | money | Yes |
| 17 | POItemCount | int | Yes |
| 18 | DiscountRate | decimal(9,5) | Yes |
| 19 | TotalGross | money | Yes |
| 20 | DiscountAmount | money | Yes |
| 21 | VendorNameAddress | varchar(320) | Yes |
| 22 | VendorPhone | varchar(25) | Yes |
| 23 | VendorFax | varchar(20) | Yes |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | Yes |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | Yes |
| 29 | DistrictUseGross | tinyint | Yes |
| 30 | AccountCode | varchar(50) | Yes |
| 31 | Attention | varchar(50) | Yes |
| 32 | CategoryName | varchar(50) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | Yes |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | Yes |
| 38 | ShippingAmount | money | Yes |
| 39 | VendorId | int | No |
| 40 | DistrictVendorCode | varchar(20) | Yes |
| 41 | BidAwardDate | datetime | Yes |

#### PODetail_Orig {view-dbo-podetail-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-03-28 12:50:19.543000 |
| **Modified** | 2018-01-21 20:26:46.790000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(3650) | Yes |
| 5 | Quantity | int | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(50) | No |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | Yes |
| 16 | POTotal | money | Yes |
| 17 | POItemCount | int | Yes |
| 18 | DiscountRate | decimal(9,5) | Yes |
| 19 | TotalGross | money | Yes |
| 20 | DiscountAmount | money | Yes |
| 21 | VendorNameAddress | varchar(320) | Yes |
| 22 | VendorPhone | varchar(25) | Yes |
| 23 | VendorFax | varchar(20) | Yes |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | Yes |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | Yes |
| 29 | DistrictUseGross | tinyint | Yes |
| 30 | AccountCode | varchar(50) | Yes |
| 31 | Attention | varchar(50) | Yes |
| 32 | CategoryName | varchar(50) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | Yes |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | Yes |
| 38 | ShippingAmount | money | Yes |
| 39 | VendorId | int | No |
| 40 | DistrictVendorCode | varchar(20) | Yes |
| 41 | BidAwardDate | datetime | Yes |

#### PODetail_old {view-dbo-podetail-old}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-06-25 11:44:21.713000 |
| **Modified** | 2018-01-21 20:26:47.427000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PODetailItemId | int | No |
| 2 | DetailId | int | No |
| 3 | ItemCode | varchar(50) | No |
| 4 | Description | varchar(1024) | Yes |
| 5 | Quantity | int | Yes |
| 6 | UnitCode | varchar(20) | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | ExtendedGross | money | Yes |
| 9 | BidPrice | money | No |
| 10 | ExtendedBid | money | Yes |
| 11 | VendorData | varchar(1075) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | VendorItemCode | varchar(50) | No |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | Yes |
| 16 | POTotal | money | Yes |
| 17 | POItemCount | int | Yes |
| 18 | DiscountRate | decimal(9,5) | Yes |
| 19 | TotalGross | money | Yes |
| 20 | DiscountAmount | money | Yes |
| 21 | VendorNameAddress | varchar(249) | Yes |
| 22 | VendorPhone | varchar(20) | Yes |
| 23 | VendorFax | varchar(20) | Yes |
| 24 | VendorBidNumber | varchar(50) | Yes |
| 25 | VendorUseGross | int | Yes |
| 26 | SchoolNameAddress | varchar(189) | Yes |
| 27 | DistrictNameAddress | varchar(189) | Yes |
| 28 | DistrictCode | varchar(4) | Yes |
| 29 | DistrictUseGross | tinyint | Yes |
| 30 | AccountCode | varchar(50) | Yes |
| 31 | Attention | varchar(50) | Yes |
| 32 | CategoryName | varchar(50) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | LocationCode | varchar(32) | No |
| 35 | SortSeq | varchar(64) | Yes |
| 36 | ShippingNameAddress | varchar(189) | Yes |
| 37 | ShippingPercentage | decimal(9,5) | Yes |
| 38 | ShippingAmount | money | Yes |
| 39 | VendorId | int | No |
| 40 | DistrictVendorCode | varchar(20) | Yes |
| 41 | BidAwardDate | datetime | Yes |

#### POHeader {view-dbo-poheader}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-03-25 01:00:29.123000 |
| **Modified** | 2025-06-04 15:31:10.653000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | No |
| 2 | PONumber | varchar(24) | Yes |
| 3 | ItemCount | int | Yes |
| 4 | Amount | money | Yes |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | RequisitionNumber | varchar(24) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | CometId | int | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | DistrictNameAddress | varchar(237) | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | SchoolNameAddress | varchar(189) | Yes |
| 15 | VendorCode | varchar(16) | Yes |
| 16 | VendorPhone | varchar(25) | Yes |
| 17 | DistrictVendorCode | varchar(20) | Yes |
| 18 | VendorName | varchar(50) | Yes |
| 19 | VendorNameAddress | varchar(249) | Yes |
| 20 | PODate | datetime | Yes |
| 21 | DatePrinted | datetime | Yes |
| 22 | DatePrintedDetail | datetime | Yes |
| 23 | DateExported | datetime | Yes |
| 24 | DistrictId | int | Yes |
| 25 | CategoryId | int | Yes |
| 26 | BudgetId | int | Yes |
| 27 | AccountId | int | No |
| 28 | VendorId | int | Yes |
| 29 | UserId | int | Yes |
| 30 | SchoolId | int | No |
| 31 | VendorBidNumber | varchar(50) | Yes |
| 32 | VendorBidComments | varchar(606) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | CategoryName | varchar(50) | Yes |
| 35 | DiscountRate | decimal(9,5) | Yes |
| 36 | DiscountAmount | money | Yes |
| 37 | TotalGross | money | Yes |
| 38 | LocationCode | varchar(32) | No |
| 39 | ShippingAmount | money | Yes |
| 40 | ShippingPercentage | decimal(9,5) | Yes |
| 41 | ShippingNameAddress | varchar(189) | Yes |
| 42 | DistrictAddress1 | varchar(30) | Yes |
| 43 | DistrictAddress2 | varchar(30) | Yes |
| 44 | DistrictAddress3 | varchar(30) | Yes |
| 45 | DistrictCity | varchar(25) | Yes |
| 46 | DistrictState | varchar(2) | Yes |
| 47 | DistrictZipcode | varchar(10) | Yes |
| 48 | SchoolAddress1 | varchar(30) | Yes |
| 49 | SchoolAddress2 | varchar(30) | Yes |
| 50 | SchoolAddress3 | varchar(30) | Yes |
| 51 | SchoolCity | varchar(25) | Yes |
| 52 | SchoolState | varchar(2) | Yes |
| 53 | SchoolZipcode | varchar(10) | Yes |
| 54 | VendorsAddress1 | varchar(50) | Yes |
| 55 | VendorsAddress2 | varchar(50) | Yes |
| 56 | VendorsAddress3 | varchar(50) | Yes |
| 57 | VendorsCity | varchar(50) | Yes |
| 58 | VendorsState | varchar(2) | Yes |
| 59 | VendorsZipcode | varchar(10) | Yes |
| 60 | ShipLocationsAddress1 | varchar(30) | Yes |
| 61 | ShipLocationsAddress2 | varchar(30) | Yes |
| 62 | ShipLocationsAddress3 | varchar(30) | Yes |
| 63 | ShipLocationsCity | varchar(25) | Yes |
| 64 | ShipLocationsState | varchar(2) | Yes |
| 65 | ShipLocationsZipcode | varchar(10) | Yes |
| 66 | ShipLocationsName | varchar(50) | Yes |
| 67 | DistrictMessage | varchar(4096) | Yes |
| 68 | BidDate | datetime | Yes |
| 69 | UsersDistrictAcctgCode | varchar(20) | Yes |
| 70 | AwardsBidHeaderId | int | Yes |
| 71 | ExportedToVendor | datetime | Yes |
| 72 | ePOSuppressed | tinyint | Yes |

#### POHeaderSummary {view-dbo-poheadersummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2003-06-30 12:55:46.187000 |
| **Modified** | 2025-11-24 19:09:05.147000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | Yes |
| 2 | PONumber | varchar(24) | Yes |
| 3 | ItemCount | int | Yes |
| 4 | Amount | money | Yes |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | RequisitionNumber | varchar(24) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | CometId | int | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | DistrictNameAddress | varchar(189) | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | SchoolNameAddress | varchar(189) | Yes |
| 15 | VendorCode | varchar(16) | Yes |
| 16 | VendorPhone | varchar(25) | Yes |
| 17 | VendorFax | varchar(20) | Yes |
| 18 | DistrictVendorCode | varchar(20) | Yes |
| 19 | VendorName | varchar(50) | Yes |
| 20 | VendorNameAddress | varchar(249) | Yes |
| 21 | PODate | datetime | Yes |
| 22 | DatePrinted | datetime | Yes |
| 23 | DatePrintedDetail | datetime | Yes |
| 24 | DateExported | datetime | Yes |
| 25 | DistrictId | int | No |
| 26 | CategoryId | int | Yes |
| 27 | BudgetId | int | No |
| 28 | AccountId | int | No |
| 29 | VendorId | int | Yes |
| 30 | UserId | int | Yes |
| 31 | SchoolId | int | Yes |
| 32 | VendorBidNumber | varchar(50) | No |
| 33 | VendorBidComments | varchar(606) | Yes |
| 34 | CategoryCode | varchar(16) | Yes |
| 35 | CategoryName | varchar(50) | Yes |
| 36 | DiscountRate | decimal(38,6) | Yes |
| 37 | DiscountAmount | money | Yes |
| 38 | TotalGross | money | Yes |
| 39 | LocationCode | varchar(32) | Yes |
| 40 | ShippingAmount | money | Yes |
| 41 | ShippingPercentage | decimal(9,5) | Yes |
| 42 | ShippingNameAddress | varchar(189) | Yes |
| 43 | DistrictAddress1 | varchar(30) | Yes |
| 44 | DistrictAddress2 | varchar(30) | Yes |
| 45 | DistrictAddress3 | varchar(30) | Yes |
| 46 | DistrictCity | varchar(25) | Yes |
| 47 | DistrictState | varchar(2) | Yes |
| 48 | DistrictZipcode | varchar(10) | Yes |
| 49 | SchoolAddress1 | varchar(30) | Yes |
| 50 | SchoolAddress2 | varchar(30) | Yes |
| 51 | SchoolAddress3 | varchar(30) | Yes |
| 52 | SchoolCity | varchar(25) | Yes |
| 53 | SchoolState | varchar(2) | Yes |
| 54 | SchoolZipcode | varchar(10) | Yes |
| 55 | VendorsAddress1 | varchar(50) | Yes |
| 56 | VendorsAddress2 | varchar(50) | Yes |
| 57 | VendorsAddress3 | varchar(50) | Yes |
| 58 | VendorsCity | varchar(50) | Yes |
| 59 | VendorsState | varchar(2) | Yes |
| 60 | VendorsZipcode | varchar(10) | Yes |
| 61 | ShipLocationsAddress1 | varchar(30) | Yes |
| 62 | ShipLocationsAddress2 | varchar(30) | Yes |
| 63 | ShipLocationsAddress3 | varchar(30) | Yes |
| 64 | ShipLocationsCity | varchar(25) | Yes |
| 65 | ShipLocationsState | varchar(2) | Yes |
| 66 | ShipLocationsZipcode | varchar(10) | Yes |
| 67 | ShipLocationsName | varchar(50) | Yes |
| 68 | DistrictMessage | varchar(4096) | Yes |
| 69 | BidDate | datetime | Yes |
| 70 | UsersDistrictAcctgCode | varchar(20) | Yes |
| 71 | AwardsBidHeaderId | int | Yes |
| 72 | ExportedToVendor | datetime | Yes |

#### POHeaderSummary_04232018 {view-dbo-poheadersummary-04232018}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-04-23 15:43:38.080000 |
| **Modified** | 2018-04-23 15:43:38.080000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | Yes |
| 2 | PONumber | varchar(24) | Yes |
| 3 | ItemCount | int | Yes |
| 4 | Amount | money | Yes |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | RequisitionNumber | varchar(24) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | CometId | int | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | DistrictNameAddress | varchar(189) | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | SchoolNameAddress | varchar(189) | Yes |
| 15 | VendorCode | varchar(16) | Yes |
| 16 | VendorPhone | varchar(25) | Yes |
| 17 | DistrictVendorCode | varchar(20) | Yes |
| 18 | VendorName | varchar(50) | Yes |
| 19 | VendorNameAddress | varchar(249) | Yes |
| 20 | PODate | datetime | Yes |
| 21 | DatePrinted | datetime | Yes |
| 22 | DatePrintedDetail | datetime | Yes |
| 23 | DateExported | datetime | Yes |
| 24 | DistrictId | int | No |
| 25 | CategoryId | int | Yes |
| 26 | BudgetId | int | No |
| 27 | AccountId | int | Yes |
| 28 | VendorId | int | Yes |
| 29 | UserId | int | Yes |
| 30 | SchoolId | int | Yes |
| 31 | VendorBidNumber | varchar(50) | No |
| 32 | VendorBidComments | varchar(540) | Yes |
| 33 | CategoryCode | varchar(16) | Yes |
| 34 | CategoryName | varchar(50) | Yes |
| 35 | DiscountRate | decimal(38,6) | Yes |
| 36 | DiscountAmount | money | Yes |
| 37 | TotalGross | money | Yes |
| 38 | LocationCode | varchar(32) | Yes |
| 39 | ShippingAmount | money | Yes |
| 40 | ShippingPercentage | decimal(9,5) | Yes |
| 41 | ShippingNameAddress | varchar(189) | Yes |
| 42 | DistrictAddress1 | varchar(30) | Yes |
| 43 | DistrictAddress2 | varchar(30) | Yes |
| 44 | DistrictAddress3 | varchar(30) | Yes |
| 45 | DistrictCity | varchar(25) | Yes |
| 46 | DistrictState | varchar(2) | Yes |
| 47 | DistrictZipcode | varchar(10) | Yes |
| 48 | SchoolAddress1 | varchar(30) | Yes |
| 49 | SchoolAddress2 | varchar(30) | Yes |
| 50 | SchoolAddress3 | varchar(30) | Yes |
| 51 | SchoolCity | varchar(25) | Yes |
| 52 | SchoolState | varchar(2) | Yes |
| 53 | SchoolZipcode | varchar(10) | Yes |
| 54 | VendorsAddress1 | varchar(50) | Yes |
| 55 | VendorsAddress2 | varchar(50) | Yes |
| 56 | VendorsAddress3 | varchar(50) | Yes |
| 57 | VendorsCity | varchar(50) | Yes |
| 58 | VendorsState | varchar(2) | Yes |
| 59 | VendorsZipcode | varchar(10) | Yes |
| 60 | ShipLocationsAddress1 | varchar(30) | Yes |
| 61 | ShipLocationsAddress2 | varchar(30) | Yes |
| 62 | ShipLocationsAddress3 | varchar(30) | Yes |
| 63 | ShipLocationsCity | varchar(25) | Yes |
| 64 | ShipLocationsState | varchar(2) | Yes |
| 65 | ShipLocationsZipcode | varchar(10) | Yes |
| 66 | ShipLocationsName | varchar(50) | Yes |
| 67 | DistrictMessage | varchar(4096) | Yes |
| 68 | BidDate | datetime | Yes |
| 69 | UsersDistrictAcctgCode | varchar(20) | Yes |
| 70 | AwardsBidHeaderId | int | Yes |
| 71 | ExportedToVendor | datetime | Yes |

#### POHeaderTest {view-dbo-poheadertest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2021-04-22 14:48:22.460000 |
| **Modified** | 2021-04-22 14:48:22.460000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | No |
| 2 | PONumber | varchar(24) | Yes |
| 3 | ItemCount | int | Yes |
| 4 | Amount | money | Yes |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | RequisitionNumber | varchar(24) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | CometId | int | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | DistrictNameAddress | varchar(237) | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | SchoolNameAddress | varchar(189) | Yes |
| 15 | VendorCode | varchar(16) | Yes |
| 16 | VendorPhone | varchar(25) | Yes |
| 17 | DistrictVendorCode | varchar(20) | Yes |
| 18 | VendorName | varchar(50) | Yes |
| 19 | VendorNameAddress | varchar(249) | Yes |
| 20 | PODate | datetime | Yes |
| 21 | DatePrinted | datetime | Yes |
| 22 | DatePrintedDetail | datetime | Yes |
| 23 | DateExported | datetime | Yes |
| 24 | DistrictId | int | Yes |
| 25 | CategoryId | int | Yes |
| 26 | BudgetId | int | Yes |
| 27 | AccountId | int | Yes |
| 28 | VendorId | int | Yes |
| 29 | UserId | int | Yes |
| 30 | SchoolId | int | No |
| 31 | VendorBidNumber | varchar(50) | Yes |
| 32 | VendorBidComments | varchar(540) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | CategoryName | varchar(50) | Yes |
| 35 | DiscountRate | decimal(9,5) | Yes |
| 36 | DiscountAmount | money | Yes |
| 37 | TotalGross | money | Yes |
| 38 | LocationCode | varchar(32) | No |
| 39 | ShippingAmount | money | Yes |
| 40 | ShippingPercentage | decimal(9,5) | Yes |
| 41 | ShippingNameAddress | varchar(189) | Yes |
| 42 | DistrictAddress1 | varchar(30) | Yes |
| 43 | DistrictAddress2 | varchar(30) | Yes |
| 44 | DistrictAddress3 | varchar(30) | Yes |
| 45 | DistrictCity | varchar(25) | Yes |
| 46 | DistrictState | varchar(2) | Yes |
| 47 | DistrictZipcode | varchar(10) | Yes |
| 48 | SchoolAddress1 | varchar(30) | Yes |
| 49 | SchoolAddress2 | varchar(30) | Yes |
| 50 | SchoolAddress3 | varchar(30) | Yes |
| 51 | SchoolCity | varchar(25) | Yes |
| 52 | SchoolState | varchar(2) | Yes |
| 53 | SchoolZipcode | varchar(10) | Yes |
| 54 | VendorsAddress1 | varchar(50) | Yes |
| 55 | VendorsAddress2 | varchar(50) | Yes |
| 56 | VendorsAddress3 | varchar(50) | Yes |
| 57 | VendorsCity | varchar(50) | Yes |
| 58 | VendorsState | varchar(2) | Yes |
| 59 | VendorsZipcode | varchar(10) | Yes |
| 60 | ShipLocationsAddress1 | varchar(30) | Yes |
| 61 | ShipLocationsAddress2 | varchar(30) | Yes |
| 62 | ShipLocationsAddress3 | varchar(30) | Yes |
| 63 | ShipLocationsCity | varchar(25) | Yes |
| 64 | ShipLocationsState | varchar(2) | Yes |
| 65 | ShipLocationsZipcode | varchar(10) | Yes |
| 66 | ShipLocationsName | varchar(50) | Yes |
| 67 | DistrictMessage | varchar(4096) | Yes |
| 68 | BidDate | datetime | Yes |
| 69 | UsersDistrictAcctgCode | varchar(20) | Yes |
| 70 | AwardsBidHeaderId | int | Yes |
| 71 | ExportedToVendor | datetime | Yes |

#### POHeader_Test {view-dbo-poheader-test}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-05-17 13:14:56.730000 |
| **Modified** | 2022-05-18 14:47:42.593000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | No |
| 2 | PONumber | varchar(24) | Yes |
| 3 | ItemCount | int | Yes |
| 4 | Amount | money | Yes |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | RequisitionNumber | varchar(24) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | CometId | int | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | DistrictNameAddress | varchar(237) | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | SchoolNameAddress | varchar(189) | Yes |
| 15 | VendorCode | varchar(16) | Yes |
| 16 | VendorPhone | varchar(25) | Yes |
| 17 | DistrictVendorCode | varchar(20) | Yes |
| 18 | VendorName | varchar(50) | Yes |
| 19 | VendorNameAddress | varchar(249) | Yes |
| 20 | PODate | datetime | Yes |
| 21 | DatePrinted | datetime | Yes |
| 22 | DatePrintedDetail | datetime | Yes |
| 23 | DateExported | datetime | Yes |
| 24 | DistrictId | int | Yes |
| 25 | CategoryId | int | Yes |
| 26 | BudgetId | int | Yes |
| 27 | AccountId | int | Yes |
| 28 | VendorId | int | Yes |
| 29 | UserId | int | Yes |
| 30 | SchoolId | int | No |
| 31 | VendorBidNumber | varchar(50) | Yes |
| 32 | VendorBidComments | varchar(540) | Yes |
| 33 | CategoryCode | char(1) | Yes |
| 34 | CategoryName | varchar(50) | Yes |
| 35 | DiscountRate | decimal(9,5) | Yes |
| 36 | DiscountAmount | money | Yes |
| 37 | TotalGross | money | Yes |
| 38 | LocationCode | varchar(32) | No |
| 39 | ShippingAmount | money | Yes |
| 40 | ShippingPercentage | decimal(9,5) | Yes |
| 41 | ShippingNameAddress | varchar(189) | Yes |
| 42 | DistrictAddress1 | varchar(30) | Yes |
| 43 | DistrictAddress2 | varchar(30) | Yes |
| 44 | DistrictAddress3 | varchar(30) | Yes |
| 45 | DistrictCity | varchar(25) | Yes |
| 46 | DistrictState | varchar(2) | Yes |
| 47 | DistrictZipcode | varchar(10) | Yes |
| 48 | SchoolAddress1 | varchar(30) | Yes |
| 49 | SchoolAddress2 | varchar(30) | Yes |
| 50 | SchoolAddress3 | varchar(30) | Yes |
| 51 | SchoolCity | varchar(25) | Yes |
| 52 | SchoolState | varchar(2) | Yes |
| 53 | SchoolZipcode | varchar(10) | Yes |
| 54 | VendorsAddress1 | varchar(50) | Yes |
| 55 | VendorsAddress2 | varchar(50) | Yes |
| 56 | VendorsAddress3 | varchar(50) | Yes |
| 57 | VendorsCity | varchar(50) | Yes |
| 58 | VendorsState | varchar(2) | Yes |
| 59 | VendorsZipcode | varchar(10) | Yes |
| 60 | ShipLocationsAddress1 | varchar(30) | Yes |
| 61 | ShipLocationsAddress2 | varchar(30) | Yes |
| 62 | ShipLocationsAddress3 | varchar(30) | Yes |
| 63 | ShipLocationsCity | varchar(25) | Yes |
| 64 | ShipLocationsState | varchar(2) | Yes |
| 65 | ShipLocationsZipcode | varchar(10) | Yes |
| 66 | ShipLocationsName | varchar(50) | Yes |
| 67 | DistrictMessage | varchar(4096) | Yes |
| 68 | BidDate | datetime | Yes |
| 69 | UsersDistrictAcctgCode | varchar(20) | Yes |
| 70 | AwardsBidHeaderId | int | Yes |
| 71 | ExportedToVendor | datetime | Yes |

#### PPCategoryView {view-dbo-ppcategoryview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2003-03-15 14:15:09.623000 |
| **Modified** | 2018-01-21 20:26:47.450000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PricePlanId | int | Yes |
| 2 | CategoryId | int | Yes |

#### PricePlanView {view-dbo-priceplanview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-11 18:29:06.960000 |
| **Modified** | 2025-10-27 20:02:29.210000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PricePlanId | int | No |
| 2 | Code | varchar(20) | Yes |

#### RTK_Item_StructureView {view-dbo-rtk-item-structureview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-08-09 16:16:59.090000 |
| **Modified** | 2018-01-21 20:26:47.583000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RTK_ItemsId | int | No |
| 2 | AlternateDesc | varchar(60) | No |
| 3 | ItemDesc | varchar(512) | No |
| 4 | MSDSDetail | nvarchar(MAX) | No |

#### ReqDetail {view-dbo-reqdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2002-05-08 13:23:53.013000 |
| **Modified** | 2018-01-21 20:26:47.457000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | Yes |
| 3 | SchoolId | int | Yes |
| 4 | UserId | int | Yes |
| 5 | BudgetId | int | Yes |
| 6 | BudgetAccountId | int | Yes |
| 7 | UserAccountId | int | Yes |
| 8 | CategoryId | int | Yes |
| 9 | ShippingId | int | Yes |
| 10 | Attention | varchar(50) | Yes |
| 11 | AccountCode | varchar(50) | Yes |
| 12 | DateEntered | datetime | Yes |
| 13 | ShippingPercent | decimal(9,5) | Yes |
| 14 | DiscountPercent | decimal(9,5) | Yes |
| 15 | ShippingCost | money | Yes |
| 16 | TotalItemsCost | money | Yes |
| 17 | TotalRequisitionCost | money | Yes |
| 18 | Comments | varchar(1023) | Yes |
| 19 | ApprovalRequired | tinyint | Yes |
| 20 | ApprovalId | int | Yes |
| 21 | ApprovalLevel | tinyint | Yes |
| 22 | StatusId | int | Yes |
| 23 | OrderDate | datetime | Yes |
| 24 | BidId | int | Yes |
| 25 | DateExported | datetime | Yes |
| 26 | DetailId | int | No |
| 27 | CatalogId | int | Yes |
| 28 | ItemId | int | Yes |
| 29 | AddendumItem | tinyint | Yes |
| 30 | ItemCode | varchar(50) | Yes |
| 31 | Quantity | int | Yes |
| 32 | LastYearsQuantity | int | Yes |
| 33 | Description | varchar(1024) | Yes |
| 34 | UnitId | int | Yes |
| 35 | UnitCode | varchar(20) | Yes |
| 36 | BidPrice | money | Yes |
| 37 | CatalogPrice | money | Yes |
| 38 | GrossPrice | money | Yes |
| 39 | DiscountRate | decimal(9,5) | Yes |
| 40 | CatalogPage | char(4) | Yes |
| 41 | PricePlanId | int | Yes |
| 42 | PriceId | int | Yes |
| 43 | AwardId | int | Yes |
| 44 | VendorId | int | Yes |
| 45 | VendorItemCode | varchar(50) | Yes |
| 46 | Alternate | varchar(1024) | Yes |
| 47 | POId | int | Yes |
| 48 | BatchDetailId | int | Yes |
| 49 | Modified | datetime | Yes |
| 50 | ModifiedById | int | Yes |
| 51 | SortSeq | varchar(64) | Yes |

#### RequisitionsView {view-dbo-requisitionsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2001-08-24 14:40:44.673000 |
| **Modified** | 2018-01-21 20:26:47.463000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | RequisitionNumber | varchar(24) | Yes |
| 4 | SchoolId | int | Yes |
| 5 | UserId | int | Yes |
| 6 | BudgetId | int | Yes |
| 7 | BudgetAccountId | int | Yes |
| 8 | UserAccountId | int | Yes |
| 9 | CategoryId | int | Yes |
| 10 | ShippingId | int | Yes |
| 11 | Attention | varchar(50) | Yes |
| 12 | DateEntered | datetime | Yes |
| 13 | ShippingPercent | decimal(9,5) | Yes |
| 14 | DiscountPercent | decimal(9,5) | Yes |
| 15 | ShippingCost | money | Yes |
| 16 | TotalItemsCost | money | Yes |
| 17 | TotalRequisitionCost | money | Yes |
| 18 | Comments | varchar(1023) | Yes |
| 19 | ApprovalRequired | tinyint | Yes |
| 20 | ApprovalId | int | Yes |
| 21 | OrderDate | datetime | Yes |
| 22 | DateExported | datetime | Yes |
| 23 | StatusId | int | Yes |

#### SearchItemsHeadingsView {view-dbo-searchitemsheadingsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-10-25 12:38:26.780000 |
| **Modified** | 2018-01-21 20:26:47.590000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | Title | varchar(255) | No |
| 3 | Description | varchar(4096) | Yes |
| 4 | HeadingId | int | Yes |
| 5 | SearchLetter | varchar(1) | No |

#### SearchItemsKeywordsView {view-dbo-searchitemskeywordsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-10-25 12:39:42.120000 |
| **Modified** | 2018-01-21 20:26:47.593000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | Title | varchar(255) | Yes |
| 3 | Description | varchar(4096) | Yes |
| 4 | HeadingId | int | Yes |
| 5 | Keyword | varchar(50) | Yes |
| 6 | KeywordId | int | Yes |

#### SearchItemsView {view-dbo-searchitemsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-10-25 10:18:32.500000 |
| **Modified** | 2018-01-21 20:26:47.600000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemId | int | No |
| 3 | ItemCode | varchar(50) | Yes |
| 4 | Description | varchar(512) | Yes |
| 5 | Code | varchar(20) | Yes |
| 6 | Title | varchar(255) | Yes |
| 7 | HeadingsDescription | varchar(4096) | Yes |
| 8 | Keyword | varchar(50) | Yes |
| 9 | SortSeq | varchar(64) | Yes |
| 10 | HeadingId | int | Yes |
| 11 | KeywordId | int | Yes |
| 12 | BidPrice | decimal(33,13) | Yes |

#### TMDistrictInfo {view-dbo-tmdistrictinfo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-27 17:07:40.987000 |
| **Modified** | 2018-01-21 20:26:47.617000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | TMSurveyId | int | No |
| 2 | Name | varchar(50) | Yes |
| 3 | County | varchar(50) | Yes |

#### TestAllFF {view-dbo-testallff}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-11-14 21:09:48.227000 |
| **Modified** | 2018-01-21 20:26:47.607000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | ItemCode | varchar(50) | Yes |
| 3 | Description | varchar(512) | Yes |
| 4 | UnitId | int | Yes |
| 5 | Code | varchar(20) | Yes |
| 6 | CrossRefId | int | No |
| 7 | CatalogPrice | money | Yes |
| 8 | VendorItemCode | varchar(50) | Yes |
| 9 | CatalogId | int | Yes |
| 10 | Name | varchar(50) | Yes |
| 11 | CategoryId | int | Yes |
| 12 | VendorId | int | Yes |
| 13 | VendorName | varchar(50) | Yes |
| 14 | AwardId | int | No |
| 15 | DistrictId | int | Yes |
| 16 | PriceId | uniqueidentifier | No |
| 17 | PricesDescription | varchar(1024) | Yes |
| 18 | PricePlanId | int | Yes |
| 19 | DiscountRate | decimal(9,5) | Yes |

#### TestFF {view-dbo-testff}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-11-14 21:09:48.303000 |
| **Modified** | 2018-01-21 20:26:47.613000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | ItemCode | varchar(50) | Yes |
| 3 | Description | varchar(512) | Yes |
| 4 | UnitId | int | Yes |
| 5 | Code | varchar(20) | Yes |
| 6 | CrossRefId | int | No |
| 7 | CatalogPrice | money | Yes |
| 8 | VendorItemCode | varchar(50) | Yes |
| 9 | CatalogId | int | Yes |
| 10 | Name | varchar(50) | Yes |
| 11 | CategoryId | int | Yes |
| 12 | VendorId | int | Yes |
| 13 | VendorName | varchar(50) | Yes |
| 14 | PricePlanId | int | Yes |
| 15 | AwardId | int | No |
| 16 | DistrictId | int | Yes |
| 17 | DiscountRate | decimal(5,2) | Yes |
| 18 | PriceId | uniqueidentifier | No |
| 19 | PricesDescription | varchar(1024) | Yes |

#### UploadView {view-dbo-uploadview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2005-05-17 09:11:53.780000 |
| **Modified** | 2018-01-21 20:26:47.620000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UploadId | int | No |
| 2 | FileName | varchar(255) | Yes |
| 3 | DateCreated | datetime | Yes |
| 4 | DateUploaded | datetime | No |
| 5 | Status | varchar(255) | Yes |
| 6 | VendorId | int | No |
| 7 | VendorName | varchar(50) | Yes |
| 8 | UploadEmailList | varchar(4096) | Yes |
| 9 | HostURL | varchar(255) | Yes |
| 10 | HostPort | int | Yes |
| 11 | HostDirectory | varchar(255) | Yes |
| 12 | HostUserName | varchar(255) | Yes |
| 13 | HostPassword | varchar(255) | Yes |
| 14 | DistrictId | int | No |
| 15 | DistrictName | varchar(50) | Yes |
| 16 | VendorAccountNumber | varchar(50) | Yes |

#### UserContactProblemView {view-dbo-usercontactproblemview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-03-07 16:18:23.023000 |
| **Modified** | 2018-01-21 20:26:47.627000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserName | varchar(10) | Yes |
| 2 | Attention | varchar(50) | Yes |
| 3 | ErrorMessage | varchar(270) | No |
| 4 | DistrictName | varchar(50) | Yes |
| 5 | DistrictId | int | No |
| 6 | RepName | varchar(30) | Yes |
| 7 | CSRepId | int | No |
| 8 | Active | tinyint | Yes |
| 9 | SchoolId | int | Yes |
| 10 | UserId | int | No |

#### UserListView {view-dbo-userlistview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2005-11-14 13:13:32.977000 |
| **Modified** | 2024-10-22 15:33:30.997000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SchoolName | varchar(50) | Yes |
| 2 | UserNumber | int | Yes |
| 3 | UserName | varchar(50) | Yes |
| 4 | Password | varchar(11) | No |
| 5 | Attention | varchar(50) | Yes |
| 6 | DistrictAccountingCode | varchar(20) | No |
| 7 | ShipLocation | varchar(50) | No |
| 8 | LocationCode | varchar(32) | No |
| 9 | AccountCode | varchar(50) | No |
| 10 | AllocationAmount | money | No |
| 11 | AllocationAvailable | numeric(19,4) | No |
| 12 | UseAllocations | tinyint | No |
| 13 | ApproverName | varchar(50) | No |
| 14 | SessionId | int | No |
| 15 | SchoolId | int | No |
| 16 | Email | varchar(255) | Yes |

#### UserTreeView {view-dbo-usertreeview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2003-12-15 17:10:37.340000 |
| **Modified** | 2024-10-22 15:34:17.513000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | DistrictId | int | Yes |
| 3 | SchoolId | int | Yes |
| 4 | ShippingId | int | Yes |
| 5 | UserName | varchar(50) | Yes |
| 6 | Password | varchar(11) | No |
| 7 | Attention | varchar(50) | Yes |
| 8 | ApprovalLevel | tinyint | Yes |
| 9 | CometId | int | Yes |
| 10 | DisableNewRequisition | tinyint | Yes |
| 11 | DistrictAcctgCode | varchar(20) | Yes |
| 12 | ApproverId | int | Yes |
| 13 | Children | int | Yes |

#### UsersApprovees {view-dbo-usersapprovees}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2004-01-07 10:00:17.810000 |
| **Modified** | 2018-01-21 20:26:47.637000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | CometId | int | Yes |
| 3 | Attention | varchar(50) | Yes |
| 4 | DisableNewRequisition | tinyint | No |
| 5 | DistrictAcctgCode | varchar(20) | Yes |
| 6 | SchoolName | varchar(50) | Yes |
| 7 | ApprovalLevelDescription | varchar(50) | Yes |
| 8 | ApproverId | int | Yes |

#### VendorBidLookup {view-dbo-vendorbidlookup}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-06-11 16:41:34.123000 |
| **Modified** | 2018-01-21 20:26:47.643000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | vendorbidid | varchar(50) | Yes |
| 2 | calendarid | int | Yes |
| 3 | code | varchar(16) | Yes |
| 4 | name | varchar(50) | Yes |
| 5 | priceplan | varchar(16) | Yes |
| 6 | categoryname | varchar(255) | Yes |
| 7 | state | char(2) | Yes |

#### VendorContactProblemView {view-dbo-vendorcontactproblemview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-10 14:24:45.887000 |
| **Modified** | 2018-01-21 20:26:47.650000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorName | varchar(50) | Yes |
| 2 | CODE | varchar(16) | Yes |
| 3 | ErrorMessage | varchar(270) | No |
| 4 | BidContactCount | int | Yes |
| 5 | POContactCount | int | Yes |
| 6 | FULLNAME | varchar(150) | Yes |
| 7 | EMAIL | varchar(255) | Yes |
| 8 | BIDCONTACT | tinyint | Yes |
| 9 | POCONTACT | tinyint | Yes |
| 10 | VENDORID | int | No |
| 11 | VENDORCONTACTID | int | Yes |
| 12 | Active | tinyint | Yes |

#### bidinfolookup {view-dbo-bidinfolookup}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-08-13 15:20:57.437000 |
| **Modified** | 2020-05-19 17:41:08.173000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | varchar(50) | Yes |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | PriceplanCode | varchar(20) | Yes |
| 4 | PricePlanDescription | varchar(278) | Yes |
| 5 | BidType | varchar(30) | No |
| 6 | BidYears | varchar(11) | Yes |
| 7 | BidAdDate | datetime | Yes |
| 8 | BidHeaderKey | int | No |

#### cfv_Districts {view-dbo-cfv-districts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-12 21:59:51.050000 |
| **Modified** | 2018-01-21 20:26:47.230000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | DistrictId | int | No |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictCode | varchar(4) | Yes |

#### cfv_Schools {view-dbo-cfv-schools}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-12 21:59:51.207000 |
| **Modified** | 2018-01-21 20:26:47.233000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | DistrictId | int | No |
| 3 | SchoolId | int | No |
| 4 | SchoolName | varchar(50) | Yes |

#### cfv_Users {view-dbo-cfv-users}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-12 22:01:46.917000 |
| **Modified** | 2018-01-21 20:26:47.237000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | DistrictId | int | No |
| 3 | SchoolId | int | No |
| 4 | UserId | int | No |
| 5 | UserName | varchar(56) | Yes |

#### cvw_NJSavings {view-dbo-cvw-njsavings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-07 22:22:06.287000 |
| **Modified** | 2018-01-21 20:26:47.270000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | BudgetName | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | CYDollars | varchar(30) | Yes |
| 6 | CYIncludedDollars | varchar(30) | Yes |
| 7 | CYIncludedPercent | int | Yes |
| 8 | CYExcludedDollars | varchar(30) | Yes |
| 9 | GTDollars | varchar(30) | Yes |
| 10 | GTYears | int | No |
| 11 | PricePlanCode | varchar(20) | Yes |
| 12 | County | varchar(50) | No |

#### cvw_NYSavings {view-dbo-cvw-nysavings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-16 14:11:41.673000 |
| **Modified** | 2018-01-21 20:26:47.273000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | Name | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | CYDollars | varchar(30) | Yes |
| 6 | CYIncludedDollars | varchar(30) | Yes |
| 7 | CYIncludedPercent | int | Yes |
| 8 | CYExcludedDollars | varchar(30) | Yes |
| 9 | GTDollars | varchar(30) | Yes |
| 10 | GTYears | int | No |
| 11 | PricePlanCode | varchar(20) | Yes |

#### cvw_Savings {view-dbo-cvw-savings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-01-28 12:20:34.997000 |
| **Modified** | 2018-01-21 20:26:47.280000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | BudgetName | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | CYDollars | varchar(30) | Yes |
| 6 | CYIncludedDollars | varchar(30) | Yes |
| 7 | CYIncludedPercent | int | Yes |
| 8 | CYExcludedDollars | varchar(30) | Yes |
| 9 | GTDollars | varchar(30) | Yes |
| 10 | GTYears | int | No |
| 11 | PricePlanCode | varchar(20) | Yes |
| 12 | County | varchar(50) | No |

#### pa_Accounts {view-dbo-pa-accounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:10:14.960000 |
| **Modified** | 2018-01-21 20:26:47.393000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | Yes |
| 2 | AccountId | int | Yes |
| 3 | Code | varchar(50) | Yes |

#### pa_Budgets {view-dbo-pa-budgets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:10:14.757000 |
| **Modified** | 2018-01-21 20:26:47.397000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | Yes |
| 2 | BudgetId | int | Yes |
| 3 | Name | varchar(30) | Yes |

#### pa_Category {view-dbo-pa-category}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:10:14.443000 |
| **Modified** | 2018-01-21 20:26:47.400000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | Yes |
| 2 | CategoryId | int | Yes |
| 3 | Name | varchar(50) | Yes |

#### pa_ReqList {view-dbo-pa-reqlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:55:03.713000 |
| **Modified** | 2018-01-21 20:26:47.403000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Accounts_Code | varchar(50) | Yes |
| 2 | ApprovalDescription | varchar(50) | Yes |
| 3 | ApprovalDate | datetime | Yes |
| 4 | CategoryName | varchar(50) | Yes |
| 5 | CometId | int | Yes |
| 6 | RequisitionNumber | varchar(24) | Yes |
| 7 | Requisitions_Attention | varchar(50) | Yes |
| 8 | AccountCode | varchar(50) | Yes |
| 9 | DateEntered | datetime | Yes |
| 10 | TotalRequisitionCost | money | Yes |
| 11 | BidHeaderId | int | Yes |
| 12 | PendingApprovals_SchoolId | int | Yes |
| 13 | PendingApprovals_UserId | int | Yes |
| 14 | PendingApprovals_BudgetId | int | Yes |
| 15 | PendingApprovals_AccountId | int | Yes |
| 16 | PendingApprovals_CategoryId | int | Yes |
| 17 | PendingApprovals_StatusId | int | Yes |
| 18 | PendingApprovals_ApprovalDate | datetime | Yes |
| 19 | PendingApprovals_ApprovalLevel | tinyint | Yes |
| 20 | SessionId | int | Yes |
| 21 | Tagged | int | No |
| 22 | RequisitionId | int | Yes |

#### pa_School {view-dbo-pa-school}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:10:14.867000 |
| **Modified** | 2018-01-21 20:26:47.410000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | Yes |
| 2 | SchoolId | int | Yes |
| 3 | Name | varchar(50) | Yes |

#### pa_Status {view-dbo-pa-status}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:10:15.163000 |
| **Modified** | 2018-01-21 20:26:47.410000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | Yes |
| 2 | StatusId | int | Yes |
| 3 | Name | varchar(50) | Yes |

#### pa_Users {view-dbo-pa-users}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-01-05 13:10:15.053000 |
| **Modified** | 2018-01-21 20:26:47.413000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | Yes |
| 2 | UserId | int | Yes |
| 3 | Attention | varchar(50) | Yes |

#### rs_DistrictSummary {view-dbo-rs-districtsummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-18 12:58:37.583000 |
| **Modified** | 2018-01-21 20:26:47.470000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | DistrictName | varchar(50) | Yes |
| 3 | ItemId | int | Yes |
| 4 | ItemCode | varchar(50) | Yes |
| 5 | SortSeq | varchar(50) | Yes |
| 6 | Description | varchar(1536) | Yes |
| 7 | UnitCode | varchar(16) | Yes |
| 8 | Quantity | int | Yes |
| 9 | VendorCode | varchar(10) | Yes |
| 10 | UnitPrice | money | Yes |
| 11 | ExtendedPrice | money | Yes |
| 12 | BidPrice | money | Yes |
| 13 | GrossPrice | money | Yes |
| 14 | DiscountRate | decimal(9,5) | Yes |
| 15 | UseGrossPrices | tinyint | Yes |
| 16 | VendorId | int | Yes |
| 17 | VendorItemCode | varchar(50) | Yes |
| 18 | Alternate | varchar(1024) | Yes |
| 19 | DistrictId | int | Yes |
| 20 | CategoryId | int | Yes |
| 21 | PricePlanId | int | Yes |
| 22 | AwardId | int | Yes |
| 23 | BudgetId | int | Yes |
| 24 | VendorTotal | money | Yes |
| 25 | VendorCount | int | Yes |
| 26 | CategoryTotal | money | Yes |
| 27 | CategoryCount | int | Yes |
| 28 | DistrictTotal | money | Yes |
| 29 | DistrictCount | int | Yes |
| 30 | ListId | int | Yes |
| 31 | BidHeaderId | int | Yes |

#### rs_DistrictSummaryAwardLetter {view-dbo-rs-districtsummaryawardletter}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-18 17:02:39.057000 |
| **Modified** | 2018-01-21 20:26:47.473000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | DistrictId | int | Yes |
| 3 | CategoryId | int | Yes |
| 4 | PricePlanId | int | Yes |
| 5 | VendorId | int | Yes |
| 6 | ItemsBid | int | Yes |
| 7 | AmountBid | money | Yes |
| 8 | ItemsAwarded | int | Yes |
| 9 | AmountAwarded | money | Yes |
| 10 | AwardId | int | Yes |
| 11 | BidDate | datetime | Yes |
| 12 | BidAwardDate | datetime | Yes |
| 13 | TotalItemsAwarded | int | Yes |
| 14 | TotalItemsBid | int | Yes |
| 15 | TotalAmountBid | money | Yes |
| 16 | TotalAmountAwarded | money | Yes |
| 17 | BidHeaderId | int | Yes |
| 18 | VendorCode | varchar(20) | Yes |
| 19 | VendorName | varchar(50) | Yes |

#### rs_DistrictSummaryVendors {view-dbo-rs-districtsummaryvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-18 17:02:07.260000 |
| **Modified** | 2018-01-21 20:26:47.477000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | VendorId | int | Yes |
| 3 | CategoryId | int | Yes |
| 4 | BidHeaderId | int | Yes |
| 5 | LineCount | int | Yes |
| 6 | GrossCost | money | Yes |
| 7 | DiscountAmount | money | Yes |
| 8 | NetCost | money | Yes |
| 9 | TotalLineCount | int | Yes |
| 10 | TotalGrossCost | money | Yes |
| 11 | TotalDiscountAmount | money | Yes |
| 12 | TotalNetCost | money | Yes |
| 13 | VendorCode | varchar(20) | Yes |
| 14 | VendorName | varchar(50) | Yes |

#### rs_SBSDetailRecap {view-dbo-rs-sbsdetailrecap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-03 15:49:53.447000 |
| **Modified** | 2018-01-21 20:26:47.560000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | RequisitionId | int | No |
| 3 | Attention | varchar(50) | Yes |
| 4 | AccountCode | varchar(50) | Yes |
| 5 | ItemCode | varchar(50) | Yes |
| 6 | Quantity | int | Yes |
| 7 | Description | varchar(1024) | Yes |
| 8 | UnitCode | varchar(20) | Yes |
| 9 | BidPrice | money | Yes |
| 10 | CatalogPrice | money | Yes |
| 11 | GrossPrice | money | Yes |
| 12 | DiscountRate | decimal(9,5) | No |
| 13 | CatalogPage | char(4) | Yes |
| 14 | BidTotal | money | Yes |
| 15 | VendorItemCode | varchar(50) | Yes |
| 16 | Alternate | varchar(1024) | Yes |
| 17 | GrossTotal | money | Yes |
| 18 | NetTotal | decimal(34,13) | Yes |
| 19 | VendorCode | varchar(16) | Yes |
| 20 | VendorName | varchar(50) | Yes |
| 21 | CategoryName | varchar(50) | Yes |
| 22 | CategoryCode | varchar(16) | Yes |
| 23 | BudgetName | varchar(30) | Yes |
| 24 | DistrictId | int | No |
| 25 | DistrictCode | varchar(4) | Yes |
| 26 | DistrictName | varchar(50) | Yes |
| 27 | SchoolId | int | No |
| 28 | SchoolName | varchar(50) | Yes |
| 29 | UserId | int | No |
| 30 | CometId | int | Yes |
| 31 | CategoryId | int | No |
| 32 | SortSeq | varchar(64) | Yes |
| 33 | BidType | tinyint | No |

#### rs_SBSReqRecap {view-dbo-rs-sbsreqrecap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-03 15:52:20.290000 |
| **Modified** | 2018-01-21 20:26:47.567000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | Attention | varchar(50) | Yes |
| 3 | AccountCode | varchar(50) | No |
| 4 | CategoryId | int | No |
| 5 | CategoryName | varchar(50) | Yes |
| 6 | CategoryCode | varchar(16) | Yes |
| 7 | BudgetName | varchar(30) | Yes |
| 8 | DistrictId | int | No |
| 9 | DistrictCode | varchar(4) | Yes |
| 10 | DistrictName | varchar(50) | Yes |
| 11 | SchoolId | int | No |
| 12 | SchoolName | varchar(50) | Yes |
| 13 | UserId | int | No |
| 14 | CometId | int | Yes |

#### rs_SBSVendorRecap {view-dbo-rs-sbsvendorrecap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-03 15:46:39.663000 |
| **Modified** | 2018-01-21 20:26:47.573000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | Attention | varchar(50) | Yes |
| 3 | CometId | int | Yes |
| 4 | ItemCount | int | Yes |
| 5 | GrossTotal | money | Yes |
| 6 | DiscountTotal | decimal(38,13) | Yes |
| 7 | NetTotal | decimal(38,13) | Yes |
| 8 | DiscountRate | varchar(16) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | CategoryCode | varchar(16) | Yes |
| 11 | BudgetName | varchar(30) | Yes |
| 12 | DistrictCode | varchar(4) | Yes |
| 13 | DistrictName | varchar(50) | Yes |
| 14 | UseGrossPrices | tinyint | Yes |
| 15 | SchoolName | varchar(50) | Yes |
| 16 | VendorCode | varchar(16) | Yes |
| 17 | VendorName | varchar(50) | Yes |
| 18 | CategoryId | int | No |
| 19 | UserId | int | No |
| 20 | AccountCode | varchar(50) | Yes |

#### rs_SBS_AccountRecap_District {view-dbo-rs-sbs-accountrecap-district}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 16:13:53.420000 |
| **Modified** | 2018-01-21 20:26:47.483000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCount | int | Yes |
| 3 | GrossTotal | money | Yes |
| 4 | DiscountTotal | decimal(38,13) | Yes |
| 5 | NetTotal | decimal(38,13) | Yes |
| 6 | AccountCode | varchar(50) | Yes |
| 7 | CategoryCode | char(1) | Yes |
| 8 | CategoryName | varchar(50) | Yes |
| 9 | DistrictCode | varchar(4) | Yes |
| 10 | DistrictName | varchar(50) | Yes |
| 11 | UseGrossPrices | tinyint | Yes |
| 12 | SchoolId | int | No |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | BudgetName | varchar(30) | Yes |
| 15 | CategoryId | int | No |
| 16 | DistrictId | int | No |

#### rs_SBS_AccountRecap_School {view-dbo-rs-sbs-accountrecap-school}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 16:19:54.217000 |
| **Modified** | 2018-01-21 20:26:47.490000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCount | int | Yes |
| 3 | GrossTotal | money | Yes |
| 4 | DiscountTotal | decimal(38,13) | Yes |
| 5 | NetTotal | decimal(38,13) | Yes |
| 6 | AccountCode | varchar(50) | Yes |
| 7 | CategoryCode | char(1) | Yes |
| 8 | CategoryName | varchar(50) | Yes |
| 9 | DistrictCode | varchar(4) | Yes |
| 10 | DistrictName | varchar(50) | Yes |
| 11 | UseGrossPrices | tinyint | Yes |
| 12 | SchoolId | int | No |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | BudgetName | varchar(30) | Yes |
| 15 | CategoryId | int | No |

#### rs_SBS_SchoolSummary {view-dbo-rs-sbs-schoolsummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 15:50:27.750000 |
| **Modified** | 2018-01-21 20:26:47.493000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | CategoryCode | varchar(16) | Yes |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | CategoryId | int | No |
| 5 | Attention | varchar(50) | Yes |
| 6 | AccountCode | varchar(50) | No |
| 7 | DistrictId | int | No |
| 8 | DistrictCode | varchar(4) | Yes |
| 9 | DistrictName | varchar(50) | Yes |
| 10 | SchoolId | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | BudgetName | varchar(30) | Yes |
| 13 | CometId | int | Yes |
| 14 | UserId | int | No |
| 15 | RequisitionId | int | No |

#### rs_SBS_SchoolSummary_Detail {view-dbo-rs-sbs-schoolsummary-detail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 16:30:18.653000 |
| **Modified** | 2018-01-21 20:26:46.450000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCode | varchar(50) | Yes |
| 3 | Description | varchar(2880) | Yes |
| 4 | CatalogPage | char(4) | Yes |
| 5 | UnitCode | varchar(20) | Yes |
| 6 | Quantity | int | Yes |
| 7 | BidPrice | money | Yes |
| 8 | GrossPrice | money | Yes |
| 9 | CatalogPrice | money | Yes |
| 10 | BidTotal | money | Yes |
| 11 | VendorItemCode | varchar(50) | Yes |
| 12 | Alternate | varchar(1024) | Yes |
| 13 | DiscountRate | int | No |
| 14 | GrossTotal | money | Yes |
| 15 | NetTotal | decimal(34,13) | Yes |
| 16 | VendorCode | varchar(16) | Yes |
| 17 | VendorName | varchar(50) | Yes |
| 18 | CategoryCode | char(1) | Yes |
| 19 | CategoryName | varchar(50) | Yes |
| 20 | RequisitionId | int | No |
| 21 | Attention | varchar(50) | Yes |
| 22 | AccountCode | varchar(50) | Yes |
| 23 | DistrictId | int | No |
| 24 | DistrictCode | varchar(4) | Yes |
| 25 | DistrictName | varchar(50) | Yes |
| 26 | SchoolId | int | No |
| 27 | SchoolName | varchar(50) | Yes |
| 28 | BudgetName | varchar(30) | Yes |
| 29 | CometId | int | Yes |
| 30 | UserId | int | No |
| 31 | SortSeq | varchar(64) | Yes |

#### rs_SBS_UserRecap_District {view-dbo-rs-sbs-userrecap-district}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 16:33:40.420000 |
| **Modified** | 2018-01-21 20:26:47.500000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCount | int | Yes |
| 3 | GrossTotal | money | Yes |
| 4 | DiscountTotal | decimal(38,13) | Yes |
| 5 | NetTotal | decimal(38,13) | Yes |
| 6 | Attention | varchar(50) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | CategoryCode | char(1) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | UseGrossPrices | tinyint | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | BudgetName | varchar(30) | Yes |
| 15 | CometId | int | Yes |
| 16 | CategoryId | int | No |
| 17 | DistrictId | int | No |
| 18 | SchoolId | int | No |

#### rs_SBS_UserRecap_School {view-dbo-rs-sbs-userrecap-school}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 16:38:25.263000 |
| **Modified** | 2018-01-21 20:26:47.507000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCount | int | Yes |
| 3 | GrossTotal | money | Yes |
| 4 | DiscountTotal | decimal(38,13) | Yes |
| 5 | NetTotal | decimal(38,13) | Yes |
| 6 | Attention | varchar(50) | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | CategoryCode | char(1) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | UseGrossPrices | tinyint | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | BudgetName | varchar(30) | Yes |
| 15 | CometId | int | Yes |
| 16 | CategoryId | int | No |
| 17 | SchoolId | int | No |

#### rs_SBS_VendorRecap_District {view-dbo-rs-sbs-vendorrecap-district}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 17:29:59.263000 |
| **Modified** | 2018-01-21 20:26:47.513000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | ItemCount | int | Yes |
| 5 | GrossTotal | money | Yes |
| 6 | DiscountTotal | decimal(38,13) | Yes |
| 7 | NetTotal | decimal(38,13) | Yes |
| 8 | CategoryCode | char(1) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | UseGrossPrices | tinyint | Yes |
| 13 | BudgetName | varchar(30) | Yes |
| 14 | DistrictId | int | No |
| 15 | CategoryId | int | No |
| 16 | DiscountRate | decimal(9,5) | Yes |

#### rs_SBS_VendorRecap_School {view-dbo-rs-sbs-vendorrecap-school}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 17:35:53.233000 |
| **Modified** | 2018-01-21 20:26:47.530000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | ItemCount | int | Yes |
| 5 | GrossTotal | money | Yes |
| 6 | DiscountTotal | decimal(38,13) | Yes |
| 7 | NetTotal | decimal(38,13) | Yes |
| 8 | CategoryCode | char(1) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | DistrictCode | varchar(4) | Yes |
| 11 | DistrictName | varchar(50) | Yes |
| 12 | UseGrossPrices | tinyint | Yes |
| 13 | SchoolName | varchar(50) | Yes |
| 14 | BudgetName | varchar(30) | Yes |
| 15 | SchoolId | int | No |
| 16 | CategoryId | int | No |
| 17 | DiscountRate | decimal(9,5) | Yes |

#### rs_SBS_VendorRecap_User {view-dbo-rs-sbs-vendorrecap-user}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 17:38:43.263000 |
| **Modified** | 2018-01-21 20:26:47.537000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | ItemCount | int | Yes |
| 5 | GrossTotal | money | Yes |
| 6 | DiscountTotal | decimal(38,13) | Yes |
| 7 | NetTotal | decimal(38,13) | Yes |
| 8 | CategoryCode | char(1) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | Attention | varchar(50) | Yes |
| 11 | DistrictCode | varchar(4) | Yes |
| 12 | DistrictName | varchar(50) | Yes |
| 13 | UseGrossPrices | tinyint | Yes |
| 14 | SchoolName | varchar(50) | Yes |
| 15 | BudgetName | varchar(30) | Yes |
| 16 | CometId | int | Yes |
| 17 | RequisitionId | int | No |
| 18 | DiscountRate | decimal(9,5) | Yes |

#### rs_SBS_VendorUserRecap_District {view-dbo-rs-sbs-vendoruserrecap-district}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 17:02:56.153000 |
| **Modified** | 2018-01-21 20:26:47.543000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCount | int | Yes |
| 3 | AwardId | int | Yes |
| 4 | GrossTotal | money | Yes |
| 5 | DiscountTotal | decimal(38,13) | Yes |
| 6 | NetTotal | decimal(38,13) | Yes |
| 7 | Attention | varchar(50) | Yes |
| 8 | AccountCode | varchar(50) | Yes |
| 9 | CategoryCode | char(1) | Yes |
| 10 | CategoryName | varchar(50) | Yes |
| 11 | DistrictCode | varchar(4) | Yes |
| 12 | DistrictName | varchar(50) | Yes |
| 13 | UseGrossPrices | tinyint | Yes |
| 14 | SchoolId | int | No |
| 15 | SchoolName | varchar(50) | Yes |
| 16 | BudgetName | varchar(30) | Yes |
| 17 | CometId | int | Yes |
| 18 | CategoryId | int | No |
| 19 | VendorId | int | No |
| 20 | VendorCode | varchar(16) | Yes |
| 21 | VendorName | varchar(50) | Yes |
| 22 | VendorPhone | varchar(20) | Yes |
| 23 | BidStartDate | datetime | Yes |
| 24 | BidEndDate | datetime | Yes |
| 25 | VendorBidNumber | varchar(50) | Yes |
| 26 | AwardDescription | varchar(511) | Yes |
| 27 | DistrictId | int | No |
| 28 | DiscountRate | decimal(9,5) | Yes |

#### rs_SBS_VendorUserRecap_School {view-dbo-rs-sbs-vendoruserrecap-school}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-11-14 17:04:52.060000 |
| **Modified** | 2018-01-21 20:26:47.553000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | ItemCount | int | Yes |
| 3 | AwardId | int | Yes |
| 4 | GrossTotal | money | Yes |
| 5 | DiscountTotal | decimal(38,13) | Yes |
| 6 | NetTotal | decimal(38,13) | Yes |
| 7 | Attention | varchar(50) | Yes |
| 8 | AccountCode | varchar(50) | Yes |
| 9 | CategoryCode | char(1) | Yes |
| 10 | CategoryName | varchar(50) | Yes |
| 11 | DistrictCode | varchar(4) | Yes |
| 12 | DistrictName | varchar(50) | Yes |
| 13 | UseGrossPrices | tinyint | Yes |
| 14 | SchoolId | int | No |
| 15 | SchoolName | varchar(50) | Yes |
| 16 | BudgetName | varchar(30) | Yes |
| 17 | CometId | int | Yes |
| 18 | CategoryId | int | No |
| 19 | VendorId | int | No |
| 20 | VendorCode | varchar(16) | Yes |
| 21 | VendorName | varchar(50) | Yes |
| 22 | VendorPhone | varchar(20) | Yes |
| 23 | BidStartDate | datetime | Yes |
| 24 | BidEndDate | datetime | Yes |
| 25 | VendorBidNumber | varchar(50) | Yes |
| 26 | AwardDescription | varchar(511) | Yes |
| 27 | DiscountRate | decimal(9,5) | Yes |

#### rs_VendorRecap {view-dbo-rs-vendorrecap}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2006-05-03 10:46:47.913000 |
| **Modified** | 2018-01-21 20:26:47.580000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | Attention | varchar(50) | Yes |
| 3 | CometId | int | Yes |
| 4 | ItemCount | int | Yes |
| 5 | GrossTotal | money | Yes |
| 6 | DiscountTotal | decimal(38,13) | Yes |
| 7 | NetTotal | decimal(38,13) | Yes |
| 8 | DiscountRate | varchar(16) | Yes |
| 9 | CategoryName | varchar(50) | Yes |
| 10 | CategoryCode | varchar(16) | Yes |
| 11 | BudgetName | varchar(30) | Yes |
| 12 | DistrictCode | varchar(4) | Yes |
| 13 | DistrictName | varchar(50) | Yes |
| 14 | UseGrossPrices | tinyint | Yes |
| 15 | SchoolName | varchar(50) | Yes |
| 16 | VendorCode | varchar(16) | Yes |
| 17 | VendorName | varchar(50) | Yes |

#### vw_ARAccounts {view-dbo-vw-araccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 11:49:23.407000 |
| **Modified** | 2018-01-21 20:26:47.670000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | AccountId | int | No |
| 4 | AccountCode | varchar(50) | No |

#### vw_ARBudgets {view-dbo-vw-arbudgets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 11:29:51.933000 |
| **Modified** | 2018-01-21 20:26:47.673000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | BudgetId | int | No |
| 4 | BudgetName | varchar(30) | No |

#### vw_ARCategories {view-dbo-vw-arcategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 11:34:51.227000 |
| **Modified** | 2018-01-21 20:26:47.677000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | CategoryId | int | No |
| 4 | CategoryName | varchar(50) | Yes |

#### vw_ARSchools {view-dbo-vw-arschools}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 11:43:07.897000 |
| **Modified** | 2018-01-21 20:26:47.680000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | SchoolId | int | No |
| 4 | SchoolName | varchar(50) | No |

#### vw_ARStatuses {view-dbo-vw-arstatuses}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 13:15:46.210000 |
| **Modified** | 2018-01-21 20:26:46.527000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | BudgetId | int | No |
| 4 | StatusId | int | No |
| 5 | StatusDesc | varchar(104) | No |
| 6 | StatusCode | int | No |

#### vw_ARUsers {view-dbo-vw-arusers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 12:32:26.713000 |
| **Modified** | 2018-01-21 20:26:47.683000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | UserId | int | No |
| 4 | UserNumber | int | No |
| 5 | Attention | varchar(50) | No |

#### vw_AVBidsVendorsCategoriesBySession {view-dbo-vw-avbidsvendorscategoriesbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-17 13:30:29.570000 |
| **Modified** | 2025-09-18 15:12:44.350000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | CategoryType | int | Yes |
| 5 | VendorId | int | No |
| 6 | VendorName | varchar(50) | Yes |
| 7 | VendorCode | varchar(16) | Yes |
| 8 | BidHeaderId | int | Yes |
| 9 | BidAdvertised | datetime | Yes |
| 10 | BidAwardDate | datetime | Yes |
| 11 | EffectiveFrom | datetime | Yes |
| 12 | EffectiveUntil | datetime | Yes |
| 13 | BidType | tinyint | No |
| 14 | VendorBidNumber | varchar(50) | Yes |
| 15 | Comments | varchar(1538) | Yes |
| 16 | Address1 | varchar(50) | Yes |
| 17 | Address2 | varchar(50) | Yes |
| 18 | City | varchar(50) | Yes |
| 19 | State | char(2) | Yes |
| 20 | Zipcode | varchar(10) | Yes |
| 21 | VendorContactFullName | varchar(150) | Yes |
| 22 | VendorContactEMail | varchar(255) | Yes |
| 23 | VendorContactPhone | varchar(25) | Yes |
| 24 | VendorContactFax | varchar(20) | Yes |
| 25 | CatalogId | int | Yes |
| 26 | BidYears | varchar(11) | Yes |
| 27 | BidMessage | varchar(1024) | Yes |

#### vw_AVCategoriesBySession {view-dbo-vw-avcategoriesbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-17 14:13:30.030000 |
| **Modified** | 2020-05-19 17:41:09.493000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |

#### vw_AVVendorsBySession {view-dbo-vw-avvendorsbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-17 14:15:02.220000 |
| **Modified** | 2020-05-19 17:41:09.897000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | Yes |
| 4 | VendorCode | varchar(16) | Yes |

#### vw_AVVendorsExport {view-dbo-vw-avvendorsexport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-03-14 09:20:56.187000 |
| **Modified** | 2024-04-22 19:59:15.387000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | No |
| 4 | ContactInfo | varchar(548) | Yes |
| 5 | CategoryId | int | No |
| 6 | CategoryName | varchar(308) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | VendorBidNumber | varchar(50) | No |
| 9 | AdditionalHandlingAmount | money | No |
| 10 | FreeHandlingAmount | money | No |
| 11 | BidComments | varchar(512) | No |
| 12 | EMail | varchar(255) | No |
| 13 | VendorCode | varchar(16) | No |
| 14 | DistrictVendorCode | varchar(20) | No |
| 15 | VendorsAccountCode | varchar(50) | No |

#### vw_ActiveBids {view-dbo-vw-activebids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2025-03-11 10:58:23.027000 |
| **Modified** | 2025-03-11 10:59:36.903000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidId | int | No |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | Yes |
| 5 | VendorCode | varchar(16) | Yes |
| 6 | CategoryId | int | No |
| 7 | CategoryName | varchar(50) | Yes |
| 8 | CategoryType | int | Yes |
| 9 | PricePlanId | int | No |
| 10 | PricePlan | varchar(20) | Yes |
| 11 | BidType | tinyint | Yes |

#### vw_ActiveCatalogs {view-dbo-vw-activecatalogs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2025-03-06 14:24:04.367000 |
| **Modified** | 2025-03-06 14:24:04.367000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | CatalogId | int | No |
| 5 | CatalogName | varchar(50) | Yes |
| 6 | VendorId | int | No |
| 7 | VendorName | varchar(50) | Yes |

#### vw_ActiveDistrictList {view-dbo-vw-activedistrictlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-03 15:15:55.473000 |
| **Modified** | 2018-01-21 20:26:47.653000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(50) | Yes |
| 2 | Address | varchar(50) | Yes |
| 3 | City | varchar(50) | Yes |
| 4 | State | varchar(2) | Yes |
| 5 | Zipcode | varchar(10) | Yes |
| 6 | BAName | varchar(174) | Yes |
| 7 | RTK | int | Yes |
| 8 | CooperativeBids | int | Yes |
| 9 | TimeAndMaterialBids | int | Yes |
| 10 | DistrictId | int | No |
| 11 | RepName | varchar(30) | Yes |
| 12 | RepEmail | varchar(128) | Yes |
| 13 | RepPhone | varchar(20) | Yes |

#### vw_ActiveVendors {view-dbo-vw-activevendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-07-14 11:30:29.520000 |
| **Modified** | 2018-01-21 20:26:47.660000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | Code | varchar(16) | Yes |
| 4 | Name | varchar(50) | Yes |
| 5 | Address1 | varchar(50) | Yes |
| 6 | Address2 | varchar(50) | Yes |
| 7 | Address3 | varchar(50) | Yes |
| 8 | City | varchar(25) | Yes |
| 9 | State | varchar(2) | Yes |
| 10 | ZipCode | varchar(10) | Yes |
| 11 | Phone | varchar(20) | Yes |
| 12 | Fax | varchar(20) | Yes |
| 13 | EMail | varchar(255) | Yes |
| 14 | UseGrossPrices | tinyint | Yes |
| 15 | ShippingPercentage | decimal(9,5) | Yes |
| 16 | DistrictId | int | Yes |
| 17 | Password | varchar(50) | Yes |
| 18 | HostURL | varchar(255) | Yes |
| 19 | HostPort | int | Yes |
| 20 | HostDirectory | varchar(255) | Yes |
| 21 | HostUserName | varchar(255) | Yes |
| 22 | HostPassword | varchar(255) | Yes |
| 23 | UploadEMailList | varchar(4096) | Yes |
| 24 | UploadType | int | Yes |
| 25 | BusinessUnit | varchar(17) | Yes |
| 26 | POPassword | varchar(50) | Yes |
| 27 | cXMLAddress | varchar(255) | Yes |
| 28 | VendorLogo | varbinary(MAX) | Yes |
| 29 | cXMLFromDomain | varchar(50) | Yes |
| 30 | cXMLFromIdentity | varchar(50) | Yes |
| 31 | cXMLToDomain | varchar(50) | Yes |
| 32 | cXMLToIdentity | varchar(50) | Yes |
| 33 | cXMLSenderDomain | varchar(50) | Yes |
| 34 | cXMLSenderIdentity | varchar(50) | Yes |
| 35 | cXMLSenderSharedSecret | varchar(50) | Yes |
| 36 | rowguid | uniqueidentifier | No |
| 37 | Contact | varchar(50) | Yes |

#### vw_ApprovalsHistory {view-dbo-vw-approvalshistory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-09-19 01:28:05.640000 |
| **Modified** | 2018-01-21 20:26:47.667000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | ApprovalDate | datetime | Yes |
| 3 | Submitter | varchar(56) | No |
| 4 | Approver | varchar(56) | No |
| 5 | StatusName | varchar(50) | No |

#### vw_ApproveRequisitions {view-dbo-vw-approverequisitions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-09-12 23:44:13.643000 |
| **Modified** | 2023-03-21 14:27:41.520000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | Yes |
| 3 | StatusID | int | No |
| 4 | StatusName | varchar(50) | No |
| 5 | TotalRequisitionCost | money | No |
| 6 | ApprovalLevel | tinyint | No |
| 7 | Attention | varchar(50) | Yes |
| 8 | CometId | varchar(5) | Yes |
| 9 | DateUpdated | datetime | Yes |
| 10 | NotesCount | int | No |
| 11 | OrderType | tinyint | No |
| 12 | OrderTypeDisplay | varchar(10) | No |
| 13 | UserDisplayName | varchar(56) | Yes |
| 14 | CategoryID | int | No |
| 15 | CategoryName | varchar(50) | Yes |
| 16 | BudgetID | int | No |
| 17 | AccountID | int | No |
| 18 | AccountCode | varchar(50) | No |
| 19 | DistrictID | int | No |
| 20 | DistrictName | varchar(50) | No |
| 21 | SchoolID | int | No |
| 22 | SchoolName | varchar(50) | Yes |
| 23 | UserID | int | No |
| 24 | UserAccountId | int | No |
| 25 | SessionId | int | No |
| 26 | AllocationAvailable | money | Yes |
| 27 | REQ_UAID | int | Yes |
| 28 | UseBudgetAccountAllocations | tinyint | No |
| 29 | BudgetAmount | money | No |
| 30 | UseAllocations | tinyint | No |
| 31 | AllocationAmount | money | No |
| 32 | HistoryCount | int | No |
| 33 | StatusDesc | varchar(104) | No |
| 34 | AddendaTotal | money | Yes |
| 35 | LastAlteredSessionId | int | Yes |

#### vw_ApproveRequisitionsBySession {view-dbo-vw-approverequisitionsbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-03 12:32:35.270000 |
| **Modified** | 2025-05-19 12:27:19.020000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | Yes |
| 3 | StatusID | int | No |
| 4 | StatusName | varchar(50) | No |
| 5 | TotalRequisitionCost | money | No |
| 6 | ApprovalLevel | tinyint | No |
| 7 | Attention | varchar(50) | Yes |
| 8 | CometId | varchar(5) | Yes |
| 9 | DateUpdated | datetime | Yes |
| 10 | NotesCount | int | No |
| 11 | OrderType | tinyint | No |
| 12 | OrderTypeDisplay | varchar(10) | No |
| 13 | UserDisplayName | varchar(56) | Yes |
| 14 | CategoryID | int | No |
| 15 | CategoryName | varchar(50) | Yes |
| 16 | BudgetID | int | No |
| 17 | AccountID | int | No |
| 18 | AccountCode | varchar(62) | No |
| 19 | DistrictID | int | No |
| 20 | DistrictName | varchar(50) | No |
| 21 | SchoolID | int | No |
| 22 | SchoolName | varchar(103) | Yes |
| 23 | UserID | int | No |
| 24 | UserAccountId | int | No |
| 25 | SessionId | int | No |
| 26 | AllocationAvailable | money | Yes |
| 27 | REQ_UAID | int | Yes |
| 28 | UseBudgetAccountAllocations | tinyint | No |
| 29 | BudgetAmount | money | No |
| 30 | UseAllocations | tinyint | No |
| 31 | AllocationAmount | money | No |
| 32 | HistoryCount | int | No |
| 33 | StatusDesc | varchar(104) | No |
| 34 | AddendaTotal | money | No |
| 35 | LastAlteredSessionId | int | Yes |
| 36 | LowPOCount | int | Yes |
| 37 | DistrictPOMinimum | money | No |
| 38 | InactiveAccount | int | No |
| 39 | AdditionalShipping | int | Yes |
| 40 | AdditionalShippingCost | decimal(38,2) | Yes |

#### vw_ApproveRequisitionsBySession_Test {view-dbo-vw-approverequisitionsbysession-test}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-04-13 15:04:19.640000 |
| **Modified** | 2022-04-13 15:04:19.640000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | Yes |
| 3 | StatusID | int | No |
| 4 | StatusName | varchar(50) | No |
| 5 | TotalRequisitionCost | money | No |
| 6 | ApprovalLevel | tinyint | No |
| 7 | Attention | varchar(50) | Yes |
| 8 | CometId | varchar(5) | Yes |
| 9 | DateUpdated | datetime | Yes |
| 10 | NotesCount | int | No |
| 11 | OrderType | tinyint | No |
| 12 | OrderTypeDisplay | varchar(10) | No |
| 13 | UserDisplayName | varchar(56) | Yes |
| 14 | CategoryID | int | No |
| 15 | CategoryName | varchar(50) | Yes |
| 16 | BudgetID | int | No |
| 17 | AccountID | int | No |
| 18 | AccountCode | varchar(62) | No |
| 19 | DistrictID | int | No |
| 20 | DistrictName | varchar(50) | No |
| 21 | SchoolID | int | No |
| 22 | SchoolName | varchar(103) | Yes |
| 23 | UserID | int | No |
| 24 | UserAccountId | int | No |
| 25 | SessionId | int | No |
| 26 | AllocationAvailable | money | Yes |
| 27 | REQ_UAID | int | Yes |
| 28 | UseBudgetAccountAllocations | tinyint | No |
| 29 | BudgetAmount | money | No |
| 30 | UseAllocations | tinyint | No |
| 31 | AllocationAmount | money | No |
| 32 | HistoryCount | int | No |
| 33 | StatusDesc | varchar(104) | No |
| 34 | AddendaTotal | money | No |
| 35 | LastAlteredSessionId | int | Yes |
| 36 | LowPOCount | int | Yes |
| 37 | DistrictPOMinimum | money | No |
| 38 | InactiveAccount | int | No |
| 39 | AdditionalShipping | int | Yes |
| 40 | AdditionalShippingCost | decimal(38,2) | Yes |

#### vw_ApproveRequisitionsTest {view-dbo-vw-approverequisitionstest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-03 10:38:38.713000 |
| **Modified** | 2018-01-21 20:26:47.057000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | Yes |
| 3 | StatusID | int | No |
| 4 | StatusName | varchar(50) | No |
| 5 | TotalRequisitionCost | money | No |
| 6 | ApprovalLevel | tinyint | No |
| 7 | Attention | varchar(50) | Yes |
| 8 | CometId | varchar(5) | Yes |
| 9 | DateUpdated | datetime | Yes |
| 10 | NotesCount | int | No |
| 11 | OrderType | tinyint | No |
| 12 | OrderTypeDisplay | varchar(10) | No |
| 13 | UserDisplayName | varchar(56) | Yes |
| 14 | CategoryID | int | No |
| 15 | CategoryName | varchar(50) | Yes |
| 16 | BudgetID | int | No |
| 17 | AccountID | int | No |
| 18 | AccountCode | varchar(50) | No |
| 19 | DistrictID | int | No |
| 20 | DistrictName | varchar(50) | No |
| 21 | SchoolID | int | No |
| 22 | SchoolName | varchar(50) | Yes |
| 23 | UserID | int | No |
| 24 | UserAccountId | int | No |
| 25 | SessionId | int | No |
| 26 | AllocationAvailable | money | Yes |
| 27 | REQ_UAID | int | Yes |
| 28 | UseBudgetAccountAllocations | tinyint | No |
| 29 | BudgetAmount | money | No |
| 30 | UseAllocations | tinyint | No |
| 31 | AllocationAmount | money | No |
| 32 | HistoryCount | int | No |
| 33 | StatusDesc | varchar(104) | No |
| 34 | AddendaTotal | money | Yes |
| 35 | LastAlteredSessionId | int | Yes |

#### vw_AtAGlance {view-dbo-vw-ataglance}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-25 11:26:15.163000 |
| **Modified** | 2019-06-27 13:17:44.167000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CSRepId | int | No |
| 2 | CSRepName | varchar(30) | No |
| 3 | DistrictId | int | No |
| 4 | DistrictName | varchar(50) | No |
| 5 | BudgetId | int | No |
| 6 | BudgetName | varchar(30) | No |
| 7 | Schedule | varchar(50) | No |
| 8 | ReqCount | int | No |
| 9 | ProcessedReqCount | int | No |
| 10 | ReqPOCount | int | No |
| 11 | DownloadedCount | int | No |
| 12 | ManualPOCount | int | No |
| 13 | POCount | int | No |
| 14 | ReadyToBidCount | int | No |
| 15 | OutToBidCount | int | No |
| 16 | NeedingToBeBidCount | int | No |
| 17 | BAApprovals | int | No |
| 18 | ReqsOverBudget | int | No |
| 19 | ExcessiveReqs | int | No |

#### vw_AvailableReqBids {view-dbo-vw-availablereqbids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-06 14:30:01.853000 |
| **Modified** | 2018-01-21 20:26:47.697000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | HeaderText | varchar(305) | Yes |

#### vw_AvailableUserAccounts {view-dbo-vw-availableuseraccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-08-24 10:19:29.640000 |
| **Modified** | 2018-01-21 20:26:47.700000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | BudgetId | int | No |
| 3 | BudgetAccountId | int | No |
| 4 | UseAllocations | tinyint | Yes |
| 5 | BudgetAmount | money | Yes |
| 6 | AmountAvailable | money | Yes |
| 7 | AccountId | int | No |
| 8 | Code | varchar(50) | Yes |

#### vw_AwardedBidResults {view-dbo-vw-awardedbidresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-11-07 16:05:19.030000 |
| **Modified** | 2024-08-28 16:22:02.240000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Item Code | varchar(50) | Yes |
| 2 | Vendor Item Code | varchar(50) | No |
| 3 | Bid Price | decimal(33,13) | Yes |
| 4 | Qty | int | Yes |
| 5 | Description | varchar(1156) | Yes |
| 6 | UOM | varchar(20) | No |
| 7 | Items Per Unit | varchar(50) | No |
| 8 | Item Bid Type | varchar(32) | No |
| 9 | Alternate | varchar(512) | No |
| 10 | Manufacturer | varchar(50) | No |
| 11 | Manufacturer Part Number | varchar(50) | No |
| 12 | UPC / EAN / ISBN | varchar(20) | No |
| 13 | SDS URL | varchar(300) | No |
| 14 | Image URL | varchar(300) | No |
| 15 | Awarded Vendor Name | varchar(50) | No |
| 16 | Vendor Code | varchar(16) | No |
| 17 | UniqueId Do Not Modify | int | No |
| 18 | BidHeaderId | int | Yes |
| 19 | VendorId | int | Yes |
| 20 | SortSeq | varchar(64) | No |
| 21 | UNSPSC | varchar(50) | No |
| 22 | UniqueItemNumber | varchar(50) | No |
| 23 | PerishableItem | bit | No |
| 24 | PrescriptionRequired | bit | No |
| 25 | DigitallyDelivered | tinyint | No |
| 26 | MinimumOrderQuantity | int | No |

#### vw_AwardedVendorsAllCurrentAndFutureBids {view-dbo-vw-awardedvendorsallcurrentandfuturebids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-10-31 14:47:05.873000 |
| **Modified** | 2023-01-09 13:38:16.640000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | BidImportId | int | No |
| 3 | VendorName | varchar(50) | No |
| 4 | ContactInfo | varchar(548) | Yes |
| 5 | CategoryId | int | No |
| 6 | CategoryName | varchar(308) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | VendorBidNumber | varchar(50) | No |
| 9 | AdditionalHandlingAmount | money | No |
| 10 | FreeHandlingAmount | money | No |
| 11 | BidComments | varchar(512) | No |
| 12 | EMail | varchar(255) | No |
| 13 | VendorCode | varchar(16) | No |
| 14 | EffectiveFrom | datetime | Yes |
| 15 | EffectiveUntil | datetime | Yes |
| 16 | BidStateId | int | Yes |
| 17 | PricePlanId | int | Yes |
| 18 | CategoryType | int | Yes |

#### vw_AwardedVendorsAllCurrentBids {view-dbo-vw-awardedvendorsallcurrentbids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2021-09-21 10:36:16.147000 |
| **Modified** | 2023-01-09 13:32:53.213000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | BidImportId | int | No |
| 3 | VendorName | varchar(50) | No |
| 4 | ContactInfo | varchar(548) | Yes |
| 5 | CategoryId | int | No |
| 6 | CategoryName | varchar(308) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | VendorBidNumber | varchar(50) | No |
| 9 | AdditionalHandlingAmount | money | No |
| 10 | FreeHandlingAmount | money | No |
| 11 | BidComments | varchar(512) | No |
| 12 | EMail | varchar(255) | No |
| 13 | VendorCode | varchar(16) | No |
| 14 | EffectiveFrom | datetime | Yes |
| 15 | EffectiveUntil | datetime | Yes |
| 16 | BidStateId | int | Yes |
| 17 | PricePlanId | int | Yes |
| 18 | CategoryType | int | Yes |

#### vw_BAPCBG {view-dbo-vw-bapcbg}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-08-30 13:10:57.127000 |
| **Modified** | 2018-01-21 20:26:47.720000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RepName | varchar(30) | Yes |
| 2 | RepEmail | varchar(128) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | FullName | varchar(195) | Yes |
| 5 | Email | varchar(255) | No |
| 6 | FullAddress | varchar(170) | Yes |

#### vw_BidAnalysisDetail {view-dbo-vw-bidanalysisdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-01 10:39:12.877000 |
| **Modified** | 2018-04-02 10:45:52.140000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | PricePlanName | varchar(278) | No |
| 3 | BidHeaderId | int | Yes |
| 4 | BidRequestItemId | int | No |
| 5 | DistrictId | int | Yes |
| 6 | DistrictName | varchar(50) | No |
| 7 | ItemCode | varchar(50) | Yes |
| 8 | Description | varchar(1024) | Yes |
| 9 | UnitCode | varchar(20) | Yes |
| 10 | VendorName | varchar(50) | No |
| 11 | VendorCode | varchar(16) | No |
| 12 | BidUnits | varchar(16) | Yes |
| 13 | BidRequest | int | Yes |
| 14 | BidType | varchar(13) | Yes |
| 15 | QuantityBid | int | Yes |
| 16 | UnitPrice | decimal(34,13) | Yes |
| 17 | ExtendedCost | decimal(38,6) | Yes |
| 18 | Alternate | varchar(MAX) | Yes |
| 19 | VendorItemCode | varchar(50) | No |
| 20 | BidRequestStatus | varchar(50) | No |
| 21 | Status | varchar(51) | No |
| 22 | ResultsStatus | int | No |
| 23 | BidResultsId | int | Yes |
| 24 | Comments | varchar(1024) | No |
| 25 | ItemComments | varchar(1024) | No |
| 26 | PriceVarianceLevel | decimal(9,5) | Yes |
| 27 | FirstPrice | decimal(34,13) | Yes |
| 28 | FirstPriceBidResultsId | int | Yes |
| 29 | SecondPrice | decimal(34,13) | Yes |
| 30 | SecondPriceBidResultsId | int | Yes |
| 31 | Compliant1st | int | Yes |
| 32 | SortKey | varchar(124) | Yes |
| 33 | Variance | decimal(38,6) | Yes |
| 34 | ItemStatus | varchar(MAX) | Yes |
| 35 | PageNo | int | Yes |
| 36 | BidResultsItemsPerUnit | varchar(50) | Yes |
| 37 | ItemsItemsPerUnit | varchar(50) | Yes |

#### vw_BidAnalysisVendorSummary {view-dbo-vw-bidanalysisvendorsummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-08-19 16:27:33.133000 |
| **Modified** | 2023-10-03 12:20:53.780000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | ItemsBid | int | Yes |
| 4 | AmountBid | money | Yes |
| 5 | VendorsCode | varchar(16) | Yes |
| 6 | VendorsName | varchar(50) | Yes |
| 7 | CalculatedAmount | money | Yes |
| 8 | ItemsWon | int | Yes |
| 9 | POCount | int | No |
| 10 | POTotal | money | No |
| 11 | AvgPO | money | No |

#### vw_BidAnalysisVendorSummaryByDistrict {view-dbo-vw-bidanalysisvendorsummarybydistrict}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-08-20 13:44:35.830000 |
| **Modified** | 2018-01-21 20:26:46.880000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | ItemsBid | int | Yes |
| 4 | AmountBid | money | Yes |
| 5 | VendorsCode | varchar(16) | Yes |
| 6 | VendorsName | varchar(50) | Yes |
| 7 | CalculatedAmount | money | Yes |
| 8 | ItemsWon | int | No |
| 9 | POCount | int | No |
| 10 | POTotal | money | No |
| 11 | AvgPO | money | No |
| 12 | DistrictId | int | Yes |

#### vw_BidAnalysisVendorSummaryTest {view-dbo-vw-bidanalysisvendorsummarytest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-11-26 12:29:33.543000 |
| **Modified** | 2022-12-16 11:52:01.983000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | ItemsBid | int | Yes |
| 4 | AmountBid | money | Yes |
| 5 | VendorsCode | varchar(16) | Yes |
| 6 | VendorsName | varchar(50) | Yes |
| 7 | CalculatedAmount | money | Yes |
| 8 | ItemsWon | int | Yes |
| 9 | POCount | int | No |
| 10 | POTotal | money | No |
| 11 | AvgPO | money | No |

#### vw_BidAncillaryBySession {view-dbo-vw-bidancillarybysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-21 19:06:41.283000 |
| **Modified** | 2018-01-21 20:26:47.723000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryName | varchar(1077) | Yes |
| 3 | BidDate | datetime | Yes |
| 4 | BidAwardDate | datetime | Yes |
| 5 | EffectiveFrom | datetime | Yes |
| 6 | EffectiveUntil | datetime | Yes |
| 7 | BidHeaderId | int | Yes |

#### vw_BidAnswers {view-dbo-vw-bidanswers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-01 13:37:28.093000 |
| **Modified** | 2018-01-21 20:26:46.127000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidAnswerId | int | No |
| 2 | BidImportId | int | No |
| 3 | BidQuestionId | int | No |
| 4 | CountyId | int | No |
| 5 | BidTradeId | int | No |
| 6 | VendorBidTMAnswerId | int | Yes |
| 7 | BidAnswerJournalId | int | Yes |
| 8 | SessionId | int | Yes |
| 9 | DateModified | datetime | Yes |
| 10 | Sequence | int | Yes |
| 11 | BidAnswer | varchar(512) | Yes |
| 12 | BidAnswerExtended | varchar(512) | Yes |
| 13 | VendorBidTMAnswerJournalId | int | Yes |
| 14 | BidEntryDisplayLabel | varchar(255) | Yes |
| 15 | QuestionText | varchar(MAX) | No |
| 16 | QuestionQty | int | Yes |
| 17 | AnswerTypeId | int | Yes |
| 18 | AnswerTypeMask | varchar(50) | Yes |
| 19 | ExtdCalcMask | varchar(50) | Yes |
| 20 | UOM | varchar(50) | No |
| 21 | BidSection | varchar(255) | Yes |
| 22 | Weight | decimal(9,5) | Yes |
| 23 | ExtdCalcTypeId | int | Yes |

#### vw_BidComplianceBySession {view-dbo-vw-bidcompliancebysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-27 11:11:40.920000 |
| **Modified** | 2026-03-20 15:23:59.457000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | Description | varchar(255) | Yes |
| 3 | TradeTitle | varchar(255) | No |
| 4 | PackageNumber | int | Yes |
| 5 | BidTradeCountyId | int | No |
| 6 | BidDate | datetime | Yes |
| 7 | BidAwardDate | datetime | Yes |
| 8 | EffectiveFrom | datetime | Yes |
| 9 | EffectiveUntil | datetime | Yes |
| 10 | BidHeaderId | int | Yes |
| 11 | CategoryName | varchar(50) | Yes |
| 12 | pwRequired | int | Yes |

#### vw_BidContactsVendorList {view-dbo-vw-bidcontactsvendorlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-01 11:51:50.933000 |
| **Modified** | 2018-01-21 20:26:47.737000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | No |
| 3 | VendorCode | varchar(16) | Yes |
| 4 | VendorName | varchar(50) | No |
| 5 | FullName | varchar(143) | Yes |
| 6 | ContactFullAddress | varchar(170) | Yes |
| 7 | ContactAddress1 | varchar(50) | No |
| 8 | ContactAddress2 | varchar(50) | No |
| 9 | ContactCity | varchar(50) | No |
| 10 | ContactState | char(2) | No |
| 11 | ContactZipcode | varchar(10) | No |
| 12 | CategoryName | varchar(50) | Yes |
| 13 | Description | varchar(278) | No |
| 14 | DistrictName | varchar(57) | No |

#### vw_BidDescriptions {view-dbo-vw-biddescriptions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-01-05 10:13:44.220000 |
| **Modified** | 2019-10-07 12:13:25.573000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemId | int | Yes |
| 3 | BidRequestItemId | int | No |
| 4 | ItemDescription | varchar(1024) | Yes |
| 5 | ExtraDescription | varchar(1024) | No |

#### vw_BidDocumentTypeNames {view-dbo-vw-biddocumenttypenames}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-18 15:36:23.193000 |
| **Modified** | 2018-01-21 20:26:47.743000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DocumentName | varchar(50) | No |
| 2 | MinBidDocumentTypeId | int | Yes |

#### vw_BidDocumentsList {view-dbo-vw-biddocumentslist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-12-28 11:08:24.020000 |
| **Modified** | 2018-01-21 20:26:47.740000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(50) | No |

#### vw_BidDuplicateIdentifiers {view-dbo-vw-bidduplicateidentifiers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-08-21 17:15:56.767000 |
| **Modified** | 2018-01-21 20:26:47.750000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | Yes |
| 2 | ItemId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | VendorItemCode | varchar(50) | Yes |
| 5 | ManufacturerBid | varchar(50) | Yes |
| 6 | ManufPartNoBid | varchar(50) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | PageNo | int | Yes |
| 9 | BidResultsId | int | No |

#### vw_BidGrouper {view-dbo-vw-bidgrouper}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-03-06 12:12:44.640000 |
| **Modified** | 2018-01-21 20:26:46.157000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | MainBidHeaderId | int | Yes |
| 2 | AltBidHeaderId | int | Yes |
| 3 | BidType | tinyint | Yes |

#### vw_BidHeadersList {view-dbo-vw-bidheaderslist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-04 21:42:26.813000 |
| **Modified** | 2018-01-21 20:26:47.753000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | Active | tinyint | No |
| 3 | AllowTotalAward | tinyint | No |
| 4 | AlertLink | varchar(255) | No |
| 5 | AlertMsg | varchar(4096) | No |
| 6 | AwardMsg | varchar(1024) | No |
| 7 | BidAwardDate | datetime | Yes |
| 8 | BidDate | datetime | Yes |
| 9 | BidMessage | varchar(1024) | No |
| 10 | BidType | tinyint | No |
| 11 | BudgetYearOption | tinyint | No |
| 12 | CalendarId | int | No |
| 13 | CategoryId | int | No |
| 14 | DateCreated | datetime | Yes |
| 15 | Description | varchar(512) | No |
| 16 | DistrictId | int | No |
| 17 | EffectiveFrom | datetime | Yes |
| 18 | EffectiveUntil | datetime | Yes |
| 19 | HostDistrictId | int | No |
| 20 | ParentBidHeaderId | int | No |
| 21 | PricePlanId | int | No |
| 22 | ScheduledReaward | datetime | Yes |
| 23 | StateId | int | No |
| 24 | TotalAwardMinimumDiscount | decimal(9,5) | No |
| 25 | SectionName | int | No |
| 26 | MarkAsOriginal | int | No |
| 27 | PriceVarianceLevel | decimal(9,5) | No |
| 28 | CategoryName | varchar(50) | No |
| 29 | PricePlanDescription | varchar(255) | No |
| 30 | StateName | varchar(50) | No |

#### vw_BidImportMostRecentContactInfo {view-dbo-vw-bidimportmostrecentcontactinfo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-07-21 16:59:34.187000 |
| **Modified** | 2018-01-21 20:26:47.760000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidImportId | int | No |
| 2 | UseVendorContactInfo | tinyint | Yes |
| 3 | VendorId | int | Yes |
| 4 | CategoryId | int | Yes |
| 5 | ContactEmail | varchar(255) | Yes |
| 6 | ContactName | varchar(50) | Yes |
| 7 | ContactPhone | varchar(20) | Yes |
| 8 | ContactFax | varchar(20) | Yes |

#### vw_BidItemDescription {view-dbo-vw-biditemdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-23 12:50:10.777000 |
| **Modified** | 2026-01-22 17:14:00.230000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemDescription | nvarchar(4000) | Yes |

#### vw_BidItemLongDescription {view-dbo-vw-biditemlongdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2020-12-23 19:11:01.880000 |
| **Modified** | 2021-01-24 21:56:47.747000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemDescription | varchar(6035) | Yes |

#### vw_BidLeadComplianceBySession {view-dbo-vw-bidleadcompliancebysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-09-15 12:15:10.227000 |
| **Modified** | 2026-03-20 15:25:25.937000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | Description | varchar(255) | Yes |
| 3 | TradeTitle | varchar(255) | No |
| 4 | PackageNumber | int | Yes |
| 5 | BidTradeCountyId | int | No |
| 6 | BidDate | datetime | Yes |
| 7 | BidAwardDate | datetime | Yes |
| 8 | EffectiveFrom | datetime | Yes |
| 9 | EffectiveUntil | datetime | Yes |
| 10 | BidHeaderId | int | Yes |
| 11 | CategoryName | varchar(50) | Yes |
| 12 | pwRequired | int | Yes |

#### vw_BidLines {view-dbo-vw-bidlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-22 17:56:34.327000 |
| **Modified** | 2018-01-21 20:26:47.770000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | VendorId | int | Yes |
| 4 | ItemCode | varchar(50) | Yes |
| 5 | Description | varchar(512) | Yes |
| 6 | Title | varchar(255) | Yes |
| 7 | Keyword | varchar(50) | Yes |
| 8 | UnitPrice | decimal(11,2) | Yes |
| 9 | UOM | varchar(20) | Yes |
| 10 | VendorItemCode | varchar(50) | Yes |
| 11 | Alternate | varchar(512) | Yes |
| 12 | HeadingId | int | No |
| 13 | KeywordId | int | No |

#### vw_BidMSRPManufacturerProductLinePrices {view-dbo-vw-bidmsrpmanufacturerproductlineprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-05 14:23:27.553000 |
| **Modified** | 2018-01-21 20:26:47.780000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsId | int | No |
| 2 | BidMSRPResultsProductLineId | int | Yes |
| 3 | ManufacturerProductLineId | int | Yes |
| 4 | MSRPOptionId | int | Yes |
| 5 | OptionName | varchar(50) | No |
| 6 | TotalAwardDiscount | decimal(9,5) | Yes |
| 7 | TotalAward | tinyint | Yes |
| 8 | WeightedDiscount | decimal(9,5) | Yes |

#### vw_BidMSRPRankedManufacturerProductLines {view-dbo-vw-bidmsrprankedmanufacturerproductlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-30 15:06:12.143000 |
| **Modified** | 2018-01-21 20:26:46.003000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerProductLineId | int | No |
| 5 | ProductLineName | varchar(100) | No |
| 6 | MSRPOptionId | int | No |
| 7 | OptionName | varchar(50) | No |

#### vw_BidMSRPRankedManufacturerProductLinesOrdered {view-dbo-vw-bidmsrprankedmanufacturerproductlinesordered}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-05 15:12:03.620000 |
| **Modified** | 2018-01-21 20:26:46.027000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerProductLineId | int | No |
| 5 | ProductLineName | varchar(100) | No |
| 6 | MSRPOptionId | int | No |
| 7 | OptionName | varchar(50) | No |
| 8 | BidMSRPResultsId | int | Yes |
| 9 | BidMSRPResultsProductLineId | int | Yes |
| 10 | WriteInManufacturer | varchar(100) | Yes |
| 11 | WriteInFlag | tinyint | Yes |
| 12 | WinningBidOverride | tinyint | Yes |
| 13 | DiscountRate | decimal(38,6) | Yes |
| 14 | PriceListTypeId | int | Yes |
| 15 | TotalAward | tinyint | Yes |
| 16 | TotalAwardDiscount | decimal(9,5) | Yes |
| 17 | ProductLineWeight | decimal(9,5) | Yes |
| 18 | TotalAwardManufacturerWeight | decimal(38,6) | Yes |
| 19 | TotalAwardProductLineWeight | decimal(38,6) | Yes |
| 20 | SortKey | varchar(15) | Yes |
| 21 | PriceListType | varchar(50) | Yes |
| 22 | VendorId | int | Yes |
| 23 | VendorName | varchar(50) | Yes |
| 24 | PriceListWarning | varchar(28) | No |
| 25 | AllFlag | int | No |
| 26 | AllActive | int | No |
| 27 | EntryFiltered | int | No |

#### vw_BidMSRPRankedManufacturerProductLinesOrderedNew {view-dbo-vw-bidmsrprankedmanufacturerproductlinesorderednew}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-11-18 17:48:52.647000 |
| **Modified** | 2018-01-21 20:26:46.930000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerProductLineId | int | No |
| 5 | ProductLineName | varchar(100) | No |
| 6 | MSRPOptionId | int | No |
| 7 | OptionName | varchar(50) | No |
| 8 | BidMSRPResultsId | int | Yes |
| 9 | BidMSRPResultsProductLineId | int | Yes |
| 10 | WriteInManufacturer | varchar(100) | Yes |
| 11 | WriteInFlag | tinyint | Yes |
| 12 | WinningBidOverride | tinyint | Yes |
| 13 | DiscountRate | decimal(38,6) | Yes |
| 14 | PriceListTypeId | int | Yes |
| 15 | TotalAward | tinyint | Yes |
| 16 | TotalAwardDiscount | decimal(9,5) | Yes |
| 17 | ProductLineWeight | decimal(9,5) | Yes |
| 18 | TotalAwardManufacturerWeight | decimal(38,6) | Yes |
| 19 | TotalAwardProductLineWeight | decimal(38,6) | Yes |
| 20 | SortKey | varchar(20) | Yes |
| 21 | PriceListType | varchar(50) | Yes |
| 22 | VendorId | int | Yes |
| 23 | VendorName | varchar(50) | Yes |
| 24 | PriceListWarning | varchar(28) | No |
| 25 | AllFlag | int | No |
| 26 | AllActive | int | No |
| 27 | EntryFiltered | int | No |
| 28 | ManufacturerAverageWeightedDiscount | decimal(38,6) | Yes |
| 29 | ProductLineAverageWeightedDiscount | decimal(38,6) | Yes |
| 30 | OptionAverageWeightedDiscount | decimal(38,6) | Yes |
| 31 | MRRSortKey | varchar(3) | Yes |
| 32 | MRTBSortKey | varchar(2) | Yes |

#### vw_BidMSRPRankedManufacturerProductLinesOrderedSaved {view-dbo-vw-bidmsrprankedmanufacturerproductlinesorderedsaved}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-30 16:25:48.123000 |
| **Modified** | 2018-01-21 20:26:46.967000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ManufacturerName | varchar(100) | No |
| 4 | ManufacturerProductLineId | int | No |
| 5 | ProductLineName | varchar(100) | No |
| 6 | MSRPOptionId | int | No |
| 7 | OptionName | varchar(50) | No |
| 8 | BidMSRPResultsId | int | Yes |
| 9 | BidMSRPResultsProductLineId | int | Yes |
| 10 | WriteInManufacturer | varchar(100) | Yes |
| 11 | WriteInFlag | tinyint | Yes |
| 12 | WinningBidOverride | tinyint | Yes |
| 13 | DiscountRate | decimal(10,5) | No |
| 14 | PriceListTypeId | int | Yes |
| 15 | TotalAward | tinyint | Yes |
| 16 | TotalAwardDiscount | decimal(9,5) | Yes |
| 17 | ProductLineWeight | decimal(9,5) | Yes |
| 18 | TotalAwardManufacturerWeight | decimal(38,6) | Yes |
| 19 | TotalAwardProductLineWeight | decimal(38,6) | Yes |
| 20 | SortKey | varchar(14) | Yes |
| 21 | PriceListType | varchar(50) | Yes |
| 22 | VendorId | int | Yes |
| 23 | VendorName | varchar(50) | Yes |
| 24 | PriceListWarning | varchar(28) | No |
| 25 | AllFlag | int | No |
| 26 | AllActive | int | No |

#### vw_BidMSRPRankedManufacturers {view-dbo-vw-bidmsrprankedmanufacturers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-30 14:39:34.010000 |
| **Modified** | 2018-01-21 20:26:47.783000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ManufacturerName | varchar(100) | No |

#### vw_BidMSRPResultsPriceRanges {view-dbo-vw-bidmsrpresultspriceranges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-11-14 21:15:02.613000 |
| **Modified** | 2018-01-21 20:26:47.787000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | No |
| 2 | BidImportId | int | No |
| 3 | BidMSRPResultsId | int | No |
| 4 | BidMSRPResultsProductLineId | int | Yes |
| 5 | ManufacturerProductLineId | int | Yes |
| 6 | MSRPOptionId | int | Yes |
| 7 | OptionName | varchar(50) | Yes |
| 8 | TotalAwardDiscount | decimal(9,5) | Yes |
| 9 | TotalAward | tinyint | Yes |
| 10 | BidMSRPResultPricesId | int | Yes |
| 11 | ManufacturerId | int | Yes |
| 12 | RangeValue | decimal(9,5) | Yes |
| 13 | RangeBase | money | Yes |
| 14 | RangeWeight | decimal(9,5) | Yes |

#### vw_BidMSRPResultsPrices {view-dbo-vw-bidmsrpresultsprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-09 21:41:32.503000 |
| **Modified** | 2018-01-21 20:26:46.013000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | No |
| 2 | BidImportId | int | No |
| 3 | BidMSRPResultsId | int | No |
| 4 | BidMSRPResultsProductLineId | int | Yes |
| 5 | ManufacturerProductLineId | int | Yes |
| 6 | ProductLineName | varchar(100) | Yes |
| 7 | MSRPOptionId | int | Yes |
| 8 | OptionName | varchar(50) | Yes |
| 9 | TotalAwardDiscount | decimal(9,5) | Yes |
| 10 | TotalAward | tinyint | Yes |
| 11 | ManufacturerId | int | Yes |
| 12 | WeightedDiscount | decimal(9,5) | Yes |
| 13 | TotalWeights | decimal(38,5) | Yes |

#### vw_BidManufacturerPartNumbers {view-dbo-vw-bidmanufacturerpartnumbers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-08-21 16:45:41.930000 |
| **Modified** | 2018-01-21 20:26:47.773000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | Yes |
| 2 | ItemId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | VendorItemCode | varchar(50) | Yes |
| 5 | ManufacturerBid | varchar(50) | Yes |
| 6 | ManufPartNoBid | varchar(50) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | PageNo | int | Yes |
| 9 | BidResultsId | int | No |

#### vw_BidMgrBidderDocs {view-dbo-vw-bidmgrbidderdocs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2020-12-08 20:48:24.280000 |
| **Modified** | 2025-10-27 20:05:45.070000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | VendorId | int | Yes |
| 4 | VendorBidNumber | varchar(50) | Yes |
| 5 | BidHeaderCheckListId | int | No |
| 6 | BidderCheckListId | int | Yes |
| 7 | DocumentUploadId | int | Yes |
| 8 | VendorCode | varchar(16) | Yes |
| 9 | VendorName | varchar(50) | Yes |
| 10 | DisplaySequence | int | Yes |
| 11 | DocumentName | varchar(50) | Yes |
| 12 | CheckListText | varchar(100) | Yes |
| 13 | UploadEligible | tinyint | No |
| 14 | UploadEligibleStr | varchar(3) | No |
| 15 | VendorUploadDateTime | datetime2 | Yes |
| 16 | DocumentNumber | varchar(255) | Yes |
| 17 | DocumentExpiration | datetime | Yes |
| 18 | DocStatus | char(1) | No |
| 19 | StatusStr | varchar(9) | No |
| 20 | DocRejectReasonComments | varchar(1024) | No |
| 21 | InDMS | int | No |
| 22 | InDmsStr | varchar(12) | No |
| 23 | DocumentTypeId | int | Yes |
| 24 | ExpirationDateReqd | tinyint | No |
| 25 | DocNumberReqd | tinyint | No |
| 26 | DocNumberLabel | varchar(50) | Yes |
| 27 | OptionalDocument | tinyint | Yes |
| 28 | DMSCountOfDocType | int | Yes |
| 29 | BidDocsCountOfDocType | int | Yes |

#### vw_BidPricing {view-dbo-vw-bidpricing}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-24 14:32:20.260000 |
| **Modified** | 2018-01-21 20:26:47.103000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemId | int | No |
| 3 | ItemCode | varchar(50) | Yes |
| 4 | ItemDescription | varchar(1156) | Yes |
| 5 | UOM | varchar(20) | Yes |
| 6 | VendorItemCode | varchar(50) | No |
| 7 | ItemBidType | varchar(32) | No |
| 8 | Alternate | varchar(512) | No |
| 9 | PageNo | int | No |
| 10 | NetPrice | decimal(33,13) | No |
| 11 | SortSeq | varchar(64) | Yes |
| 12 | VendorName | varchar(50) | Yes |

#### vw_BidProductLinePrices {view-dbo-vw-bidproductlineprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-05-07 11:45:08.427000 |
| **Modified** | 2018-01-21 20:26:46.390000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidProductLineId | int | No |
| 2 | RangeBase | money | Yes |
| 3 | RangeTop | numeric(20,4) | Yes |
| 4 | DiscountRate | decimal(9,5) | Yes |

#### vw_BidProjectAveragePO {view-dbo-vw-bidprojectaveragepo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2007-08-17 14:54:13.810000 |
| **Modified** | 2018-01-21 20:26:47.797000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | No |
| 3 | VendorCode | varchar(16) | Yes |
| 4 | VendorName | varchar(50) | Yes |
| 5 | VendorInfo | varchar(376) | Yes |
| 6 | Items | int | No |
| 7 | Total | money | No |
| 8 | POCount | int | No |
| 9 | TotalQuantity | int | No |
| 10 | AvgPO | money | No |

#### vw_BidRequestItemMergeDetail {view-dbo-vw-bidrequestitemmergedetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-08-05 15:26:34.347000 |
| **Modified** | 2018-01-21 20:26:47.807000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemCode | varchar(50) | Yes |
| 3 | ItemDesc | varchar(512) | Yes |
| 4 | BidRequestItemId | int | No |
| 5 | ItemId | int | Yes |
| 6 | BidRequest | int | Yes |
| 7 | Active | tinyint | Yes |
| 8 | RequisitionCount | int | Yes |
| 9 | BidRequestAmount | money | Yes |
| 10 | Checksum | int | Yes |
| 11 | UnitCode | varchar(20) | Yes |
| 12 | SortSeq | varchar(64) | Yes |
| 13 | DistrictName | varchar(50) | Yes |
| 14 | Heading | varchar(308) | Yes |

#### vw_BidRequestItemMergeHeader {view-dbo-vw-bidrequestitemmergeheader}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-08-07 13:44:05.750000 |
| **Modified** | 2019-08-27 06:57:01.940000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemCode | varchar(50) | Yes |
| 3 | ItemDesc | varchar(512) | Yes |
| 4 | BidRequestItemId | int | No |
| 5 | ItemId | int | Yes |
| 6 | BidRequest | int | Yes |
| 7 | Active | tinyint | Yes |
| 8 | RequisitionCount | int | Yes |
| 9 | BidRequestAmount | money | Yes |
| 10 | Checksum | int | Yes |
| 11 | ExcludeFlag | int | No |
| 12 | MergedFlag | int | No |
| 13 | MasterItemFlag | int | No |
| 14 | MasterItemCode | varchar(50) | No |
| 15 | UnitCode | varchar(20) | Yes |

#### vw_BidRequestItemsBidMgr {view-dbo-vw-bidrequestitemsbidmgr}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-08-30 13:10:04.910000 |
| **Modified** | 2018-01-21 20:26:47.817000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemId | int | Yes |
| 4 | BidRequest | int | Yes |
| 5 | Active | tinyint | Yes |
| 6 | RequisitionCount | int | Yes |
| 7 | Status | varchar(50) | No |
| 8 | Comments | varchar(1024) | No |
| 9 | CrossReferencesText | varchar(1024) | No |
| 10 | ItemCode | varchar(50) | Yes |
| 11 | SortSeq | varchar(64) | Yes |
| 12 | Description | varchar(512) | Yes |
| 13 | UnitId | int | No |
| 14 | Code | varchar(20) | Yes |
| 15 | BIDMGRTAGFILEID | int | No |
| 16 | TAGUSR | int | Yes |
| 17 | TAGTBL | int | Yes |
| 18 | TAGPTR | int | Yes |
| 19 | TAGVAL | char(10) | Yes |
| 20 | WEIGHT | real | Yes |

#### vw_BidResults {view-dbo-vw-bidresults}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-04-01 22:24:22.633000 |
| **Modified** | 2018-01-21 20:26:46.993000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidId | int | No |
| 3 | ItemId | int | Yes |
| 4 | UnitPrice | money | Yes |
| 5 | Alternate | varchar(512) | Yes |
| 6 | QuantityBid | int | Yes |
| 7 | BidRequest | int | Yes |
| 8 | AwardId | int | No |
| 9 | VendorItemCode | varchar(50) | Yes |
| 10 | CrossRefId | int | Yes |
| 11 | ItemBidType | varchar(13) | No |
| 12 | PackedItemCode | varchar(50) | Yes |
| 13 | PackedVendorItemCode | varchar(50) | Yes |
| 14 | PageNo | int | Yes |
| 15 | ContractNumber | varchar(50) | Yes |
| 16 | DateModified | datetime | No |
| 17 | BidResultsId | int | Yes |
| 18 | VendorId | int | Yes |

#### vw_BidTabReadyNotifications {view-dbo-vw-bidtabreadynotifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-08-16 23:40:15.420000 |
| **Modified** | 2017-02-22 16:28:34.447000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictNotificationId | int | Yes |
| 2 | DistrictId | int | No |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | CategoryId | int | No |
| 5 | CategoryName | varchar(50) | Yes |
| 6 | NotifyUser | int | Yes |
| 7 | NotifyApprover | int | Yes |
| 8 | NotifyBA | int | Yes |
| 9 | NotifyPrimary | int | Yes |
| 10 | NotifyAD | int | Yes |
| 11 | NotifyBG | int | Yes |
| 12 | OtherNotify | varchar(4096) | Yes |

#### vw_BidTrades {view-dbo-vw-bidtrades}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-05 12:51:40.580000 |
| **Modified** | 2018-01-21 20:26:47.827000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | StateCode | char(2) | Yes |
| 2 | StateName | varchar(50) | Yes |
| 3 | CountyName | varchar(50) | No |
| 4 | TradeName | varchar(255) | Yes |
| 5 | BidTradeCountyId | int | No |
| 6 | BidDate | datetime | Yes |
| 7 | BidAwardDate | datetime | Yes |
| 8 | EffectiveFrom | datetime | Yes |
| 9 | EffectiveUntil | datetime | Yes |
| 10 | BidHeaderId | int | Yes |

#### vw_BidTradesBySession {view-dbo-vw-bidtradesbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-01 15:14:00.163000 |
| **Modified** | 2026-03-20 11:48:08.480000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | Description | varchar(255) | Yes |
| 3 | TradeTitle | varchar(255) | No |
| 4 | PackageNumber | int | No |
| 5 | BidTradeCountyId | int | No |
| 6 | BidDate | datetime | Yes |
| 7 | BidAwardDate | datetime | Yes |
| 8 | EffectiveFrom | datetime | Yes |
| 9 | EffectiveUntil | datetime | Yes |
| 10 | BidHeaderId | int | Yes |
| 11 | pwRequired | int | Yes |

#### vw_BidTradesBySession_Test {view-dbo-vw-bidtradesbysession-test}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-05-17 12:27:55.450000 |
| **Modified** | 2024-12-17 10:35:12.680000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | Description | varchar(255) | Yes |
| 3 | TradeTitle | varchar(255) | No |
| 4 | PackageNumber | int | No |
| 5 | BidTradeCountyId | int | No |
| 6 | BidDate | datetime | Yes |
| 7 | BidAwardDate | datetime | Yes |
| 8 | EffectiveFrom | datetime | Yes |
| 9 | EffectiveUntil | datetime | Yes |
| 10 | BidHeaderId | int | Yes |

#### vw_BidTradesVendorDetailForReports {view-dbo-vw-bidtradesvendordetailforreports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-05 21:25:51.227000 |
| **Modified** | 2018-01-21 20:26:46.230000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidTradeCountyId | int | No |
| 2 | BidImportId | int | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | BidCounty | varchar(50) | No |
| 5 | BidState | varchar(50) | Yes |
| 6 | TradeName | varchar(255) | No |
| 7 | AwardType | varchar(50) | Yes |
| 8 | BidDate | datetime | Yes |
| 9 | BidAwardDate | datetime | Yes |
| 10 | VendorCode | varchar(16) | No |
| 11 | VendorName | varchar(50) | No |
| 12 | ContactName | varchar(150) | No |
| 13 | ContactPhone | varchar(25) | No |
| 14 | ContactFax | varchar(20) | No |
| 15 | ContactEmail | varchar(255) | No |
| 16 | Address1 | varchar(50) | No |
| 17 | Address2 | varchar(50) | No |
| 18 | City | varchar(50) | No |
| 19 | State | char(2) | No |
| 20 | Zipcode | varchar(10) | No |
| 21 | HostName | varchar(50) | Yes |
| 22 | HostNameAndAddress | varchar(222) | Yes |
| 23 | BidEntryDisplayLabel | varchar(255) | Yes |
| 24 | BidAnswer | varchar(4096) | Yes |
| 25 | UOM | varchar(51) | No |
| 26 | Sequence | int | Yes |

#### vw_BidTradesVendors {view-dbo-vw-bidtradesvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-02 09:45:55.433000 |
| **Modified** | 2018-01-21 20:26:46.150000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidTradeCountyId | int | No |
| 2 | BidImportId | int | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | VendorId | int | No |
| 5 | BidCounty | varchar(50) | No |
| 6 | BidState | varchar(50) | Yes |
| 7 | TradeName | varchar(255) | Yes |
| 8 | VendorCode | varchar(16) | No |
| 9 | VendorName | varchar(50) | No |
| 10 | ContactName | varchar(150) | No |
| 11 | ContactPhone | varchar(25) | No |
| 12 | ContactFax | varchar(20) | No |
| 13 | ContactEmail | varchar(255) | No |
| 14 | Address1 | varchar(50) | No |
| 15 | Address2 | varchar(50) | No |
| 16 | City | varchar(50) | No |
| 17 | State | char(2) | No |
| 18 | Zipcode | varchar(10) | No |
| 19 | AwardAmount | numeric(19,4) | No |

#### vw_BidTradesVendorsAnswers {view-dbo-vw-bidtradesvendorsanswers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-02 17:02:33.493000 |
| **Modified** | 2018-01-21 20:26:46.217000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidImportId | int | No |
| 2 | BidTradeCountyId | int | No |
| 3 | Sequence | int | Yes |
| 4 | BidEntryDisplayLabel | varchar(255) | Yes |
| 5 | BidAnswer | varchar(4148) | Yes |

#### vw_BidTradesVendorsAnswersBySession {view-dbo-vw-bidtradesvendorsanswersbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-02 16:57:36.080000 |
| **Modified** | 2018-01-21 20:26:46.200000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidImportId | int | No |
| 2 | BidTradeCountyId | int | No |
| 3 | Sequence | int | Yes |
| 4 | QuestionText | varchar(MAX) | No |
| 5 | BidAnswer | varchar(512) | Yes |

#### vw_BidTradesVendorsBySession {view-dbo-vw-bidtradesvendorsbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-01 17:09:17.177000 |
| **Modified** | 2025-09-18 15:12:44.807000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | BidTradeCountyId | int | No |
| 3 | BidImportId | int | Yes |
| 4 | VendorBidComments | varchar(1024) | No |
| 5 | VendorCountyBidComments | varchar(4096) | No |
| 6 | BidHeaderId | int | Yes |
| 7 | BidCounty | varchar(50) | No |
| 8 | BidState | varchar(50) | Yes |
| 9 | AwardType | varchar(50) | Yes |
| 10 | VendorCode | varchar(16) | No |
| 11 | VendorName | varchar(50) | Yes |
| 12 | ContactName | varchar(150) | No |
| 13 | ContactPhone | varchar(25) | No |
| 14 | ContactFax | varchar(20) | No |
| 15 | ContactEmail | varchar(255) | No |
| 16 | Address1 | varchar(50) | No |
| 17 | Address2 | varchar(50) | No |
| 18 | City | varchar(50) | No |
| 19 | State | char(2) | No |
| 20 | Zipcode | varchar(10) | No |

#### vw_BidTradesVendorsForReports {view-dbo-vw-bidtradesvendorsforreports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-05 13:16:04.243000 |
| **Modified** | 2023-07-19 12:25:25.667000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidTradeCountyId | int | No |
| 2 | BidImportId | int | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | BidCounty | varchar(50) | No |
| 5 | BidState | varchar(50) | Yes |
| 6 | TradeName | varchar(255) | No |
| 7 | PackageNumber | int | Yes |
| 8 | TradeDescription | varchar(255) | Yes |
| 9 | AwardType | varchar(50) | Yes |
| 10 | BidDate | datetime | Yes |
| 11 | BidAwardDate | datetime | Yes |
| 12 | EffectiveFrom | datetime | Yes |
| 13 | EffectiveUntil | datetime | Yes |
| 14 | VendorCode | varchar(16) | No |
| 15 | VendorName | varchar(50) | No |
| 16 | ContactName | varchar(150) | No |
| 17 | ContactPhone | varchar(25) | No |
| 18 | ContactFax | varchar(20) | No |
| 19 | ContactEmail | varchar(255) | No |
| 20 | Address1 | varchar(50) | No |
| 21 | Address2 | varchar(50) | No |
| 22 | City | varchar(50) | No |
| 23 | State | char(2) | No |
| 24 | Zipcode | varchar(10) | No |
| 25 | VendorContactInfo | varchar(5824) | Yes |
| 26 | HostName | varchar(50) | Yes |
| 27 | HostNameAndAddress | varchar(222) | Yes |
| 28 | CategoryType | int | Yes |
| 29 | CategoryName | varchar(1074) | Yes |
| 30 | Grouping | varchar(50) | No |

#### vw_BidType {view-dbo-vw-bidtype}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-21 20:20:49.127000 |
| **Modified** | 2018-01-21 20:26:47.870000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | CategoryType | int | Yes |
| 3 | Grouping | varchar(50) | Yes |
| 4 | TradeCount | int | Yes |
| 5 | ItemCount | int | Yes |

#### vw_BidUPCs {view-dbo-vw-bidupcs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-08-15 15:41:18.930000 |
| **Modified** | 2019-08-20 15:00:35.193000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | Yes |
| 2 | ItemId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | VendorItemCode | varchar(50) | Yes |
| 5 | BidHeaderId | int | Yes |
| 6 | PageNo | int | Yes |
| 7 | BidResultsId | int | No |
| 8 | UPC_ISBN | varchar(20) | Yes |

#### vw_BidVendor {view-dbo-vw-bidvendor}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-17 16:39:17.100000 |
| **Modified** | 2018-01-21 20:26:47.873000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | CategoryId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | Description | varchar(512) | Yes |
| 5 | BidMessage | varchar(1024) | Yes |
| 6 | EffectiveFrom | datetime | Yes |
| 7 | EffectiveUntil | datetime | Yes |

#### vw_BidVendorItemCodes {view-dbo-vw-bidvendoritemcodes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-08-21 13:23:20.317000 |
| **Modified** | 2018-01-21 20:26:47.877000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | Yes |
| 2 | ItemId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | VendorItemCode | varchar(50) | Yes |
| 5 | ManufacturerBid | varchar(50) | Yes |
| 6 | ManufPartNoBid | varchar(50) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | PageNo | int | Yes |
| 9 | BidResultsId | int | No |

#### vw_BidVendorList {view-dbo-vw-bidvendorlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-01 11:37:28.133000 |
| **Modified** | 2021-05-28 11:32:49.657000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | Yes |
| 3 | VendorCode | varchar(16) | Yes |
| 4 | VendorName | varchar(MAX) | Yes |
| 5 | CategoryName | varchar(50) | Yes |
| 6 | CategoryId | int | No |
| 7 | Description | varchar(278) | No |
| 8 | DistrictName | varchar(57) | No |

#### vw_BidVendorsBySession {view-dbo-vw-bidvendorsbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-22 16:07:28.020000 |
| **Modified** | 2025-09-18 15:12:44.933000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | BidImportId | int | Yes |
| 3 | VendorBidComments | varchar(1541) | No |
| 4 | VendorCountyBidComments | varchar(1) | No |
| 5 | BidHeaderId | int | Yes |
| 6 | BidCounty | varchar(50) | No |
| 7 | BidState | varchar(50) | Yes |
| 8 | AwardType | varchar(15) | No |
| 9 | VendorCode | varchar(16) | No |
| 10 | VendorName | varchar(50) | Yes |
| 11 | ContactName | varchar(150) | No |
| 12 | ContactPhone | varchar(25) | No |
| 13 | ContactFax | varchar(20) | No |
| 14 | ContactEmail | varchar(255) | No |
| 15 | Address1 | varchar(50) | No |
| 16 | Address2 | varchar(50) | No |
| 17 | City | varchar(50) | No |
| 18 | State | char(2) | No |
| 19 | Zipcode | varchar(10) | No |

#### vw_BidVendorsSinceLastYear {view-dbo-vw-bidvendorssincelastyear}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-10-25 14:07:51.353000 |
| **Modified** | 2018-01-21 20:26:46.267000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | No |
| 3 | CategoryId | int | Yes |

#### vw_BidYears {view-dbo-vw-bidyears}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-09-27 13:46:36.073000 |
| **Modified** | 2025-10-27 20:06:35.867000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidYears | varchar(11) | Yes |

#### vw_BillingStatus {view-dbo-vw-billingstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-10-09 14:42:16.550000 |
| **Modified** | 2018-01-21 20:26:47.890000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | Name | varchar(50) | Yes |
| 3 | CurrentBudgetId | int | No |
| 4 | NextBudgetId | int | No |
| 5 | CurrentEDSAmount | money | Yes |
| 6 | CurrentEDSType | varchar(63) | Yes |
| 7 | NextEDSAmount | money | Yes |
| 8 | NextEDSType | varchar(50) | Yes |
| 9 | CurrentRTKAmount | money | Yes |
| 10 | CurrentRTKType | varchar(13) | No |
| 11 | NextRTKAmount | money | Yes |
| 12 | CurrentTMAmount | money | Yes |
| 13 | NextTMAmount | money | Yes |
| 14 | CurrentTMType | varchar(13) | No |
| 15 | NeedsEDS | int | No |
| 16 | NeedsRTK | int | No |
| 17 | NeedsTM | int | No |

#### vw_BrowseDistrictBidHeaders {view-dbo-vw-browsedistrictbidheaders}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 23:00:45.103000 |
| **Modified** | 2018-01-21 20:26:47.897000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | HeadingId | int | Yes |
| 3 | Title | varchar(255) | Yes |

#### vw_BudgetDistrictBySession {view-dbo-vw-budgetdistrictbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-26 21:49:03.940000 |
| **Modified** | 2018-01-21 20:26:47.900000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | DistrictName | varchar(50) | Yes |
| 3 | BudgetName | varchar(30) | Yes |
| 4 | BudgetId | int | Yes |
| 5 | StateName | varchar(50) | Yes |
| 6 | CountyName | varchar(50) | Yes |
| 7 | DistrictId | int | Yes |

#### vw_BudgetPrice {view-dbo-vw-budgetprice}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-10-07 14:29:08.450000 |
| **Modified** | 2018-01-21 20:26:47.907000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidPrice | money | Yes |
| 2 | BidItemId | int | Yes |
| 3 | CrossRefId | int | No |
| 4 | VendorId | int | Yes |
| 5 | CatalogId | int | Yes |
| 6 | CatalogPrice | money | Yes |
| 7 | GrossPrice | money | Yes |
| 8 | DiscountRate | int | Yes |
| 9 | CatalogPage | char(4) | Yes |
| 10 | PricePlanId | int | Yes |
| 11 | AwardId | int | Yes |
| 12 | VendorItemCode | varchar(50) | Yes |
| 13 | Alternate | int | Yes |
| 14 | ItemMustBeBid | int | No |
| 15 | CatalogYear | char(2) | Yes |
| 16 | ItemId | int | No |
| 17 | SortKey | varchar(42) | Yes |

#### vw_BudgetsFilter {view-dbo-vw-budgetsfilter}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-31 12:24:10.250000 |
| **Modified** | 2018-01-21 20:26:47.910000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetName | varchar(9) | Yes |
| 2 | BudgetFilterId | int | Yes |

#### vw_CSReps {view-dbo-vw-csreps}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2024-04-22 08:44:52.770000 |
| **Modified** | 2024-04-22 08:44:52.770000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(30) | Yes |

#### vw_CatalogCompare {view-dbo-vw-catalogcompare}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-31 15:20:46.853000 |
| **Modified** | 2025-10-27 20:08:56.247000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CatalogIdOld | int | Yes |
| 2 | CrossRefId | int | No |
| 3 | VendorItemCodeOld | varchar(50) | Yes |
| 4 | PageOld | char(4) | Yes |
| 5 | CatalogPriceOld | money | Yes |
| 6 | GrossPriceOld | money | Yes |
| 7 | DoNotDiscountOld | int | Yes |
| 8 | DescriptionOld | varchar(512) | Yes |
| 9 | UnitCodeOld | varchar(20) | Yes |
| 10 | NewCatalogId | int | Yes |
| 11 | sysid | int | No |
| 12 | VendorItemCodeNew | varchar(50) | Yes |
| 13 | PageNew | int | Yes |
| 14 | CatalogPriceNew | money | Yes |
| 15 | GrossPriceNew | money | Yes |
| 16 | DoNotDiscountNew | int | Yes |
| 17 | DescriptionNew | varchar(512) | Yes |
| 18 | UnitCodeNew | varchar(16) | Yes |
| 19 | CatalogPriceChangePercent | money | Yes |
| 20 | GrossPriceChangePercent | money | Yes |

#### vw_CatalogImport {view-dbo-vw-catalogimport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-05 23:06:22.610000 |
| **Modified** | 2018-01-21 20:26:47.917000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CatalogImportFieldId | int | No |
| 2 | CatalogImportId | int | No |
| 3 | SequenceId | int | Yes |
| 4 | Name | varchar(50) | No |
| 5 | Optional | tinyint | Yes |
| 6 | rowguid | uniqueidentifier | No |
| 7 | CatalogImportMapId | int | Yes |
| 8 | CatalogId | int | Yes |
| 9 | ImportIndex | int | Yes |
| 10 | ImportRegExp | varchar(1024) | Yes |

#### vw_CatalogImporter1 {view-dbo-vw-catalogimporter1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-18 17:06:27.530000 |
| **Modified** | 2018-01-21 20:26:47.923000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | VendorName | varchar(50) | Yes |
| 3 | VendorCode | varchar(16) | Yes |
| 4 | CategoryId | int | Yes |
| 5 | VendorId | int | Yes |

#### vw_CatalogImporter1Dtl {view-dbo-vw-catalogimporter1dtl}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-18 17:06:38.123000 |
| **Modified** | 2018-01-21 20:26:47.927000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | VendorName | varchar(50) | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | BidDescription | varchar(512) | Yes |
| 5 | EffectiveFrom | datetime | Yes |
| 6 | EffectiveUntil | datetime | Yes |
| 7 | CategoryId | int | Yes |
| 8 | VendorId | int | Yes |
| 9 | BidHeaderActive | tinyint | Yes |

#### vw_CatalogImporterCat {view-dbo-vw-catalogimportercat}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-18 17:36:29.390000 |
| **Modified** | 2018-01-21 20:26:47.930000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | CategoryId | int | Yes |

#### vw_CatalogImporterVen {view-dbo-vw-catalogimporterven}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-18 17:39:20.983000 |
| **Modified** | 2018-01-21 20:26:47.933000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorName | varchar(50) | Yes |
| 2 | VendorId | int | No |
| 3 | VendorCode | varchar(16) | Yes |

#### vw_CatalogImports {view-dbo-vw-catalogimports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-03-03 18:17:02.487000 |
| **Modified** | 2018-01-21 20:26:47.940000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | VendorName | varchar(50) | Yes |
| 3 | CatalogYear | char(2) | Yes |
| 4 | CatalogName | varchar(50) | Yes |
| 5 | NumberOfItems | int | Yes |
| 6 | DatePosted | varchar(30) | No |
| 7 | WebLink | varchar(30) | No |
| 8 | CatalogId | int | No |

#### vw_CatalogPages {view-dbo-vw-catalogpages}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-11 15:55:38.890000 |
| **Modified** | 2018-01-21 20:26:47.080000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | ItemId | int | Yes |
| 3 | CatalogId | int | No |
| 4 | Name | varchar(50) | Yes |
| 5 | Page | char(4) | Yes |
| 6 | PDFAvailable | tinyint | Yes |
| 7 | VendorItemCode | varchar(50) | Yes |
| 8 | VendorId | int | Yes |

#### vw_CatalogPages1 {view-dbo-vw-catalogpages1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-02-19 23:27:46.947000 |
| **Modified** | 2018-01-21 20:26:47.953000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | ItemId | int | No |
| 3 | CatalogId | int | No |
| 4 | Name | varchar(50) | Yes |
| 5 | Page | int | Yes |
| 6 | PDFAvailable | tinyint | Yes |
| 7 | VendorItemCode | varchar(50) | Yes |
| 8 | VendorId | int | Yes |

#### vw_CatalogPages_Orig {view-dbo-vw-catalogpages-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-02-19 23:29:03.490000 |
| **Modified** | 2018-01-21 20:26:47.947000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | ItemId | int | Yes |
| 3 | CatalogId | int | No |
| 4 | Name | varchar(50) | Yes |
| 5 | Page | char(4) | Yes |
| 6 | PDFAvailable | tinyint | Yes |
| 7 | VendorItemCode | varchar(50) | Yes |
| 8 | VendorId | int | Yes |

#### vw_CatalogPricing {view-dbo-vw-catalogpricing}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-24 15:48:14.017000 |
| **Modified** | 2018-01-21 20:26:45.990000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | Yes |
| 2 | CrossRefId | int | No |
| 3 | BidHeaderId | int | Yes |
| 4 | AwardCatalogId | int | No |
| 5 | AwardId | int | No |
| 6 | BidId | int | No |
| 7 | NetPrice | decimal(34,13) | Yes |

#### vw_CatalogRefsItemTest {view-dbo-vw-catalogrefsitemtest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-03-22 16:47:46.220000 |
| **Modified** | 2018-01-21 20:26:47.963000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemId | int | No |
| 3 | CatalogRefs | nvarchar(MAX) | Yes |

#### vw_CatalogRequestStatus {view-dbo-vw-catalogrequeststatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-03-24 17:09:14.597000 |
| **Modified** | 2018-01-21 20:26:47.967000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CatalogRequestId | int | No |
| 2 | VendorId | int | Yes |
| 3 | EmailAddress | varchar(255) | Yes |
| 4 | ContactName | varchar(255) | Yes |
| 5 | SendDate | datetime | Yes |
| 6 | CatalogRequestNotes | varchar(1000) | Yes |
| 7 | Status | varchar(18) | Yes |
| 8 | StatusDate | datetime | Yes |
| 9 | FollowUpDate | datetime | Yes |
| 10 | CatalogRequestStatusId | int | Yes |
| 11 | VendorName | varchar(50) | Yes |

#### vw_CatalogsAttachedToBids {view-dbo-vw-catalogsattachedtobids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-03-07 16:01:02.463000 |
| **Modified** | 2024-01-26 16:02:05.650000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | BidNumber | int | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | CatalogName | varchar(50) | Yes |
| 5 | CrossRefCount | int | Yes |
| 6 | DatePosted | varchar(30) | No |
| 7 | LastAwardDate | varchar(30) | No |
| 8 | AwardWarning | varchar(58) | Yes |
| 9 | CatalogId | int | No |
| 10 | DiscountRate | decimal(9,5) | Yes |
| 11 | AvgDiscPercent | money | Yes |
| 12 | CatalogDiscountComments | varchar(512) | Yes |
| 13 | BidItemDiscountRate | decimal(9,5) | Yes |
| 14 | BidImportId | int | No |

#### vw_Categories {view-dbo-vw-categories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-09-27 13:52:33.330000 |
| **Modified** | 2019-09-27 13:52:33.330000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |

#### vw_CategoriesAndVendors {view-dbo-vw-categoriesandvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-08-31 13:24:40.327000 |
| **Modified** | 2018-01-21 20:26:47.980000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | DistrictId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | VendorName | varchar(50) | Yes |

#### vw_ContinuanceCharges {view-dbo-vw-continuancecharges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2023-12-04 16:54:39.283000 |
| **Modified** | 2023-12-19 11:52:09.983000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Id | uniqueidentifier | No |
| 2 | Email | varchar(255) | Yes |
| 3 | Status | char(1) | Yes |
| 4 | SignedBy | varchar(255) | Yes |
| 5 | Received | datetime | Yes |
| 6 | DistrictName | varchar(50) | Yes |
| 7 | NameAndAddress | varchar(1024) | Yes |
| 8 | ParentDistrict | varchar(50) | Yes |
| 9 | BudgetName | varchar(30) | Yes |
| 10 | SchoolYear | varchar(61) | Yes |
| 11 | SchoolYearNumber | int | Yes |
| 12 | LMAmount | money | Yes |
| 13 | RTKAmount | money | Yes |
| 14 | ChargeTypeId | int | No |
| 15 | Description | varchar(50) | Yes |
| 16 | section | int | No |
| 17 | LM | int | Yes |
| 18 | RTK | int | Yes |
| 19 | Amount | money | Yes |
| 20 | FrequencyData | varchar(50) | Yes |
| 21 | BillDate | date | Yes |
| 22 | CycleAmount | money | Yes |

#### vw_ContinuanceSection0Charges {view-dbo-vw-continuancesection0charges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2023-12-06 14:51:30.650000 |
| **Modified** | 2023-12-19 11:52:10.100000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Id | uniqueidentifier | No |
| 2 | BillDate | date | Yes |
| 3 | TotalLMAmount | money | Yes |
| 4 | TotalRTKAmount | money | Yes |
| 5 | LMAmount | money | Yes |
| 6 | RTKAmount | money | Yes |

#### vw_ContinuanceSection1Charges {view-dbo-vw-continuancesection1charges}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2023-12-07 16:12:49.250000 |
| **Modified** | 2023-12-19 11:52:10.210000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Id | uniqueidentifier | No |
| 2 | BillDate | date | Yes |
| 3 | Amount | money | Yes |
| 4 | Title | varchar(50) | Yes |
| 5 | Covering | varchar(101) | Yes |

#### vw_CrossRefsDescription {view-dbo-vw-crossrefsdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-01-29 09:45:09.157000 |
| **Modified** | 2025-12-07 20:06:47.170000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | CrossRefId | int | No |
| 3 | ItemDescription | nvarchar(4000) | Yes |
| 4 | FullDescription | nvarchar(4000) | Yes |

#### vw_CrossRefsLongDescription {view-dbo-vw-crossrefslongdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2020-12-23 19:06:57.310000 |
| **Modified** | 2021-01-24 21:56:47.453000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | CrossRefId | int | No |
| 3 | ItemDescription | varchar(4740) | Yes |

#### vw_DMSAllDocuments {view-dbo-vw-dmsalldocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-01-05 16:27:58.880000 |
| **Modified** | 2024-07-25 16:15:01.287000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DocumentType | varchar(255) | No |
| 2 | DocName | varchar(8000) | Yes |
| 3 | DocId | uniqueidentifier | No |
| 4 | PagesCaptured | int | Yes |

#### vw_DMSBidDocuments {view-dbo-vw-dmsbiddocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-01-05 14:55:06.190000 |
| **Modified** | 2024-07-25 15:53:56.177000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidNbr | varchar(MAX) | Yes |
| 3 | DocType | varchar(MAX) | Yes |
| 4 | DocId | uniqueidentifier | Yes |
| 5 | DistrictVisible | varchar(MAX) | Yes |
| 6 | PagesCaptured | int | Yes |
| 7 | FIleName | varchar(8000) | Yes |

#### vw_DMSBidDocuments_View {view-dbo-vw-dmsbiddocuments-view}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-05-01 21:57:35.850000 |
| **Modified** | 2019-09-22 07:50:49.630000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | varchar(30) | Yes |
| 2 | BidNbr | varchar(MAX) | Yes |
| 3 | DocType | varchar(MAX) | Yes |
| 4 | DocId | uniqueidentifier | No |
| 5 | DistrictVisible | varchar(MAX) | No |
| 6 | PagesCaptured | int | Yes |
| 7 | FileName | varchar(1024) | No |

#### vw_DMSRTKDocuments {view-dbo-vw-dmsrtkdocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-08-08 14:26:46.107000 |
| **Modified** | 2018-04-23 13:34:33.833000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | MSDSId | varchar(MAX) | Yes |
| 2 | DocId | uniqueidentifier | No |
| 3 | PagesCaptured | int | Yes |
| 4 | DocName | varchar(1024) | Yes |

#### vw_DMSRTKSurveys {view-dbo-vw-dmsrtksurveys}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-08-04 18:38:53.867000 |
| **Modified** | 2018-04-23 13:35:36.123000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | varchar(MAX) | Yes |
| 2 | FacilityNumber | varchar(MAX) | Yes |
| 3 | FacilityName | varchar(MAX) | Yes |
| 4 | ReportYear | varchar(MAX) | Yes |
| 5 | DocId | uniqueidentifier | No |

#### vw_DMSSDSDocuments {view-dbo-vw-dmssdsdocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-03-16 16:21:12.020000 |
| **Modified** | 2019-03-06 13:20:29.340000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | MSDSId | int | No |
| 2 | DocId | uniqueidentifier | No |
| 3 | PagesCaptured | int | Yes |
| 4 | DocName | varchar(1024) | Yes |

#### vw_DMSSDSDocuments_View {view-dbo-vw-dmssdsdocuments-view}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-02-06 14:30:49.907000 |
| **Modified** | 2019-02-06 14:30:49.907000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | MSDSId | varchar(MAX) | Yes |
| 2 | DocId | uniqueidentifier | No |
| 3 | PagesCaptured | int | Yes |
| 4 | DocName | varchar(1024) | Yes |

#### vw_DMSVendorBidDocuments {view-dbo-vw-dmsvendorbiddocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-01-05 15:29:25.410000 |
| **Modified** | 2024-09-04 14:50:01.883000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(10) | Yes |
| 2 | DistrictVisible | varchar(10) | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | BidNbr | varchar(20) | Yes |
| 5 | DocType | varchar(8000) | Yes |
| 6 | ExpirationDate | varchar(30) | Yes |
| 7 | DocumentNumber | varchar(255) | Yes |
| 8 | DocId | uniqueidentifier | Yes |
| 9 | PagesCaptured | int | Yes |
| 10 | FileName | varchar(8000) | Yes |

#### vw_DMSVendorBidDocumentsTest {view-dbo-vw-dmsvendorbiddocumentstest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-10-19 16:12:13.940000 |
| **Modified** | 2018-01-21 20:26:47.110000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(MAX) | No |
| 2 | DistrictVisible | varchar(MAX) | No |
| 3 | BidHeaderId | int | Yes |
| 4 | BidNbr | varchar(MAX) | Yes |
| 5 | DocType | varchar(MAX) | Yes |
| 6 | DocId | uniqueidentifier | No |
| 7 | PagesCaptured | int | Yes |

#### vw_DMSVendorBidDocuments_04232018 {view-dbo-vw-dmsvendorbiddocuments-04232018}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-04-23 13:11:57.853000 |
| **Modified** | 2018-04-23 13:25:08.757000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(MAX) | No |
| 2 | DistrictVisible | varchar(MAX) | No |
| 3 | BidHeaderId | int | Yes |
| 4 | BidNbr | varchar(MAX) | Yes |
| 5 | DocType | varchar(MAX) | Yes |
| 6 | ExpirationDate | varchar(MAX) | No |
| 7 | DocumentNumber | varchar(MAX) | No |
| 8 | DocId | uniqueidentifier | No |
| 9 | PagesCaptured | int | Yes |

#### vw_DMSVendorBidDocuments_View {view-dbo-vw-dmsvendorbiddocuments-view}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-05-01 21:54:56.440000 |
| **Modified** | 2023-06-30 12:16:29.730000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(MAX) | No |
| 2 | DistrictVisible | varchar(MAX) | No |
| 3 | BidHeaderId | varchar(30) | Yes |
| 4 | BidNbr | varchar(MAX) | Yes |
| 5 | DocType | varchar(MAX) | Yes |
| 6 | ExpirationDate | varchar(MAX) | No |
| 7 | DocumentNumber | varchar(MAX) | No |
| 8 | DocId | uniqueidentifier | Yes |
| 9 | PagesCaptured | int | Yes |
| 10 | FileName | varchar(1024) | No |

#### vw_DMSVendorBidDocuments_ViewTest {view-dbo-vw-dmsvendorbiddocuments-viewtest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2023-06-07 17:22:51.860000 |
| **Modified** | 2023-06-07 17:41:50.973000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(MAX) | No |
| 2 | DistrictVisible | varchar(MAX) | No |
| 3 | BidHeaderId | varchar(30) | Yes |
| 4 | BidNbr | varchar(MAX) | Yes |
| 5 | DocType | varchar(MAX) | Yes |
| 6 | ExpirationDate | varchar(MAX) | No |
| 7 | DocumentNumber | varchar(MAX) | No |
| 8 | DocId | uniqueidentifier | Yes |
| 9 | PagesCaptured | int | Yes |
| 10 | FileName | varchar(1024) | No |

#### vw_DMSVendorDocuments {view-dbo-vw-dmsvendordocuments}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-10-19 14:22:34.997000 |
| **Modified** | 2024-09-04 14:52:56.913000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(10) | Yes |
| 2 | DistrictVisible | varchar(10) | Yes |
| 3 | DocType | varchar(255) | Yes |
| 4 | ExpirationDate | varchar(30) | Yes |
| 5 | DocumentNumber | varchar(255) | Yes |
| 6 | DocId | uniqueidentifier | Yes |
| 7 | PagesCaptured | int | Yes |
| 8 | FileName | varchar(8000) | Yes |

#### vw_DMSVendorDocuments_View {view-dbo-vw-dmsvendordocuments-view}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-05-01 21:56:49.620000 |
| **Modified** | 2023-06-07 17:04:25.643000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorCode | varchar(30) | Yes |
| 2 | DistrictVisible | varchar(MAX) | No |
| 3 | DocType | varchar(MAX) | No |
| 4 | ExpirationDate | varchar(MAX) | No |
| 5 | DocumentNumber | varchar(MAX) | No |
| 6 | DocId | uniqueidentifier | Yes |
| 7 | PagesCaptured | int | Yes |
| 8 | FileName | varchar(1024) | No |

#### vw_DetailDescription {view-dbo-vw-detaildescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-03-20 20:06:16.967000 |
| **Modified** | 2026-01-22 20:17:42.033000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemDescription | nvarchar(MAX) | Yes |
| 3 | ShortDescription | nvarchar(MAX) | Yes |

#### vw_DetailDescriptionPrint {view-dbo-vw-detaildescriptionprint}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-27 11:07:37.510000 |
| **Modified** | 2018-01-21 20:26:47.993000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemDescription | varchar(2356) | Yes |

#### vw_DetailDescriptionSBS {view-dbo-vw-detaildescriptionsbs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-02-18 11:08:52.993000 |
| **Modified** | 2018-01-21 20:26:46.440000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemDescription | varchar(2880) | Yes |

#### vw_DetailDescriptionTest {view-dbo-vw-detaildescriptiontest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-03-26 11:15:12.623000 |
| **Modified** | 2018-01-21 20:26:48.003000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemDescription | varchar(2356) | Yes |

#### vw_DetailDescription_old {view-dbo-vw-detaildescription-old}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-06-25 11:43:16.200000 |
| **Modified** | 2018-01-21 20:26:47.987000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemDescription | varchar(2311) | Yes |

#### vw_DetailNotifications {view-dbo-vw-detailnotifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-03-30 12:38:07.960000 |
| **Modified** | 2024-02-29 17:10:06.527000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailNotificationId | bigint | No |
| 2 | DetailId | bigint | No |
| 3 | NotificationId | bigint | Yes |
| 4 | DateCreated | datetime | No |
| 5 | OrigItemId | int | Yes |
| 6 | NewItemId | int | Yes |
| 7 | OrigVendorId | int | Yes |
| 8 | NewVendorId | int | Yes |
| 9 | OrigBidPrice | decimal(11,5) | Yes |
| 10 | NewBidPrice | decimal(11,5) | Yes |

#### vw_DetailOnBid {view-dbo-vw-detailonbid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-05-06 10:13:47.547000 |
| **Modified** | 2022-12-20 12:18:47.577000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | Yes |
| 2 | BidHeaderId | int | Yes |
| 3 | BidAwardDate | datetime | Yes |
| 4 | EffectiveFrom | datetime | Yes |
| 5 | EffectiveUntil | datetime | Yes |
| 6 | ReadyToUseDate | datetime | Yes |

#### vw_DetailView {view-dbo-vw-detailview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 19:33:55.343000 |
| **Modified** | 2018-01-21 20:26:46.177000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | DetailId | int | No |
| 3 | ItemId | int | Yes |
| 4 | ItemCode | varchar(50) | No |
| 5 | Quantity | int | No |
| 6 | LastYearsQuantity | int | No |
| 7 | Description | varchar(3650) | Yes |
| 8 | UnitCode | varchar(20) | No |
| 9 | BidPrice | money | No |
| 10 | Extended | money | No |
| 11 | SessionId | int | No |
| 12 | VendorName | varchar(50) | No |
| 13 | VendorCode | varchar(16) | No |
| 14 | CatalogName | varchar(50) | No |
| 15 | AltDescription | varchar(1024) | No |
| 16 | VendorItemCode | varchar(50) | Yes |
| 17 | CatalogPage | char(4) | Yes |
| 18 | NoBid | int | No |
| 19 | ItemMustBeBid | int | No |
| 20 | BidInfo | varchar(51) | Yes |
| 21 | HasBeenBid | int | No |
| 22 | AllowOverride | int | No |
| 23 | VendorOverridden | int | No |
| 24 | ItemBidType | varchar(32) | Yes |

#### vw_DistrictBudgetList {view-dbo-vw-districtbudgetlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-05 15:01:29.060000 |
| **Modified** | 2018-01-21 20:26:48.010000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | selected | int | No |
| 2 | BudgetId | int | No |
| 3 | BudgetName | varchar(30) | No |
| 4 | DistrictId | int | No |
| 5 | DistrictName | varchar(50) | No |
| 6 | DistrictCode | varchar(4) | No |
| 7 | BAName | varchar(194) | No |
| 8 | DistrictNameAndAddress | varchar(189) | Yes |
| 9 | BudgetsFilterId | int | Yes |

#### vw_DistrictBudgetPP {view-dbo-vw-districtbudgetpp}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-31 00:43:30.307000 |
| **Modified** | 2018-01-21 20:26:48.013000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | selected | int | No |
| 2 | BudgetId | int | No |
| 3 | BudgetName | varchar(30) | No |
| 4 | DistrictId | int | No |
| 5 | DistrictName | varchar(50) | No |
| 6 | DistrictCode | varchar(4) | No |
| 7 | PricePlanId | int | No |
| 8 | PricePlanCode | varchar(20) | No |
| 9 | BudgetsFilterId | int | Yes |

#### vw_DistrictContactsList {view-dbo-vw-districtcontactslist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-08-27 20:04:26.090000 |
| **Modified** | 2018-08-27 20:04:26.090000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictContactId | int | No |
| 3 | FullName | varchar(174) | Yes |
| 4 | FullAddress | varchar(167) | Yes |
| 5 | FullContacts | varchar(316) | Yes |
| 6 | ContactPosition | varchar(50) | Yes |

#### vw_DistrictCounties_BidMgr {view-dbo-vw-districtcounties-bidmgr}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-16 13:32:46.850000 |
| **Modified** | 2018-01-21 20:26:48.017000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | StateCode | varchar(2) | Yes |
| 2 | CountyName | varchar(50) | Yes |

#### vw_DistrictList {view-dbo-vw-districtlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2025-03-04 09:15:42.927000 |
| **Modified** | 2025-03-04 09:15:42.927000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | County | varchar(50) | Yes |
| 2 | DistrictName | varchar(50) | Yes |
| 3 | Code | char(2) | Yes |
| 4 | StateName | varchar(50) | Yes |

#### vw_DistrictPOInfo {view-dbo-vw-districtpoinfo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-05-16 21:20:04.720000 |
| **Modified** | 2018-01-21 20:26:48.030000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RepName | varchar(30) | Yes |
| 2 | DistrictName | varchar(50) | Yes |
| 3 | State | varchar(2) | Yes |
| 4 | LY Estimated PO Count | int | Yes |
| 5 | LY PO Count | int | Yes |
| 6 | LY PO Printed Count | int | Yes |
| 7 | LY PO Exported Count | int | Yes |
| 8 | LY PIT Estimated PO Count | int | Yes |
| 9 | LY PIT PO Count | int | Yes |
| 10 | LY PIT PO Printed Count | int | Yes |
| 11 | LY PIT PO Exported Count | int | Yes |
| 12 | CY Estimated PO Count | int | Yes |
| 13 | CY PO Count | int | Yes |
| 14 | CY PO Printed Count | int | Yes |
| 15 | CY PO Exported Count | int | Yes |

#### vw_DistrictPaymentSchedule {view-dbo-vw-districtpaymentschedule}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-08-11 21:35:17.510000 |
| **Modified** | 2022-03-15 10:29:47.800000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SysId | int | No |
| 2 | DistrictId | int | Yes |
| 3 | BudgetId | int | Yes |
| 4 | DistrictName | varchar(50) | Yes |
| 5 | DistrictNameAndAddress | varchar(1024) | Yes |
| 6 | DearMsg | varchar(1024) | Yes |
| 7 | LMFeeMsg | varchar(1024) | Yes |
| 8 | RTKFeeMsg | varchar(1024) | Yes |
| 9 | ExplainationMsg | varchar(1024) | Yes |
| 10 | AcknowledgeMsg | varchar(1024) | Yes |
| 11 | ProgramName | varchar(50) | Yes |
| 12 | BudgetYear | varchar(50) | Yes |
| 13 | OrderYear | varchar(50) | Yes |
| 14 | CDateHeader | varchar(50) | Yes |
| 15 | LMAmountHeader | varchar(50) | Yes |
| 16 | RTKAmountHeader | varchar(50) | Yes |
| 17 | TotalLMCharges | money | Yes |
| 18 | TotalLMChargesStr | varchar(20) | Yes |
| 19 | TotalRTKCharges | money | Yes |
| 20 | TotalRTKChargesStr | varchar(20) | Yes |
| 21 | CDate | datetime | Yes |
| 22 | CDateStr | varchar(20) | Yes |
| 23 | ChargeId | int | Yes |
| 24 | LMAmount | money | Yes |
| 25 | LMAmountStr | varchar(20) | Yes |
| 26 | RTKAmount | money | Yes |
| 27 | RTKAmountStr | varchar(20) | Yes |
| 28 | RTK | int | Yes |
| 29 | AccountingDistrictCode | varchar(50) | Yes |
| 30 | LMChargeCode | varchar(50) | Yes |
| 31 | RTKChargeCode | varchar(50) | Yes |
| 32 | Street1 | varchar(50) | Yes |
| 33 | City | varchar(50) | Yes |
| 34 | State | varchar(10) | Yes |
| 35 | Zipcode | varchar(10) | Yes |
| 36 | PODiskAmount | money | Yes |
| 37 | PODiskCode | varchar(50) | Yes |
| 38 | GenericPOAmount | money | Yes |
| 39 | GenericPOCode | varchar(50) | Yes |
| 40 | EPOAmount | money | Yes |
| 41 | EPOCode | varchar(50) | Yes |

#### vw_DistrictSchools {view-dbo-vw-districtschools}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-27 11:33:58.073000 |
| **Modified** | 2018-01-21 20:26:48.040000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | SchoolId | int | No |
| 3 | Name | varchar(50) | Yes |

#### vw_DistrictStates_BidMgr {view-dbo-vw-districtstates-bidmgr}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-16 13:23:46.017000 |
| **Modified** | 2018-01-21 20:26:48.060000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | StateCode | varchar(2) | Yes |

#### vw_DistrictsNeedingReview {view-dbo-vw-districtsneedingreview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-04-24 14:15:15.777000 |
| **Modified** | 2018-01-21 20:26:48.053000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CSRepId | int | No |
| 2 | CSRepName | varchar(30) | No |
| 3 | DistrictId | int | No |
| 4 | DistrictName | varchar(50) | No |
| 5 | BudgetId | int | No |
| 6 | BudgetName | varchar(30) | No |
| 7 | Schedule | varchar(50) | No |
| 8 | CategoryName | varchar(50) | Yes |
| 9 | ReqsNeedingToBeBid | int | No |
| 10 | BidAddendaReqsOnHold | int | No |
| 11 | BidAddendaReqsBeingApproved | int | No |
| 12 | BidAddendaReqsApproved | int | No |
| 13 | BidAddendaReqsAtEDS | int | No |

#### vw_Districts_Assoc_With_Bid {view-dbo-vw-districts-assoc-with-bid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-08-30 13:18:27.087000 |
| **Modified** | 2018-01-21 20:26:48.040000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | DistrictId | int | No |
| 3 | Name | varchar(50) | Yes |

#### vw_DocumentTypes {view-dbo-vw-documenttypes}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-17 17:55:16.287000 |
| **Modified** | 2018-01-21 20:26:48.083000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidDocumentTypeId | int | No |
| 2 | BidType | varchar(30) | No |
| 3 | Name | varchar(50) | No |
| 4 | Description | varchar(4096) | Yes |
| 5 | VendorSpecific | varchar(3) | No |
| 6 | State | char(2) | Yes |
| 7 | Sequence | int | Yes |
| 8 | DistrictVisible | varchar(3) | No |

#### vw_EmailBlastChangeNotificationHTMLTableApprover_NotUsed {view-dbo-vw-emailblastchangenotificationhtmltableapprover-notused}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-03-31 21:32:20.360000 |
| **Modified** | 2022-04-06 13:12:12.047000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionersBlastId | int | Yes |
| 2 | ApproverUserId | int | Yes |
| 3 | EmailHTMLTable | nvarchar(MAX) | Yes |

#### vw_EmailBlastChangeNotificationHTMLTableRequisitioner_NotUsed {view-dbo-vw-emailblastchangenotificationhtmltablerequisitioner-notused}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-03-31 21:34:08.077000 |
| **Modified** | 2022-04-06 13:14:47.607000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | EmailBlastId | int | Yes |
| 2 | UserId | int | No |
| 3 | EmailHTMLTable | nvarchar(MAX) | Yes |

#### vw_ExistingRequisitions {view-dbo-vw-existingrequisitions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-02 20:33:13.023000 |
| **Modified** | 2018-01-21 20:26:48.090000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | RequisitionId | int | No |
| 3 | RequisitionNumber | varchar(24) | Yes |
| 4 | Attention | varchar(50) | Yes |
| 5 | DateEntered | datetime | Yes |
| 6 | TotalItemsCost | money | No |
| 7 | CategoryId | int | Yes |
| 8 | CategoryName | varchar(50) | Yes |
| 9 | AccountCode | varchar(50) | Yes |
| 10 | StatusName | varchar(50) | Yes |
| 11 | ApprovalLevel | tinyint | Yes |
| 12 | RequisitionStatus | varchar(255) | Yes |
| 13 | Available | money | No |

#### vw_ExistingUserAccounts {view-dbo-vw-existinguseraccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-08-30 10:49:20.120000 |
| **Modified** | 2018-01-21 20:26:48.093000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | BudgetId | int | No |
| 3 | BudgetAccountId | int | No |
| 4 | UseAllocations | tinyint | Yes |
| 5 | BudgetAmount | money | Yes |
| 6 | AmountAvailable | money | Yes |
| 7 | AccountId | int | No |
| 8 | Code | varchar(50) | Yes |

#### vw_ExistingUserAccounts_NEW {view-dbo-vw-existinguseraccounts-new}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-11-27 11:57:27.823000 |
| **Modified** | 2018-01-21 20:26:48.097000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | BudgetId | int | No |
| 3 | BudgetAccountId | int | No |
| 4 | budgetUseAllocations | tinyint | Yes |
| 5 | BudgetAmount | money | Yes |
| 6 | AmountAvailable | money | Yes |
| 7 | AccountId | int | No |
| 8 | Code | varchar(50) | Yes |
| 9 | UserAccountID | int | No |
| 10 | UseAllocations | tinyint | Yes |
| 11 | AllocationAmount | money | Yes |

#### vw_FA_ALLBudgetAccounts {view-dbo-vw-fa-allbudgetaccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:05:14.320000 |
| **Modified** | 2018-01-21 20:26:46.480000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetAccountID | int | No |
| 2 | BudgetAmount | money | No |
| 3 | AmountAvailable | money | No |
| 4 | UseAllocations | tinyint | No |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | BudgetID | int | No |
| 7 | Code | varchar(50) | Yes |
| 8 | Type | varchar(50) | Yes |
| 9 | AccountID | int | No |
| 10 | Allocated | money | No |
| 11 | Spent | money | No |
| 12 | SchoolID | int | No |
| 13 | SessionID | int | No |
| 14 | Active | int | No |

#### vw_FA_ALLUserAccounts {view-dbo-vw-fa-alluseraccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:05:29.810000 |
| **Modified** | 2023-04-19 11:02:20.527000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetAccountID | int | No |
| 2 | BudgetAmount | money | No |
| 3 | AmountAvailable | money | No |
| 4 | UseBudgetAccountAllocations | tinyint | No |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | BudgetID | int | No |
| 7 | Code | varchar(50) | Yes |
| 8 | Type | varchar(50) | Yes |
| 9 | AccountID | int | No |
| 10 | Allocated | money | No |
| 11 | Spent | money | No |
| 12 | SchoolID | int | No |
| 13 | SessionID | int | No |
| 14 | UserAccountId | int | No |
| 15 | UserId | int | Yes |
| 16 | AllocationAmount | money | No |
| 17 | AllocationAvailable | money | No |
| 18 | UseAllocations | tinyint | No |
| 19 | UserSpent | money | No |
| 20 | Active | int | No |

#### vw_FA_BudgetAccounts {view-dbo-vw-fa-budgetaccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:06:11.207000 |
| **Modified** | 2023-04-19 11:02:20.340000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetAccountID | int | No |
| 2 | BudgetAmount | money | No |
| 3 | AmountAvailable | money | No |
| 4 | UseAllocations | tinyint | No |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | BudgetID | int | No |
| 7 | Code | varchar(50) | Yes |
| 8 | Type | varchar(50) | Yes |
| 9 | AccountID | int | No |
| 10 | Allocated | money | No |
| 11 | Spent | money | No |
| 12 | SchoolID | int | No |
| 13 | SessionID | int | No |

#### vw_FA_BudgetsView {view-dbo-vw-fa-budgetsview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:03:42.880000 |
| **Modified** | 2026-01-13 11:40:51.693000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | BudgetId | int | No |
| 3 | Name | varchar(30) | Yes |
| 4 | EndDate | datetime | Yes |
| 5 | AnnualCutoff | datetime | Yes |
| 6 | CurrentBudget | int | No |
| 7 | AllowEdit | int | No |
| 8 | EditFrom | datetime | Yes |

#### vw_FA_CategoriesAndVendors {view-dbo-vw-fa-categoriesandvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-13 23:48:46.557000 |
| **Modified** | 2018-01-21 20:26:48.103000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryID | int | No |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | Yes |

#### vw_FA_EDSUser {view-dbo-vw-fa-edsuser}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:05:07.083000 |
| **Modified** | 2025-04-11 14:41:07.707000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | DistrictId | int | Yes |
| 3 | SchoolId | int | Yes |
| 4 | ShippingId | int | Yes |
| 5 | Active | tinyint | No |
| 6 | UserName | varchar(50) | Yes |
| 7 | Password | varchar(100) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | ApprovalLevel | tinyint | Yes |
| 10 | CometId | int | Yes |
| 11 | DisableNewRequisition | tinyint | Yes |
| 12 | DistrictAcctgCode | varchar(20) | Yes |
| 13 | ApproverId | int | Yes |
| 14 | NewRequisitionButton | int | No |
| 15 | AllowIncidentals | tinyint | No |
| 16 | AllowVendorChanges | tinyint | No |
| 17 | AllowShipToChanges | tinyint | No |
| 18 | AllowTM | tinyint | No |
| 19 | Email | varchar(255) | Yes |
| 20 | SecurityRoleId | int | Yes |
| 21 | Use20 | int | Yes |
| 22 | EmailByPassDate | date | Yes |
| 23 | FirstName | varchar(20) | Yes |
| 24 | LastName | varchar(30) | Yes |
| 25 | useCF | int | No |
| 26 | AllowExport | bit | No |
| 27 | HasAdminAccess | bit | No |
| 28 | Role | varchar(50) | No |
| 29 | UserDisplayName | varchar(56) | Yes |
| 30 | AllowAddenda | bit | No |
| 31 | AllowMSRP | tinyint | No |
| 32 | AllowAccountCodeMgmt | tinyint | No |
| 33 | POAccess | int | No |
| 34 | AllowVendorCodeMaintenance | tinyint | No |
| 35 | PositionData | nvarchar(4000) | Yes |

#### vw_FA_ReqCategories {view-dbo-vw-fa-reqcategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-07 18:46:07.820000 |
| **Modified** | 2018-01-21 20:26:48.107000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | BudgetId | int | No |
| 3 | CategoryId | int | No |
| 4 | Name | varchar(50) | Yes |
| 5 | CategoryType | int | Yes |

#### vw_FA_Requisitions {view-dbo-vw-fa-requisitions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-25 20:50:58.080000 |
| **Modified** | 2018-01-21 20:26:46.460000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | Yes |
| 3 | StatusID | int | No |
| 4 | StatusName | varchar(50) | No |
| 5 | TotalRequisitionCost | money | Yes |
| 6 | ApprovalLevel | tinyint | No |
| 7 | Attention | varchar(50) | Yes |
| 8 | CometId | varchar(5) | Yes |
| 9 | DateUpdated | datetime | Yes |
| 10 | NotesCount | int | Yes |
| 11 | OrderType | tinyint | Yes |
| 12 | OrderTypeDisplay | varchar(10) | No |
| 13 | UsersFullName | varchar(56) | Yes |
| 14 | CategoryID | int | No |
| 15 | CategoryName | varchar(50) | Yes |
| 16 | BudgetID | int | No |
| 17 | AccountID | int | No |
| 18 | AccountCode | varchar(50) | No |
| 19 | DistrictID | int | No |
| 20 | DistrictName | varchar(50) | No |
| 21 | SchoolID | int | No |
| 22 | SchoolName | varchar(50) | Yes |
| 23 | UserID | int | No |
| 24 | UserAccountId | int | Yes |
| 25 | SessionId | int | No |

#### vw_FA_UserAccounts {view-dbo-vw-fa-useraccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:06:26.300000 |
| **Modified** | 2023-04-19 11:02:20.443000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetAccountID | int | No |
| 2 | BudgetAmount | money | No |
| 3 | AmountAvailable | money | No |
| 4 | UseBudgetAccountAllocations | tinyint | No |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | BudgetID | int | No |
| 7 | Code | varchar(50) | Yes |
| 8 | Type | varchar(50) | Yes |
| 9 | AccountID | int | No |
| 10 | Allocated | money | No |
| 11 | Spent | money | No |
| 12 | SchoolID | int | No |
| 13 | SessionID | int | No |
| 14 | UserAccountId | int | No |
| 15 | Active | tinyint | Yes |
| 16 | UserId | int | Yes |
| 17 | AllocationAmount | money | No |
| 18 | AllocationAvailable | money | No |
| 19 | UseAllocations | tinyint | No |
| 20 | UserSpent | money | No |

#### vw_FA_UserDisplayName {view-dbo-vw-fa-userdisplayname}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-13 23:48:52.270000 |
| **Modified** | 2018-01-21 20:26:46.457000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserID | int | No |
| 2 | UserDisplayName | varchar(56) | Yes |

#### vw_FA_UserList {view-dbo-vw-fa-userlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-14 00:01:58.407000 |
| **Modified** | 2018-01-21 20:26:48.110000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | DistrictId | int | No |
| 3 | SchoolId | int | No |
| 4 | UserId | int | No |
| 5 | DisplayName | varchar(56) | Yes |

#### vw_FA_UserLogin {view-dbo-vw-fa-userlogin}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-13 23:57:03.773000 |
| **Modified** | 2018-01-21 20:26:48.113000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserIsActive | tinyint | Yes |
| 2 | UserID | int | No |
| 3 | CometId | int | Yes |
| 4 | Password | varchar(10) | Yes |
| 5 | Attention | varchar(50) | Yes |
| 6 | ApprovalLevel | tinyint | Yes |
| 7 | ApproverID | int | Yes |
| 8 | HasAdminAccess | bit | Yes |
| 9 | SchoolIsActive | tinyint | Yes |
| 10 | SchoolID | int | No |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | DistrictIsActive | tinyint | Yes |
| 13 | DistrictName | varchar(50) | Yes |
| 14 | DistrictID | int | No |
| 15 | DistrictCode | varchar(4) | Yes |
| 16 | CSRepID | int | Yes |

#### vw_Financials {view-dbo-vw-financials}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-09-12 16:16:06.807000 |
| **Modified** | 2023-12-22 11:18:08.057000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | Yes |
| 2 | BudgetId | int | No |
| 3 | Description | varchar(50) | Yes |
| 4 | dcId | uniqueidentifier | Yes |
| 5 | Status | varchar(13) | No |
| 6 | Received | datetime | Yes |
| 7 | SignedBy | varchar(255) | Yes |
| 8 | Comments | varchar(4096) | Yes |
| 9 | DistrictChargeId | int | Yes |
| 10 | Amount | money | Yes |
| 11 | FrequencyData | varchar(50) | Yes |
| 12 | dpcId | uniqueidentifier | Yes |
| 13 | ProposedAmount | money | Yes |
| 14 | PreviousAmount | money | Yes |
| 15 | BillMonths | varchar(8000) | Yes |

#### vw_FormattedDetailDescription {view-dbo-vw-formatteddetaildescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-22 20:51:38.677000 |
| **Modified** | 2018-01-21 20:26:48.123000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemDescription | varchar(2893) | Yes |

#### vw_GetMSDSInfo {view-dbo-vw-getmsdsinfo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-03-16 13:45:08.517000 |
| **Modified** | 2018-01-21 20:26:48.127000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | MSDSId | int | No |
| 2 | ItemDescription | varchar(60) | Yes |
| 3 | ItemList | varchar(1024) | Yes |

#### vw_HeadingsByBid {view-dbo-vw-headingsbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-05 18:19:05.040000 |
| **Modified** | 2018-01-21 20:26:48.130000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | HeadingId | int | No |
| 3 | HeadingTitle | varchar(255) | Yes |

#### vw_HeadingsByReq {view-dbo-vw-headingsbyreq}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-13 23:57:11.310000 |
| **Modified** | 2019-11-05 04:56:19.913000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | HeadingId | int | No |
| 3 | Title | varchar(255) | Yes |
| 4 | DateCreated | datetime | Yes |
| 5 | DistrictId | int | Yes |

#### vw_HeadingsByReqTest {view-dbo-vw-headingsbyreqtest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-01-14 21:18:26.403000 |
| **Modified** | 2019-01-14 21:22:06.597000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | HeadingId | int | No |
| 3 | Title | varchar(255) | Yes |

#### vw_HeadingsKeywordsByBid {view-dbo-vw-headingskeywordsbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-05 18:18:52.523000 |
| **Modified** | 2018-01-21 20:26:46.037000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | HeadingId | int | No |
| 3 | HeadingTitle | varchar(255) | No |
| 4 | KeywordId | int | No |
| 5 | Keyword | varchar(50) | No |

#### vw_IncidentalOrderDownloads {view-dbo-vw-incidentalorderdownloads}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-02-18 13:37:46.623000 |
| **Modified** | 2025-07-22 07:31:16.720000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | BudgetId | int | Yes |
| 3 | RequisitionId | int | Yes |
| 4 | RequisitionNumber | varchar(24) | Yes |
| 5 | UploadDate | datetime | Yes |

#### vw_IncidentalOrderDownloadsDetail {view-dbo-vw-incidentalorderdownloadsdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-02-18 15:01:24.280000 |
| **Modified** | 2018-01-21 20:26:48.143000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | DistrictRequisitionNumber | varchar(50) | Yes |

#### vw_InstructionBookCalendar {view-dbo-vw-instructionbookcalendar}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-10-28 12:59:36.380000 |
| **Modified** | 2018-01-21 20:26:46.683000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | UserId | int | No |
| 3 | CalendarId | int | No |
| 4 | HeaderText | varchar(8000) | Yes |
| 5 | FooterText | varchar(8000) | Yes |
| 6 | HeaderTextHTML | varchar(4096) | Yes |
| 7 | FooterTextHTML | varchar(4096) | No |
| 8 | CalendarTypeId | int | No |
| 9 | DateCount | int | No |
| 10 | Description | varchar(50) | Yes |
| 11 | Date1 | datetime | No |
| 12 | Date2 | datetime | Yes |
| 13 | Date3 | datetime | Yes |
| 14 | Date4 | datetime | Yes |
| 15 | BookType | varchar(50) | No |
| 16 | ScheduleGroup | varchar(50) | No |
| 17 | CalendarName | varchar(83) | Yes |

#### vw_InstructionBookContents {view-dbo-vw-instructionbookcontents}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-10-28 15:33:25.867000 |
| **Modified** | 2018-01-21 20:26:46.770000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | UserId | int | No |
| 3 | Priority | int | Yes |
| 4 | Title | varchar(255) | Yes |
| 5 | TitleInTOC | tinyint | Yes |
| 6 | Body | varchar(4096) | Yes |
| 7 | HeaderAttributes | int | Yes |
| 8 | IBCId | int | No |
| 9 | SubReportName | varchar(1024) | Yes |
| 10 | HTMLBody | varchar(MAX) | No |

#### vw_IsRequisitionLocked {view-dbo-vw-isrequisitionlocked}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-11-18 11:34:58.590000 |
| **Modified** | 2018-01-21 20:26:48.147000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | IsLocked | int | No |

#### vw_ItemDescription {view-dbo-vw-itemdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-03-20 19:53:28.450000 |
| **Modified** | 2019-01-30 13:57:49.960000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | CategoryId | int | Yes |
| 3 | ItemDescription | varchar(1156) | Yes |

#### vw_ItemDescriptionNoExtra {view-dbo-vw-itemdescriptionnoextra}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-09-22 13:15:40.080000 |
| **Modified** | 2018-01-21 20:26:48.150000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | ItemDescription | varchar(1156) | Yes |

#### vw_ItemDescriptionNoExtraNH {view-dbo-vw-itemdescriptionnoextranh}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-03-01 11:21:32.977000 |
| **Modified** | 2018-01-21 20:26:47.117000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | ItemDescription | varchar(848) | Yes |

#### vw_ItemPricing {view-dbo-vw-itempricing}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-24 14:25:37.180000 |
| **Modified** | 2018-01-21 20:26:46.063000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | categoryId | int | Yes |
| 3 | ItemId | int | No |
| 4 | CatalogId | int | Yes |
| 5 | CrossRefId | int | Yes |
| 6 | ItemCode | varchar(50) | Yes |
| 7 | Description | varchar(2356) | Yes |
| 8 | UnitId | int | Yes |
| 9 | UnitCode | varchar(20) | Yes |
| 10 | BidPrice | decimal(34,13) | Yes |
| 11 | CatalogPrice | money | Yes |
| 12 | GrossPrice | money | Yes |
| 13 | DiscountRate | decimal(15,5) | Yes |
| 14 | CatalogPage | varchar(16) | Yes |
| 15 | CatalogYear | char(2) | Yes |
| 16 | PricePlanId | int | Yes |
| 17 | AwardId | int | Yes |
| 18 | VendorId | int | Yes |
| 19 | VendorItemCode | varchar(50) | Yes |
| 20 | PackedVendorItemCode | varchar(255) | Yes |
| 21 | Alternate | varchar(512) | Yes |
| 22 | SortSeq | varchar(64) | Yes |
| 23 | BidItemId | int | Yes |
| 24 | ItemMustBeBid | int | No |
| 25 | PriceSort | varchar(82) | Yes |

#### vw_ItemsByBid {view-dbo-vw-itemsbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-05 16:36:17.517000 |
| **Modified** | 2018-01-21 20:26:45.947000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | CategoryId | int | Yes |
| 3 | ItemId | int | No |
| 4 | ItemCode | varchar(50) | No |
| 5 | ItemDescription | varchar(1156) | No |
| 6 | UnitCode | varchar(20) | No |
| 7 | HeadingId | int | No |
| 8 | HeadingTitle | varchar(255) | No |
| 9 | KeywordId | int | No |
| 10 | Keyword | varchar(50) | No |
| 11 | VendorId | int | No |
| 12 | VendorName | varchar(50) | No |
| 13 | SortSeq | varchar(64) | Yes |
| 14 | NetPrice | decimal(33,13) | Yes |
| 15 | CatalogName | varchar(50) | No |
| 16 | CatalogPrice | money | No |
| 17 | RequisitionId | int | No |
| 18 | DetailId | int | No |
| 19 | Quantity | int | No |
| 20 | Alternate | varchar(512) | No |
| 21 | ItemBidType | varchar(32) | No |
| 22 | PageNo | int | No |
| 23 | VendorItemCode | varchar(50) | No |

#### vw_JavaReqDetail {view-dbo-vw-javareqdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-07-01 13:39:27.850000 |
| **Modified** | 2018-01-21 20:26:48.157000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | RequisitionId | int | Yes |
| 3 | Alternate | varchar(1024) | No |
| 4 | BidPrice | money | No |
| 5 | CatalogPage | char(4) | No |
| 6 | CatalogPrice | money | No |
| 7 | Description | varchar(1024) | No |
| 8 | DistrictRequisitionNumber | varchar(50) | No |
| 9 | ExtraDescription | varchar(1024) | No |
| 10 | HeadingTitle | varchar(255) | No |
| 11 | ItemCode | varchar(50) | No |
| 12 | ItemMustBeBid | int | No |
| 13 | Keyword | varchar(50) | No |
| 14 | LastYearsQuantity | int | No |
| 15 | Modified | datetime | Yes |
| 16 | Quantity | int | No |
| 17 | SectionName | varchar(255) | No |
| 18 | SortSeq | varchar(64) | No |
| 19 | UnitCode | varchar(20) | No |
| 20 | VendorItemCode | varchar(50) | No |
| 21 | UserNbr | int | No |
| 22 | Attention | varchar(50) | No |
| 23 | VendorName | varchar(50) | No |
| 24 | DistrictVendorCode | varchar(20) | No |
| 25 | VendorsAccountCode | varchar(50) | No |
| 26 | CatalogName | varchar(50) | No |

#### vw_KeywordsByBid {view-dbo-vw-keywordsbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-05 18:12:57.690000 |
| **Modified** | 2018-01-21 20:26:45.980000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | KeywordId | int | No |
| 3 | Keyword | varchar(50) | No |

#### vw_KeywordsByReqHeading {view-dbo-vw-keywordsbyreqheading}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-13 23:57:19.733000 |
| **Modified** | 2019-08-07 11:48:35.790000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | HeadingId | int | No |
| 3 | KeywordId | int | No |
| 4 | Keyword | varchar(50) | Yes |

#### vw_LastBidAwardDate {view-dbo-vw-lastbidawarddate}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-04-13 19:00:00.170000 |
| **Modified** | 2022-04-07 17:30:32.597000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | LastAwardDate | varchar(30) | No |
| 3 | LastAwardDateSort | varchar(30) | No |

#### vw_LatestCrossRef {view-dbo-vw-latestcrossref}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-07-15 23:30:20.137000 |
| **Modified** | 2018-01-21 20:26:48.170000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ItemId | int | Yes |
| 3 | CrossRefId | int | No |
| 4 | CatalogYear | char(2) | Yes |
| 5 | CatalogPrice | money | Yes |

#### vw_LowestPrice {view-dbo-vw-lowestprice}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-08-19 15:42:15.933000 |
| **Modified** | 2022-12-16 13:05:12.700000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestItemId | int | No |
| 3 | BidResultsId | int | No |
| 4 | BidPrice | decimal(34,13) | Yes |

#### vw_MPIHeadings {view-dbo-vw-mpiheadings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-02-25 14:55:08.710000 |
| **Modified** | 2018-01-21 20:26:48.177000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | HeadingId | bigint | Yes |
| 3 | HeadingTitle | varchar(308) | Yes |

#### vw_MSRPBidReqManufacturer {view-dbo-vw-msrpbidreqmanufacturer}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-09-26 14:41:07.390000 |
| **Modified** | 2018-01-21 20:26:48.180000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestManufacturerId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | ManufacturerId | int | Yes |
| 5 | SequenceNumber | int | Yes |
| 6 | AllowAdditionalProductLines | tinyint | Yes |
| 7 | UseOptions | tinyint | Yes |
| 8 | Name | varchar(100) | No |

#### vw_MSRPBidReqManufacturerWriteIn {view-dbo-vw-msrpbidreqmanufacturerwritein}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-11 14:28:32.110000 |
| **Modified** | 2018-01-21 20:26:48.183000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestManufacturerId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | ManufacturerId | int | Yes |
| 5 | SequenceNumber | int | Yes |
| 6 | AllowAdditionalProductLines | tinyint | Yes |
| 7 | UseOptions | tinyint | Yes |
| 8 | Name | varchar(100) | No |

#### vw_MSRPBidReqProdLineAndOption {view-dbo-vw-msrpbidreqprodlineandoption}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-09-23 17:11:28.520000 |
| **Modified** | 2018-01-21 20:26:48.187000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestManufacturerId | int | No |
| 3 | ManufacturerId | int | Yes |
| 4 | ManufacturerName | varchar(100) | Yes |
| 5 | BidRequestProductLineId | int | No |
| 6 | ManufacturerProductLineId | int | Yes |
| 7 | ProductLineName | varchar(100) | Yes |
| 8 | BidRequestoptionId | int | No |
| 9 | OptionName | varchar(50) | Yes |
| 10 | SortKey | varchar(512) | Yes |

#### vw_MSRPBidReqProdLineAndOptionWriteIn {view-dbo-vw-msrpbidreqprodlineandoptionwritein}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-11 14:38:50.517000 |
| **Modified** | 2018-01-21 20:26:48.193000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidRequestManufacturerId | int | No |
| 3 | ManufacturerId | int | Yes |
| 4 | ManufacturerName | varchar(100) | Yes |
| 5 | BidRequestProductLineId | int | No |
| 6 | ManufacturerProductLineId | int | Yes |
| 7 | ProductLineName | varchar(100) | Yes |
| 8 | BidRequestoptionId | int | No |
| 9 | OptionName | varchar(50) | Yes |
| 10 | SortKey | varchar(512) | Yes |

#### vw_MSRPBidReqProductLine {view-dbo-vw-msrpbidreqproductline}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-10 17:07:55.307000 |
| **Modified** | 2018-01-21 20:26:48.197000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidRequestProductLineId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | BidRequestManufacturerId | int | No |
| 4 | ManufacturerProductLineId | int | Yes |
| 5 | NameManufProdLine | varchar(100) | No |
| 6 | AllFlag | int | No |

#### vw_MSRPBidResultsManufRev2 {view-dbo-vw-msrpbidresultsmanufrev2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-17 15:47:47.567000 |
| **Modified** | 2018-01-21 20:26:46.103000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | No |
| 2 | BidImportId | int | No |
| 3 | WriteInFlag | tinyint | No |
| 4 | ManufacturerName | varchar(100) | No |
| 5 | Active | int | No |
| 6 | AuthorizationLetter | tinyint | No |
| 7 | SubmittedExcel | tinyint | No |
| 8 | ProductCatalog | tinyint | No |
| 9 | TotalAward | tinyint | No |
| 10 | VendorPriceFile | tinyint | No |
| 11 | TotalAwardString | varchar(20) | Yes |
| 12 | BidMSRPResultsId | int | No |
| 13 | BidRequestManufacturerId | int | Yes |
| 14 | ManufacturerId | int | Yes |
| 15 | PriceListTypeId | int | No |
| 16 | WriteInManufacturer | varchar(100) | Yes |
| 17 | VendorName | varchar(50) | Yes |
| 18 | ActiveBidImport | tinyint | Yes |
| 19 | ActiveBidMSRPResults | tinyint | Yes |
| 20 | TotalAwardDiscount | decimal(9,5) | Yes |
| 21 | ExcelFileApproved | tinyint | No |

#### vw_MSRPBidResultsProdLines {view-dbo-vw-msrpbidresultsprodlines}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-10-07 18:04:09.343000 |
| **Modified** | 2018-01-21 20:26:46.090000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsProductLineId | int | No |
| 2 | BidMSRPResultsId | int | No |
| 3 | Active | tinyint | Yes |
| 4 | ProdLineOrWriteIn | varchar(100) | No |
| 5 | WriteInProductLineFlag | tinyint | Yes |
| 6 | BidRequestProductLineId | int | Yes |
| 7 | BidRequestOptionId | int | Yes |
| 8 | MSRPOptionId | int | Yes |
| 9 | OptionName | varchar(50) | Yes |
| 10 | WeightedDiscount | decimal(9,5) | Yes |
| 11 | Modified | datetime | Yes |
| 12 | SortKey | varchar(512) | Yes |
| 13 | ManufacturerProductLineId | int | No |

#### vw_MSRPCategoriesBySession {view-dbo-vw-msrpcategoriesbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-17 15:16:51.640000 |
| **Modified** | 2021-12-07 13:52:52.623000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | BidHeaderId | varchar(8000) | Yes |

#### vw_MSRPMPLVendorsCategoriesBySession {view-dbo-vw-msrpmplvendorscategoriesbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-05-07 11:54:45.703000 |
| **Modified** | 2018-11-14 13:30:48.840000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | VendorId | int | No |
| 5 | VendorName | varchar(50) | No |
| 6 | VendorCode | varchar(16) | No |
| 7 | ManufacturerId | int | No |
| 8 | ManufacturerName | varchar(100) | No |
| 9 | BidHeaderId | int | Yes |
| 10 | BidAdvertised | datetime | Yes |
| 11 | BidAwardDate | datetime | Yes |
| 12 | EffectiveFrom | datetime | Yes |
| 13 | EffectiveUntil | datetime | Yes |
| 14 | BidMessage | varchar(1024) | Yes |
| 15 | HostAwardDate | datetime | Yes |
| 16 | VendorBidNumber | varchar(50) | Yes |
| 17 | Comments | varchar(1024) | Yes |
| 18 | Website | varchar(255) | Yes |
| 19 | ManufacturersDiscountRate | decimal(9,5) | Yes |
| 20 | ManufacturersDiscountRateStr | varchar(32) | Yes |
| 21 | ManufacturersUpDownStr | varchar(9) | No |
| 22 | Address1 | varchar(50) | Yes |
| 23 | Address2 | varchar(50) | Yes |
| 24 | City | varchar(50) | Yes |
| 25 | State | char(2) | Yes |
| 26 | Zipcode | varchar(10) | Yes |
| 27 | VendorContactFullName | varchar(150) | Yes |
| 28 | VendorContactEMail | varchar(255) | Yes |
| 29 | VendorContactPhone | varchar(25) | Yes |
| 30 | VendorContactFax | varchar(20) | Yes |
| 31 | VendorsManufacturerNotes | varchar(1000) | No |
| 32 | StateName | varchar(50) | No |
| 33 | ProductLine | varchar(100) | No |
| 34 | OptionName | varchar(50) | No |
| 35 | ProductLineDiscountRate | decimal(9,5) | Yes |
| 36 | ProductLineDiscountRateStr | varchar(32) | Yes |
| 37 | ProductLineUpDownStr | varchar(9) | No |
| 38 | RangeBase | numeric(19,4) | Yes |
| 39 | RangeTop | numeric(20,4) | Yes |
| 40 | PriceRangeDiscountRate | decimal(9,5) | Yes |
| 41 | PriceRangeDiscountRateStr | varchar(32) | Yes |
| 42 | PriceRangeUpDownStr | varchar(9) | No |
| 43 | BMAId | int | No |
| 44 | ManufacturerProductLineId | int | No |
| 45 | MSRPOptionId | int | No |
| 46 | BidProductLineId | int | No |

#### vw_MSRPMPLVendorsCategoriesReport {view-dbo-vw-msrpmplvendorscategoriesreport}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-11-28 15:24:00.133000 |
| **Modified** | 2022-06-17 13:33:00.820000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | No |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | No |
| 5 | VendorCode | varchar(16) | No |
| 6 | ManufacturerId | int | No |
| 7 | ManufacturerName | varchar(100) | No |
| 8 | BidHeaderId | int | Yes |
| 9 | BidAdvertised | datetime | Yes |
| 10 | BidAwardDate | datetime | Yes |
| 11 | EffectiveFrom | datetime | Yes |
| 12 | EffectiveUntil | datetime | Yes |
| 13 | BidMessage | varchar(1024) | Yes |
| 14 | HostAwardDate | datetime | Yes |
| 15 | VendorBidNumber | varchar(50) | Yes |
| 16 | Comments | varchar(1024) | Yes |
| 17 | Website | varchar(255) | Yes |
| 18 | ManufacturersDiscountRate | decimal(9,5) | Yes |
| 19 | ManufacturersDiscountRateStr | varchar(32) | Yes |
| 20 | ManufacturersUpDownStr | varchar(9) | No |
| 21 | Address1 | varchar(50) | Yes |
| 22 | Address2 | varchar(50) | Yes |
| 23 | City | varchar(50) | Yes |
| 24 | State | char(2) | Yes |
| 25 | Zipcode | varchar(10) | Yes |
| 26 | VendorContactFullName | varchar(150) | Yes |
| 27 | VendorContactEMail | varchar(255) | Yes |
| 28 | VendorContactPhone | varchar(25) | Yes |
| 29 | VendorContactFax | varchar(20) | Yes |
| 30 | VendorsManufacturerNotes | varchar(1000) | No |
| 31 | StateName | varchar(50) | No |
| 32 | ProductLine | varchar(100) | No |
| 33 | OptionName | varchar(50) | No |
| 34 | ProductLineDiscountRate | decimal(9,5) | Yes |
| 35 | ProductLineDiscountRateStr | varchar(32) | Yes |
| 36 | ProductLineUpDownStr | varchar(9) | No |
| 37 | RangeBase | money | Yes |
| 38 | RangeTop | numeric(20,4) | Yes |
| 39 | PriceRangeDiscountRate | decimal(9,5) | Yes |
| 40 | PriceRangeDiscountRateStr | varchar(32) | Yes |
| 41 | PriceRangeUpDownStr | varchar(9) | No |
| 42 | BMAId | int | No |
| 43 | ManufacturerProductLineId | int | No |
| 44 | MSRPOptionId | int | No |
| 45 | BidProductLineId | int | No |
| 46 | HostDistrict | varchar(50) | No |
| 47 | RangeStr | varchar(43) | Yes |
| 48 | VendorNameAndAddress | varchar(394) | Yes |
| 49 | ContactName | varchar(170) | Yes |
| 50 | AwardType | varchar(10) | No |
| 51 | ReawardDate | datetime | Yes |
| 52 | ReawardFrom | datetime | Yes |
| 53 | ReawardUntil | datetime | Yes |
| 54 | PricePlanId | int | Yes |

#### vw_MSRPMPLVendorsCategoriesReportBC {view-dbo-vw-msrpmplvendorscategoriesreportbc}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-12-01 19:15:44.350000 |
| **Modified** | 2022-12-01 19:15:44.350000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryId | int | No |
| 2 | CategoryName | varchar(50) | Yes |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | No |
| 5 | VendorCode | varchar(16) | No |
| 6 | ManufacturerId | int | No |
| 7 | ManufacturerName | varchar(100) | No |
| 8 | BidHeaderId | int | Yes |
| 9 | BidAdvertised | datetime | Yes |
| 10 | BidAwardDate | datetime | Yes |
| 11 | EffectiveFrom | datetime | Yes |
| 12 | EffectiveUntil | datetime | Yes |
| 13 | BidMessage | varchar(1024) | Yes |
| 14 | HostAwardDate | datetime | Yes |
| 15 | VendorBidNumber | varchar(50) | Yes |
| 16 | Comments | varchar(1024) | Yes |
| 17 | Website | varchar(255) | Yes |
| 18 | ManufacturersDiscountRate | decimal(9,5) | Yes |
| 19 | ManufacturersDiscountRateStr | varchar(32) | Yes |
| 20 | ManufacturersUpDownStr | varchar(9) | No |
| 21 | Address1 | varchar(50) | Yes |
| 22 | Address2 | varchar(50) | Yes |
| 23 | City | varchar(50) | Yes |
| 24 | State | char(2) | Yes |
| 25 | Zipcode | varchar(10) | Yes |
| 26 | VendorContactFullName | varchar(150) | Yes |
| 27 | VendorContactEMail | varchar(255) | Yes |
| 28 | VendorContactPhone | varchar(25) | Yes |
| 29 | VendorContactFax | varchar(20) | Yes |
| 30 | VendorsManufacturerNotes | varchar(1000) | No |
| 31 | StateName | varchar(50) | No |
| 32 | ProductLine | varchar(100) | No |
| 33 | OptionName | varchar(50) | No |
| 34 | ProductLineDiscountRate | decimal(9,5) | Yes |
| 35 | ProductLineDiscountRateStr | varchar(32) | Yes |
| 36 | ProductLineUpDownStr | varchar(9) | No |
| 37 | RangeBase | money | Yes |
| 38 | RangeTop | numeric(20,4) | Yes |
| 39 | PriceRangeDiscountRate | decimal(9,5) | Yes |
| 40 | PriceRangeDiscountRateStr | varchar(32) | Yes |
| 41 | PriceRangeUpDownStr | varchar(9) | No |
| 42 | BMAId | int | No |
| 43 | ManufacturerProductLineId | int | No |
| 44 | MSRPOptionId | int | No |
| 45 | BidProductLineId | int | No |
| 46 | HostDistrict | varchar(50) | No |
| 47 | RangeStr | varchar(43) | Yes |
| 48 | VendorNameAndAddress | varchar(394) | Yes |
| 49 | ContactName | varchar(170) | Yes |
| 50 | AwardType | varchar(10) | No |
| 51 | ReawardDate | datetime | Yes |
| 52 | ReawardFrom | datetime | Yes |
| 53 | ReawardUntil | datetime | Yes |
| 54 | PricePlanId | int | Yes |

#### vw_MSRPManufacturersBySession {view-dbo-vw-msrpmanufacturersbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-17 15:23:11.020000 |
| **Modified** | 2021-12-07 13:52:53.273000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | VendorId | int | No |
| 3 | ManufacturerId | int | No |
| 4 | ManufacturerName | varchar(100) | No |
| 5 | WebsiteLink | varchar(255) | No |
| 6 | BidHeaderId | int | Yes |
| 7 | DiscountRate | decimal(9,5) | Yes |
| 8 | DiscountRateStr | varchar(32) | Yes |
| 9 | UpDownStr | varchar(10) | No |
| 10 | VendorsManufacturerNotes | varchar(1000) | No |
| 11 | CategoryId | int | No |

#### vw_MSRPProductLineExceptions {view-dbo-vw-msrpproductlineexceptions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2020-01-13 12:49:09.577000 |
| **Modified** | 2020-01-15 18:00:08.317000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | ManufacturerId | int | Yes |
| 3 | ProductLineExceptions | varchar(8000) | Yes |

#### vw_MSRPRankManufacturerAWD {view-dbo-vw-msrprankmanufacturerawd}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-11-20 13:13:19.050000 |
| **Modified** | 2018-01-21 20:26:46.910000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsId | int | No |
| 2 | ManufacturerId | int | Yes |
| 3 | AverageWeightedDiscount | decimal(38,6) | Yes |

#### vw_MSRPRankOptionAWD {view-dbo-vw-msrprankoptionawd}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-11-17 16:11:32.840000 |
| **Modified** | 2018-01-21 20:26:46.913000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsId | int | No |
| 2 | BidMSRPResultsProductLineId | int | No |
| 3 | BidRequestOptionId | int | Yes |
| 4 | BidRequestProductLineId | int | Yes |
| 5 | ManufacturerProductLineId | int | Yes |
| 6 | MSRPOptionId | int | Yes |
| 7 | OptionName | varchar(50) | Yes |
| 8 | Weight | decimal(9,5) | Yes |
| 9 | AverageWeightedDiscount | decimal(38,6) | Yes |

#### vw_MSRPRankProductLineAWD {view-dbo-vw-msrprankproductlineawd}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-11-17 16:13:20.493000 |
| **Modified** | 2018-01-21 20:26:46.920000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsId | int | No |
| 2 | ManufacturerProductLineId | int | Yes |
| 3 | AverageWeightedDiscount | decimal(38,6) | Yes |

#### vw_MSRPRankRequirements {view-dbo-vw-msrprankrequirements}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-11-24 14:01:56.830000 |
| **Modified** | 2018-01-21 20:26:46.907000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsId | int | No |
| 2 | BidMSRPResultsProductLineId | int | No |
| 3 | SortKey | varchar(3) | Yes |

#### vw_MSRPRankTieBreaker {view-dbo-vw-msrpranktiebreaker}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-11-24 16:03:01.407000 |
| **Modified** | 2018-01-21 20:26:46.900000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidMSRPResultsId | int | No |
| 2 | BidMSRPResultsProductLineId | int | No |
| 3 | SortKey | varchar(2) | No |

#### vw_MSRPVendorsAndManufacturersByReq {view-dbo-vw-msrpvendorsandmanufacturersbyreq}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-05-21 11:09:20.030000 |
| **Modified** | 2018-01-21 20:26:48.220000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | Yes |
| 5 | ManufacturerId | int | No |
| 6 | ManufacturerName | varchar(100) | No |
| 7 | DiscountRate | decimal(9,5) | No |
| 8 | FullName | varchar(150) | Yes |
| 9 | Phone | varchar(25) | Yes |
| 10 | VendorURL | varchar(255) | No |
| 11 | ManufacturerURL | varchar(255) | Yes |

#### vw_MSRPVendorsBidHeaderBySession {view-dbo-vw-msrpvendorsbidheaderbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-17 15:15:45.930000 |
| **Modified** | 2025-09-18 15:12:45.073000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | Yes |
| 4 | VendorCode | varchar(16) | No |
| 5 | BidHeaderId | int | Yes |
| 6 | CategoryId | int | No |

#### vw_MSRPVendorsCategoriesBySession {view-dbo-vw-msrpvendorscategoriesbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-25 11:54:32.960000 |
| **Modified** | 2025-09-18 15:12:45.213000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | VendorId | int | No |
| 5 | VendorName | varchar(50) | Yes |
| 6 | VendorCode | varchar(16) | No |
| 7 | ManufacturerId | int | No |
| 8 | ManufacturerName | varchar(100) | No |
| 9 | BidHeaderId | int | Yes |
| 10 | BidAdvertised | datetime | Yes |
| 11 | BidAwardDate | datetime | Yes |
| 12 | EffectiveFrom | datetime | Yes |
| 13 | EffectiveUntil | datetime | Yes |
| 14 | BidMessage | varchar(1024) | Yes |
| 15 | HostAwardDate | datetime | Yes |
| 16 | VendorBidNumber | varchar(50) | Yes |
| 17 | Comments | varchar(1024) | Yes |
| 18 | Website | varchar(255) | Yes |
| 19 | DiscountRate | decimal(9,5) | Yes |
| 20 | DiscountRateStr | varchar(32) | Yes |
| 21 | UpDownStr | varchar(9) | No |
| 22 | Address1 | varchar(50) | Yes |
| 23 | Address2 | varchar(50) | Yes |
| 24 | City | varchar(50) | Yes |
| 25 | State | char(2) | Yes |
| 26 | Zipcode | varchar(10) | Yes |
| 27 | VendorContactFullName | varchar(150) | Yes |
| 28 | VendorContactEMail | varchar(255) | Yes |
| 29 | VendorContactPhone | varchar(25) | Yes |
| 30 | VendorContactFax | varchar(20) | Yes |
| 31 | VendorsManufacturerNotes | varchar(1000) | No |
| 32 | StateName | varchar(50) | No |

#### vw_MultiVendorPODistrictsAndBudgets {view-dbo-vw-multivendorpodistrictsandbudgets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-03-24 12:41:51.697000 |
| **Modified** | 2018-01-21 20:26:48.240000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | BudgetId | int | No |
| 3 | VendorSessionId | int | No |
| 4 | DistrictName | varchar(50) | Yes |
| 5 | BudgetName | varchar(30) | Yes |
| 6 | VendorsAccountCode | varchar(50) | No |
| 7 | BudgetFilterId | int | Yes |
| 8 | CurrentBidPOCount | int | Yes |

#### vw_NJDistricts {view-dbo-vw-njdistricts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-03-10 14:40:21.427000 |
| **Modified** | 2018-01-21 20:26:48.247000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | DistrictCode | varchar(4) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | NameAndAddress | varchar(1024) | Yes |
| 5 | BAName | varchar(50) | No |
| 6 | PhoneNumber | varchar(20) | Yes |
| 7 | County | varchar(50) | No |
| 8 | CSRepName | varchar(30) | No |

#### vw_NY_TM_Districts {view-dbo-vw-ny-tm-districts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-07-26 11:28:31.913000 |
| **Modified** | 2018-01-21 20:26:46.813000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(50) | Yes |
| 2 | FullName | varchar(174) | No |
| 3 | Email | varchar(255) | No |
| 4 | Description | varchar(50) | No |
| 5 | Address1 | varchar(50) | No |
| 6 | City | varchar(50) | No |
| 7 | State | char(2) | No |
| 8 | Zipcode | varchar(10) | No |

#### vw_NY_TM_Districts_Mailing {view-dbo-vw-ny-tm-districts-mailing}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-07-26 12:42:36.383000 |
| **Modified** | 2018-01-21 20:26:46.820000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(50) | Yes |
| 2 | FullName | varchar(174) | Yes |
| 3 | Address1 | varchar(50) | Yes |
| 4 | City | varchar(50) | No |
| 5 | State | varchar(2) | No |
| 6 | Zipcode | varchar(10) | No |

#### vw_OverrideReferences {view-dbo-vw-overridereferences}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-10 19:05:30.097000 |
| **Modified** | 2018-01-21 20:26:46.593000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | FilterByDetailId | int | No |
| 3 | DetailId | int | No |
| 4 | RequisitionNumber | varchar(24) | Yes |
| 5 | Requisitions_Attention | varchar(50) | Yes |
| 6 | AccountCode | varchar(50) | Yes |
| 7 | TotalRequisitionCost | money | Yes |
| 8 | School_Name | varchar(50) | Yes |
| 9 | District_Name | varchar(50) | Yes |
| 10 | CometId | int | Yes |
| 11 | Status | varchar(104) | No |
| 12 | CategoryName | varchar(50) | Yes |
| 13 | ApprovalDate | datetime | Yes |

#### vw_OverrideVendorBidders {view-dbo-vw-overridevendorbidders}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-10 12:01:54.417000 |
| **Modified** | 2026-03-05 15:32:54.130000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | Active | int | Yes |
| 3 | BidResultsId | int | No |
| 4 | BidPrice | decimal(34,13) | Yes |
| 5 | VendorName | varchar(69) | No |
| 6 | ItemBidType | varchar(13) | No |
| 7 | VendorItemCode | varchar(50) | Yes |
| 8 | Alternate | varchar(512) | Yes |
| 9 | VendorDescription | varchar(1497) | Yes |
| 10 | PageNumber | varchar(30) | No |
| 11 | UOM | varchar(16) | No |
| 12 | Original | varchar(18) | No |
| 13 | VOMId | int | Yes |
| 14 | Comments | varchar(1024) | No |
| 15 | SortKey | varchar(16) | Yes |

#### vw_PLBidItems {view-dbo-vw-plbiditems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-24 10:39:56.650000 |
| **Modified** | 2018-01-21 20:26:46.043000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | BidId | int | No |
| 4 | BidItemId | int | No |
| 5 | CrossRefId | int | Yes |
| 6 | AwardId | int | No |

#### vw_PLCatalog {view-dbo-vw-plcatalog}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-24 12:37:07.550000 |
| **Modified** | 2018-01-21 20:26:46 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | BidId | int | No |
| 4 | BidItemId | int | Yes |
| 5 | CrossRefId | int | No |
| 6 | AwardId | int | No |

#### vw_POHeaderBidImports {view-dbo-vw-poheaderbidimports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-12-03 16:34:59.860000 |
| **Modified** | 2023-02-20 14:48:36.010000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | Yes |
| 2 | BidImportId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | BidType | int | No |

#### vw_POStatus {view-dbo-vw-postatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-04-28 12:45:08.523000 |
| **Modified** | 2025-06-25 11:51:41.010000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | No |
| 2 | AwardsBidHeaderId | int | Yes |
| 3 | CategoryId | int | Yes |
| 4 | RequisitionId | int | No |
| 5 | SchoolId | int | No |
| 6 | VendorId | int | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Amount | money | Yes |
| 9 | Attention | varchar(50) | Yes |
| 10 | CategoryName | varchar(50) | Yes |
| 11 | ExportedToVendor | datetime | Yes |
| 12 | ItemCount | int | Yes |
| 13 | PONumber | varchar(24) | Yes |
| 14 | RequisitionNumber | varchar(24) | Yes |
| 15 | SchoolName | varchar(50) | Yes |
| 16 | POStatus | varchar(125) | Yes |
| 17 | VendorName | varchar(50) | Yes |
| 18 | CometId | int | Yes |

#### vw_POStatus_Test {view-dbo-vw-postatus-test}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-05-17 13:15:05.133000 |
| **Modified** | 2022-05-17 13:15:05.133000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | POId | int | No |
| 2 | AwardsBidHeaderId | int | Yes |
| 3 | CategoryId | int | Yes |
| 4 | RequisitionId | int | No |
| 5 | SchoolId | int | No |
| 6 | VendorId | int | Yes |
| 7 | AccountCode | varchar(50) | Yes |
| 8 | Amount | money | Yes |
| 9 | Attention | varchar(50) | Yes |
| 10 | CategoryName | varchar(50) | Yes |
| 11 | ExportedToVendor | datetime | Yes |
| 12 | ItemCount | int | Yes |
| 13 | PONumber | varchar(24) | Yes |
| 14 | RequisitionNumber | varchar(24) | Yes |
| 15 | SchoolName | varchar(50) | Yes |
| 16 | POStatus | varchar(125) | Yes |
| 17 | VendorName | varchar(50) | Yes |
| 18 | CometId | int | Yes |

#### vw_PendingDetailChangeNotifications {view-dbo-vw-pendingdetailchangenotifications}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-03-29 15:37:55.353000 |
| **Modified** | 2024-02-29 17:38:20.090000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailNotificationId | bigint | No |
| 2 | DetailId | bigint | No |
| 3 | NotificationId | bigint | Yes |
| 4 | DateCreated | datetime | No |
| 5 | OrigItemId | int | Yes |
| 6 | NewItemId | int | Yes |
| 7 | OrigVendorId | int | Yes |
| 8 | NewVendorId | int | Yes |
| 9 | OrigBidPrice | decimal(11,5) | Yes |
| 10 | NewBidPrice | decimal(11,5) | Yes |
| 11 | ReqUserId | int | Yes |
| 12 | ApprovalById | int | Yes |
| 13 | NotificationType | varchar(8) | No |
| 14 | Email | varchar(255) | No |

#### vw_PricePlanFilter {view-dbo-vw-priceplanfilter}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-31 12:18:31.993000 |
| **Modified** | 2018-01-21 20:26:48.257000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | PricePlanId | int | No |
| 2 | Code | varchar(20) | Yes |
| 3 | Description | varchar(255) | Yes |

#### vw_RTKContentCentralMSDS {view-dbo-vw-rtkcontentcentralmsds}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-07-03 14:21:08.350000 |
| **Modified** | 2018-01-21 20:26:46.280000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CatalogName | varchar(50) | Yes |
| 2 | DocumentType | varchar(50) | Yes |
| 3 | DocFolder | varchar(260) | Yes |
| 4 | DocName | varchar(260) | Yes |
| 5 | BaseName | varchar(260) | Yes |
| 6 | FullFileName | varchar(520) | Yes |
| 7 | VersionMajor | bigint | Yes |
| 8 | VersionMinor | bigint | Yes |
| 9 | CreatedUtc | datetime | No |
| 10 | PagesCaptured | int | Yes |
| 11 | DocId | uniqueidentifier | No |
| 12 | RevisionDate | datetime | Yes |
| 13 | CategoryName | varchar(50) | Yes |
| 14 | EDSItemCode | varchar(100) | Yes |
| 15 | ManufacturerName | varchar(100) | Yes |
| 16 | ProductName | varchar(100) | Yes |
| 17 | ManufacturerPartNumber | varchar(500) | Yes |
| 18 | EPARegistrationNumber | varchar(100) | Yes |
| 19 | SendTo | varchar(50) | Yes |
| 20 | AttachedRTKItems | int | Yes |

#### vw_RTKDefaultMSDSLocation {view-dbo-vw-rtkdefaultmsdslocation}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-06-05 23:08:24.453000 |
| **Modified** | 2018-01-21 20:26:48.337000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RTKLocation | varchar(50) | Yes |
| 2 | DistrictId | int | Yes |
| 3 | MSDSId | int | No |
| 4 | FacilityNumber | varchar(20) | Yes |

#### vw_RTKInfo {view-dbo-vw-rtkinfo}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-12-15 19:40:08.160000 |
| **Modified** | 2018-01-21 20:26:46.510000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Year | int | Yes |
| 2 | DistrictId | int | No |
| 3 | Name | varchar(50) | Yes |
| 4 | NJEIN | varchar(20) | Yes |
| 5 | FacilityId | varchar(1) | No |
| 6 | FacilityName | varchar(50) | Yes |
| 7 | CoMunCode | varchar(5) | Yes |
| 8 | ExposedEmployeesCount | int | Yes |
| 9 | FacilityEmergencyContact | varchar(100) | Yes |
| 10 | EmergencyPhone | varchar(50) | Yes |
| 11 | Location | varchar(406) | Yes |
| 12 | MailingAddress | varchar(406) | Yes |
| 13 | EmailResponsibleOfficial | varchar(200) | Yes |
| 14 | PhoneResponsibleOfficial | varchar(50) | Yes |
| 15 | TitleResponsibleOfficial | varchar(100) | Yes |
| 16 | AlternateDesc | varchar(60) | Yes |
| 17 | Manufacturer | varchar(50) | No |
| 18 | MSDSId | int | Yes |
| 19 | Quantity | int | Yes |
| 20 | InventoryCode | char(2) | Yes |
| 21 | InventoryDesc | varchar(25) | Yes |
| 22 | ProductLocation | varchar(50) | No |
| 23 | ProductExposedEmployees | int | Yes |
| 24 | Purpose | varchar(50) | Yes |
| 25 | RTK_PurposeID | int | Yes |
| 26 | UOMCode | char(1) | Yes |
| 27 | UOM | varchar(20) | Yes |
| 28 | SubstanceNo | char(4) | Yes |
| 29 | CASChemicalName | varchar(50) | Yes |
| 30 | CASRegNo | varchar(11) | No |
| 31 | DOT_Id | char(4) | Yes |
| 32 | MixturePercentCode | char(2) | Yes |
| 33 | MixtureDesc | varchar(12) | Yes |
| 34 | SpecHazCodes | varchar(36) | Yes |
| 35 | ContainerCode | char(2) | Yes |
| 36 | ContainerDesc | varchar(30) | Yes |
| 37 | CategoryId | int | Yes |

#### vw_RTKInfoAnnual {view-dbo-vw-rtkinfoannual}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-06-20 22:56:06.630000 |
| **Modified** | 2018-01-21 20:26:46.893000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Year | int | Yes |
| 2 | DistrictId | int | No |
| 3 | Name | varchar(50) | Yes |
| 4 | NJEIN | varchar(20) | Yes |
| 5 | FacilityId | varchar(1) | No |
| 6 | FacilityName | varchar(50) | Yes |
| 7 | CoMunCode | varchar(5) | Yes |
| 8 | ExposedEmployeesCount | int | Yes |
| 9 | FacilityEmergencyContact | varchar(100) | Yes |
| 10 | EmergencyPhone | varchar(50) | Yes |
| 11 | Location | varchar(406) | Yes |
| 12 | MailingAddress | varchar(406) | Yes |
| 13 | EmailResponsibleOfficial | varchar(200) | Yes |
| 14 | PhoneResponsibleOfficial | varchar(50) | Yes |
| 15 | TitleResponsibleOfficial | varchar(100) | Yes |
| 16 | AlternateDesc | varchar(60) | Yes |
| 17 | Manufacturer | varchar(50) | No |
| 18 | MSDSId | int | Yes |
| 19 | Quantity | int | Yes |
| 20 | InventoryCode | char(2) | Yes |
| 21 | InventoryDesc | varchar(25) | Yes |
| 22 | ProductLocation | varchar(50) | No |
| 23 | ProductExposedEmployees | int | Yes |
| 24 | Purpose | varchar(50) | Yes |
| 25 | RTK_PurposeID | int | Yes |
| 26 | UOMCode | char(1) | Yes |
| 27 | UOM | varchar(20) | Yes |
| 28 | SubstanceNo | char(4) | Yes |
| 29 | CASChemicalName | varchar(50) | Yes |
| 30 | CASRegNo | varchar(11) | No |
| 31 | DOT_Id | char(4) | Yes |
| 32 | MixturePercentCode | char(2) | Yes |
| 33 | MixtureDesc | varchar(12) | Yes |
| 34 | SpecHazCodes | varchar(36) | Yes |
| 35 | ContainerCode | char(2) | Yes |
| 36 | ContainerDesc | varchar(30) | Yes |
| 37 | CategoryId | int | Yes |

#### vw_RTKItems {view-dbo-vw-rtkitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-07-09 17:26:00.100000 |
| **Modified** | 2018-01-21 20:26:48.340000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | ItemCode | varchar(50) | No |
| 3 | ItemDescription | varchar(512) | No |
| 4 | RTK_ItemsId | int | No |
| 5 | CategoryId | int | Yes |
| 6 | ItemId | int | Yes |
| 7 | LegacyCometCode | varchar(16) | Yes |
| 8 | AlternateDesc | varchar(60) | Yes |
| 9 | CaseCount | int | Yes |
| 10 | MeasurePct | decimal(9,5) | Yes |
| 11 | ContainerCodesId | int | Yes |
| 12 | UOMCodesId | int | Yes |
| 13 | OtherContainerDesc | varchar(20) | Yes |
| 14 | LegacyCometDesc | varchar(60) | Yes |
| 15 | PurposeDesc | varchar(50) | No |
| 16 | RTK_PurposeId | int | Yes |
| 17 | Manufacturer | varchar(50) | Yes |

#### vw_RTKItems2 {view-dbo-vw-rtkitems2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-08-02 19:04:46.033000 |
| **Modified** | 2018-01-21 20:26:48.347000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | No |
| 2 | ItemCode | varchar(50) | No |
| 3 | LegacyCometCode | varchar(16) | No |
| 4 | ItemDescription | varchar(512) | No |
| 5 | AlternateDesc | varchar(60) | No |
| 6 | CaseCount | int | Yes |
| 7 | MeasurePct | decimal(9,5) | Yes |
| 8 | ContainerCode | char(2) | Yes |
| 9 | UOMCode | char(1) | Yes |
| 10 | ReportQty | int | Yes |
| 11 | RTK_ItemsId | int | No |
| 12 | ContainerCodesID | int | Yes |
| 13 | UOMCodesID | int | Yes |
| 14 | ItemId | int | Yes |
| 15 | CategoryId | int | Yes |
| 16 | PurposeDesc | varchar(50) | No |
| 17 | RTK_PurposeId | int | Yes |
| 18 | Manufacturer | varchar(50) | Yes |

#### vw_RTKItemsAnnual {view-dbo-vw-rtkitemsannual}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-06-20 22:55:56.423000 |
| **Modified** | 2018-01-21 20:26:46.887000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RTK_SitesId | int | Yes |
| 2 | Quantity | int | Yes |
| 3 | DistrictId | int | Yes |
| 4 | year | int | Yes |
| 5 | RTKDescription | varchar(60) | Yes |
| 6 | ExactLocationOnSite | varchar(50) | Yes |
| 7 | Manufacturer | varchar(50) | Yes |
| 8 | ContainerCodesId | int | Yes |
| 9 | RTK_PurposeId | int | Yes |
| 10 | UOMCodesId | int | Yes |
| 11 | MSDSId | int | Yes |
| 12 | CategoryId | int | Yes |

#### vw_RTKItemsRev2 {view-dbo-vw-rtkitemsrev2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-01-15 14:21:04.547000 |
| **Modified** | 2018-01-21 20:26:46.500000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RTK_SitesId | int | Yes |
| 2 | Quantity | int | Yes |
| 3 | DistrictId | int | Yes |
| 4 | year | int | Yes |
| 5 | RTKDescription | varchar(60) | Yes |
| 6 | ExactLocationOnSite | varchar(50) | Yes |
| 7 | Manufacturer | varchar(50) | Yes |
| 8 | ContainerCodesId | int | Yes |
| 9 | RTK_PurposeId | int | Yes |
| 10 | UOMCodesId | int | Yes |
| 11 | MSDSId | int | Yes |
| 12 | CategoryId | int | Yes |

#### vw_RTKReportItems {view-dbo-vw-rtkreportitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-08-07 19:45:27.407000 |
| **Modified** | 2018-01-21 20:26:48.350000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictName | varchar(50) | Yes |
| 2 | Year | int | Yes |
| 3 | SiteId | int | Yes |
| 4 | FacilityName | varchar(50) | Yes |
| 5 | CategoryName | varchar(50) | Yes |
| 6 | Quantity | int | Yes |
| 7 | ItemCode | varchar(50) | No |
| 8 | ItemDescription | varchar(512) | No |
| 9 | AlternateDesc | varchar(60) | No |
| 10 | ManuallyEntered | int | No |
| 11 | ManualEntryYesNo | varchar(3) | No |
| 12 | EDSItem | int | No |
| 13 | EDSItemYesNo | varchar(3) | No |
| 14 | RTK_ReportItemsId | int | No |
| 15 | RTK_ItemsId | int | No |
| 16 | RTK_SitesId | int | No |
| 17 | ItemId | int | No |
| 18 | CATEGORYID | int | Yes |
| 19 | DistrictId | int | Yes |
| 20 | MSDSId | int | Yes |
| 21 | ContentCentralMSDSDocId | varchar(36) | No |

#### vw_RTK_MSDSandCC {view-dbo-vw-rtk-msdsandcc}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-07-30 12:14:44.093000 |
| **Modified** | 2018-01-21 20:26:46.287000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Active | tinyint | Yes |
| 2 | RevisionDate | datetime | Yes |
| 3 | AlternateDescription | varchar(60) | Yes |
| 4 | EDSItemCode | varchar(100) | Yes |
| 5 | ManufacturerName | varchar(100) | Yes |
| 6 | ProductName | varchar(100) | Yes |
| 7 | ManufacturerPartNumber | varchar(500) | Yes |
| 8 | EPARegistrationNumber | varchar(100) | Yes |
| 9 | MSDSId | int | No |
| 10 | CurrentVersionMSDSId | int | Yes |
| 11 | ContentCentralMSDSDocId | varchar(36) | Yes |
| 12 | FullFileName | varchar(520) | Yes |
| 13 | DefaultVersion | int | No |

#### vw_RTK_Sites {view-dbo-vw-rtk-sites}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-06-12 11:16:36.243000 |
| **Modified** | 2018-01-21 20:26:48.330000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RTK_SitesId | int | No |
| 2 | DistrictId | int | No |
| 3 | DistrictName | varchar(50) | No |
| 4 | FacilityName | varchar(50) | No |
| 5 | NJEIN | varchar(20) | No |
| 6 | CoMunCode | varchar(5) | No |
| 7 | ChemicalInventoryStatus | tinyint | No |
| 8 | ExposedEmployeesCount | int | No |
| 9 | FacilityEmergencyContact | varchar(100) | No |
| 10 | EmergencyPhone | varchar(50) | No |
| 11 | FacilityLocation | varchar(408) | Yes |
| 12 | MailingAddress | varchar(408) | Yes |
| 13 | ResponsibleOfficial | varchar(100) | No |
| 14 | TitleResponsibleOfficial | varchar(100) | No |
| 15 | PhoneResponsibleOfficial | varchar(50) | No |
| 16 | EmailResponsibleOfficial | varchar(200) | No |
| 17 | RTKContact | varchar(174) | No |
| 18 | RTKEmail | varchar(255) | No |
| 19 | RTKPhone | varchar(20) | No |

#### vw_RefList {view-dbo-vw-reflist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-05-28 16:00:31.373000 |
| **Modified** | 2025-06-09 16:24:28.907000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictName | varchar(50) | Yes |
| 2 | Budgetname | varchar(30) | Yes |
| 3 | SchoolName | varchar(50) | Yes |
| 4 | CometId | int | Yes |
| 5 | Attention | varchar(50) | Yes |
| 6 | ItemCode | varchar(50) | Yes |
| 7 | VendorItemCode | varchar(50) | No |
| 8 | Quantity | int | Yes |
| 9 | BidPrice | money | Yes |
| 10 | description | varchar(1024) | Yes |
| 11 | ItemBidType | varchar(32) | No |
| 12 | Alternate | varchar(1024) | No |
| 13 | ReqStatus | varchar(255) | Yes |
| 14 | POId | int | No |
| 15 | PONumber | varchar(24) | No |
| 16 | ExportedToVendor | datetime | Yes |
| 17 | BidHeaderId | int | Yes |
| 18 | Category Name | varchar(50) | Yes |
| 19 | Account Code | varchar(50) | No |
| 20 | Account Balance | varchar(30) | Yes |
| 21 | BudgetId | int | No |
| 22 | DistrictId | int | No |
| 23 | RequisitionId | int | No |
| 24 | detailId | int | No |
| 25 | ItemId | int | Yes |
| 26 | CategoryId | int | Yes |
| 27 | UserId | int | No |
| 28 | BidItemId | int | Yes |
| 29 | VendorId | int | Yes |
| 30 | SortSeq | varchar(64) | Yes |
| 31 | LastYearsQuantity | int | Yes |
| 32 | ItemMustBeBid | int | No |
| 33 | RequisitionNumber | varchar(24) | Yes |
| 34 | UniqueItemNumber | varchar(50) | Yes |

#### vw_RepsDistricts {view-dbo-vw-repsdistricts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-12 21:09:27.513000 |
| **Modified** | 2018-01-21 20:26:48.260000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Active | tinyint | No |
| 2 | DistrictId | int | No |
| 3 | DistrictCode | varchar(4) | No |
| 4 | DistrictName | varchar(50) | No |
| 5 | BAName | varchar(50) | No |
| 6 | Phone | varchar(20) | No |
| 7 | Fax | varchar(20) | No |
| 8 | CSRepId | int | No |

#### vw_ReqBidReview {view-dbo-vw-reqbidreview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-05-05 14:41:29.767000 |
| **Modified** | 2018-01-21 20:26:48.267000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RSId | int | Yes |
| 2 | RepName | varchar(30) | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | SchoolName | varchar(50) | Yes |
| 5 | ShipName | varchar(50) | Yes |
| 6 | CometId | int | Yes |
| 7 | CategoryName | varchar(50) | Yes |
| 8 | BudgetName | varchar(30) | Yes |
| 9 | BidHeaderId | int | Yes |
| 10 | RequisitionNumber | varchar(24) | Yes |
| 11 | Attention | varchar(50) | Yes |
| 12 | TotalRequisitionCost | money | Yes |
| 13 | ItemCount | int | Yes |
| 14 | ItemCode | varchar(50) | Yes |
| 15 | Description | varchar(1024) | Yes |
| 16 | Quantity | int | Yes |
| 17 | BidPrice | money | Yes |
| 18 | UnitCode | varchar(20) | Yes |
| 19 | ItemStatus | varchar(65) | No |

#### vw_ReqCategories {view-dbo-vw-reqcategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-02-29 14:29:38.047000 |
| **Modified** | 2018-01-21 20:26:48.273000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | CategoryId | int | No |
| 3 | Name | varchar(50) | Yes |

#### vw_ReqDetail {view-dbo-vw-reqdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-03-19 10:23:02.903000 |
| **Modified** | 2025-09-18 15:12:45.940000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemId | int | Yes |
| 3 | ItemCode | varchar(50) | No |
| 4 | Quantity | int | No |
| 5 | LastYearsQuantity | int | No |
| 6 | Description | nvarchar(MAX) | Yes |
| 7 | LongDescription | nvarchar(MAX) | Yes |
| 8 | UnitCode | varchar(20) | No |
| 9 | BidPrice | money | No |
| 10 | Extended | money | No |
| 11 | LastAlteredSessionID | int | No |
| 12 | VendorName | varchar(50) | Yes |
| 13 | VendorCode | varchar(16) | No |
| 14 | CatalogName | varchar(50) | No |
| 15 | AltDescription | varchar(1024) | No |
| 16 | VendorItemCode | varchar(50) | Yes |
| 17 | CatalogPage | char(4) | Yes |
| 18 | NoBid | int | No |
| 19 | ItemMustBeBid | int | No |
| 20 | BidInfo | varchar(53) | Yes |
| 21 | HasBeenBid | int | No |
| 22 | AllowOverride | int | No |
| 23 | VendorOverridden | int | No |
| 24 | ItemBidType | varchar(32) | Yes |
| 25 | SortSeq | varchar(64) | Yes |
| 26 | RequisitionId | int | No |
| 27 | AddendumAdded | tinyint | No |
| 28 | MostPopular | int | No |
| 29 | TabSelection | varchar(7) | No |
| 30 | AddedFromAddenda | datetime | Yes |
| 31 | VendorID | int | Yes |
| 32 | UnitId | int | Yes |
| 33 | HeadingID | int | Yes |
| 34 | KeywordID | int | Yes |
| 35 | BrandName | varchar(50) | Yes |
| 36 | ManufacturerId | int | Yes |
| 37 | ManufacturorNumber | varchar(50) | Yes |
| 38 | VendorPartNumber | varchar(50) | Yes |
| 39 | ListPrice | money | Yes |
| 40 | ItemsPerUnit | varchar(50) | Yes |
| 41 | Items_VendorID | int | Yes |
| 42 | VendorToSupplyManufacturer | tinyint | Yes |
| 43 | ExtraDescription | varchar(1024) | Yes |
| 44 | DateAvailable | datetime | Yes |
| 45 | Modified | datetime | Yes |
| 46 | BidStatus | varchar(14) | No |
| 47 | BaseDescription | varchar(512) | No |
| 48 | SortKey | datetime | Yes |
| 49 | BidHeaderId | int | Yes |
| 50 | CatalogRefs | varchar(1) | No |
| 51 | BidderToSupplyVendor | tinyint | Yes |
| 52 | BidderToSupplyVendorPartNbr | tinyint | Yes |
| 53 | DistrictVendorCode | varchar(20) | No |
| 54 | VendorsAccountCode | varchar(50) | No |
| 55 | VendorBidInfo | varchar(576) | Yes |
| 56 | BidItemId | int | Yes |
| 57 | BelowMinimumItem | int | No |
| 58 | MinimumPOAmount | money | No |
| 59 | AdditionalShipping | tinyint | No |
| 60 | SDSAvail | int | Yes |
| 61 | ShortDescription | nvarchar(MAX) | Yes |
| 62 | ImageURL | varchar(1024) | Yes |
| 63 | ShippingCost | decimal(9,2) | Yes |
| 64 | ShippingUpdateRequired | int | No |
| 65 | DeliveryDate | nvarchar(4000) | Yes |
| 66 | PerishableItem | bit | Yes |
| 67 | DoctorsName | varchar(100) | Yes |
| 68 | DEANumber | varchar(9) | Yes |
| 69 | PrescriptionRequired | bit | Yes |
| 70 | DigitallyDelivered | tinyint | Yes |
| 71 | DigitallyDeliveredEmail | varchar(255) | Yes |
| 72 | MinimumOrderQuantity | int | Yes |
| 73 | CrossRefId | int | Yes |
| 74 | UserId | int | Yes |
| 75 | SchoolId | int | Yes |
| 76 | DistrictId | int | Yes |
| 77 | BudgetId | int | No |
| 78 | SDSURL | varchar(512) | Yes |
| 79 | ManufacturorNumberDetail | varchar(50) | Yes |
| 80 | BrandNameDetail | varchar(50) | Yes |
| 81 | OrderedYear | int | Yes |

#### vw_ReqDetail-removed 12082010 {view-dbo-vw-reqdetail-removed-12082010}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-12-08 15:05:51.160000 |
| **Modified** | 2018-01-21 20:26:46.490000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemId | int | Yes |
| 3 | ItemCode | varchar(50) | No |
| 4 | Quantity | int | No |
| 5 | LastYearsQuantity | int | No |
| 6 | Description | varchar(3650) | Yes |
| 7 | UnitCode | varchar(20) | No |
| 8 | BidPrice | money | No |
| 9 | Extended | money | No |
| 10 | SessionId | int | No |
| 11 | VendorName | varchar(50) | No |
| 12 | VendorCode | varchar(16) | No |
| 13 | CatalogName | varchar(50) | No |
| 14 | AltDescription | varchar(1024) | No |
| 15 | VendorItemCode | varchar(50) | No |
| 16 | CatalogPage | char(4) | Yes |
| 17 | NoBid | int | No |
| 18 | ItemMustBeBid | int | No |
| 19 | BidInfo | varchar(51) | Yes |
| 20 | HasBeenBid | int | No |
| 21 | AllowOverride | int | No |
| 22 | VendorOverridden | int | No |
| 23 | ItemBidType | varchar(32) | Yes |
| 24 | SortSeq | varchar(64) | Yes |
| 25 | RequisitionId | int | No |

#### vw_ReqDetail1 {view-dbo-vw-reqdetail1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-09-05 16:04:42.860000 |
| **Modified** | 2024-12-17 21:00:30.343000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemId | int | Yes |
| 3 | ItemCode | varchar(50) | No |
| 4 | Quantity | int | No |
| 5 | LastYearsQuantity | int | No |
| 6 | Description | nvarchar(MAX) | Yes |
| 7 | UnitCode | varchar(20) | No |
| 8 | BidPrice | money | No |
| 9 | Extended | money | No |
| 10 | SessionId | int | No |
| 11 | VendorName | varchar(50) | No |
| 12 | VendorCode | varchar(16) | No |
| 13 | CatalogName | varchar(50) | No |
| 14 | AltDescription | varchar(1024) | No |
| 15 | VendorItemCode | varchar(50) | Yes |
| 16 | CatalogPage | char(4) | Yes |
| 17 | NoBid | int | No |
| 18 | ItemMustBeBid | int | No |
| 19 | BidInfo | varchar(53) | Yes |
| 20 | HasBeenBid | int | No |
| 21 | AllowOverride | int | No |
| 22 | VendorOverridden | int | No |
| 23 | ItemBidType | varchar(32) | Yes |
| 24 | SortSeq | varchar(64) | Yes |
| 25 | RequisitionId | int | No |
| 26 | AddendumAdded | tinyint | No |
| 27 | MostPopular | int | No |
| 28 | TabSelection | varchar(7) | No |
| 29 | AddedFromAddenda | datetime | Yes |
| 30 | VendorID | int | Yes |
| 31 | UnitId | int | Yes |
| 32 | HeadingID | int | Yes |
| 33 | KeywordID | int | Yes |
| 34 | BrandName | varchar(50) | Yes |
| 35 | ManufacturorNumber | varchar(50) | Yes |
| 36 | VendorPartNumber | varchar(50) | Yes |
| 37 | ListPrice | money | Yes |
| 38 | ItemsPerUnit | varchar(50) | Yes |
| 39 | Items_VendorID | int | Yes |
| 40 | ExtraDescription | varchar(1024) | Yes |
| 41 | DateAvailable | datetime | Yes |
| 42 | BidStatus | varchar(14) | No |
| 43 | BaseDescription | varchar(512) | No |
| 44 | SortKey | datetime | Yes |
| 45 | UserId | int | Yes |
| 46 | SchoolId | int | Yes |
| 47 | DistrictId | int | Yes |
| 48 | PageList | varchar(8000) | Yes |

#### vw_ReqDetailAsp1 {view-dbo-vw-reqdetailasp1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-01-10 12:11:05.600000 |
| **Modified** | 2018-01-21 20:26:46.757000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | DetailId | int | No |
| 3 | ItemId | int | Yes |
| 4 | ItemCode | varchar(50) | No |
| 5 | Quantity | int | No |
| 6 | LastYearsQuantity | int | No |
| 7 | Description | varchar(4480) | Yes |
| 8 | UnitCode | varchar(20) | No |
| 9 | BidPrice | money | No |
| 10 | Extended | money | No |
| 11 | SessionId | int | No |
| 12 | VendorName | varchar(50) | No |
| 13 | VendorCode | varchar(16) | No |
| 14 | CatalogName | varchar(50) | No |
| 15 | AltDescription | varchar(1024) | No |
| 16 | VendorItemCode | varchar(50) | Yes |
| 17 | CatalogPage | char(4) | Yes |
| 18 | NoBid | int | No |
| 19 | ItemMustBeBid | int | No |
| 20 | BidInfo | varchar(51) | Yes |
| 21 | HasBeenBid | int | No |
| 22 | AllowOverride | int | No |
| 23 | VendorOverridden | int | No |
| 24 | ItemBidType | varchar(32) | Yes |
| 25 | SortSeq | varchar(64) | Yes |
| 26 | CatalogRefs | varchar(8000) | Yes |
| 27 | AllowDescriptionModify | int | No |

#### vw_ReqDetailPrint {view-dbo-vw-reqdetailprint}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-21 18:35:35.610000 |
| **Modified** | 2023-03-21 14:34:15.703000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Alternate | varchar(2050) | Yes |
| 2 | BidItemId | int | No |
| 3 | BidPrice | money | No |
| 4 | CatalogPage | char(4) | No |
| 5 | CatalogPrice | money | No |
| 6 | ShortDescription | varchar(1024) | No |
| 7 | ExtraDescription | varchar(1024) | No |
| 8 | ItemCode | varchar(50) | No |
| 9 | Quantity | int | No |
| 10 | RequisitionId | int | No |
| 11 | SortSeq | varchar(64) | No |
| 12 | UnitCode | varchar(20) | No |
| 13 | VendorItemCode | varchar(50) | No |
| 14 | ItemBidType | varchar(16) | No |
| 15 | ExtendedBidPrice | decimal(20,4) | Yes |
| 16 | AccountCode | varchar(50) | No |
| 17 | Attention | varchar(50) | No |
| 18 | DateEntered | datetime | No |
| 19 | RequisitionNumber | varchar(24) | No |
| 20 | ShippingCost | money | No |
| 21 | TotalItemsCost | money | No |
| 22 | TotalRequisitionCost | money | No |
| 23 | CategoryName | varchar(50) | Yes |
| 24 | BudgetName | varchar(30) | No |
| 25 | DistrictName | varchar(50) | No |
| 26 | DistrictCode | varchar(4) | No |
| 27 | ShipToName | varchar(50) | No |
| 28 | ShipToAddress1 | varchar(30) | No |
| 29 | ShipToAddress2 | varchar(30) | No |
| 30 | ShipToAddress3 | varchar(30) | No |
| 31 | ShipToCity | varchar(25) | No |
| 32 | ShipToState | varchar(2) | No |
| 33 | ShipToZipcode | varchar(10) | No |
| 34 | UserNumber | int | No |
| 35 | BidHeaderId | int | No |
| 36 | BidMsg | varchar(583) | Yes |
| 37 | FreeHandlingAmount | money | No |
| 38 | HandlingAmount | money | No |
| 39 | FreeHandlingStart | datetime | No |
| 40 | FreeHandlingEnd | datetime | No |
| 41 | VendorId | int | No |
| 42 | VendorCode | varchar(16) | No |
| 43 | VendorName | varchar(50) | No |
| 44 | VendorContactName | varchar(150) | No |
| 45 | VendorContactAddress1 | varchar(50) | No |
| 46 | VendorContactAddress2 | varchar(50) | No |
| 47 | VendorContactCity | varchar(50) | No |
| 48 | VendorContactState | char(2) | No |
| 49 | VendorContactZip | varchar(10) | No |
| 50 | VendorContactPhone | varchar(25) | No |
| 51 | VendorContactFax | varchar(20) | No |
| 52 | VendorContactEmail | varchar(255) | No |
| 53 | VendorBidNumber | varchar(50) | No |
| 54 | VendorAwardMsg | varchar(511) | No |
| 55 | DistrictVendorCode | varchar(20) | No |
| 56 | VendorsAccountCode | varchar(50) | No |
| 57 | FullDescription | varchar(8000) | Yes |
| 58 | FullVendorInfo | varchar(726) | Yes |
| 59 | FullDistrictInfo | varchar(420) | No |
| 60 | FullShipToInfo | varchar(315) | Yes |
| 61 | CompliantAlert | tinyint | No |
| 62 | SortKey | varchar(121) | Yes |
| 63 | SortVendorKey | varchar(51) | Yes |
| 64 | BidType | tinyint | No |
| 65 | PrintBidAs | tinyint | No |
| 66 | ItemsNotBid | int | No |
| 67 | BidsThisVendor | int | No |
| 68 | BelowMinimum | int | No |
| 69 | AdditionalShipping | int | Yes |

#### vw_ReqDetailPrintTest {view-dbo-vw-reqdetailprinttest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2023-07-14 16:08:50.873000 |
| **Modified** | 2023-07-28 12:37:54.633000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Alternate | varchar(2050) | Yes |
| 2 | BidItemId | int | No |
| 3 | BidPrice | money | No |
| 4 | CatalogPage | char(4) | No |
| 5 | CatalogPrice | money | No |
| 6 | ShortDescription | varchar(1024) | No |
| 7 | ExtraDescription | varchar(1024) | No |
| 8 | ItemCode | varchar(50) | No |
| 9 | Quantity | int | No |
| 10 | RequisitionId | int | No |
| 11 | SortSeq | varchar(64) | No |
| 12 | UnitCode | varchar(20) | No |
| 13 | VendorItemCode | varchar(50) | No |
| 14 | ItemBidType | varchar(16) | No |
| 15 | ExtendedBidPrice | decimal(20,4) | Yes |
| 16 | AccountCode | varchar(50) | No |
| 17 | Attention | varchar(50) | No |
| 18 | DateEntered | datetime | No |
| 19 | RequisitionNumber | varchar(24) | No |
| 20 | ShippingCost | money | No |
| 21 | TotalItemsCost | money | No |
| 22 | TotalRequisitionCost | money | No |
| 23 | CategoryName | varchar(50) | Yes |
| 24 | BudgetName | varchar(30) | No |
| 25 | DistrictName | varchar(50) | No |
| 26 | DistrictCode | varchar(4) | No |
| 27 | ShipToName | varchar(50) | No |
| 28 | ShipToAddress1 | varchar(30) | No |
| 29 | ShipToAddress2 | varchar(30) | No |
| 30 | ShipToAddress3 | varchar(30) | No |
| 31 | ShipToCity | varchar(25) | No |
| 32 | ShipToState | varchar(2) | No |
| 33 | ShipToZipcode | varchar(10) | No |
| 34 | UserNumber | int | No |
| 35 | BidHeaderId | int | No |
| 36 | BidMsg | varchar(583) | Yes |
| 37 | FreeHandlingAmount | money | No |
| 38 | HandlingAmount | money | No |
| 39 | FreeHandlingStart | datetime | No |
| 40 | FreeHandlingEnd | datetime | No |
| 41 | VendorId | int | No |
| 42 | VendorCode | varchar(16) | No |
| 43 | VendorName | varchar(50) | No |
| 44 | VendorContactName | varchar(150) | No |
| 45 | VendorContactAddress1 | varchar(50) | No |
| 46 | VendorContactAddress2 | varchar(50) | No |
| 47 | VendorContactCity | varchar(50) | No |
| 48 | VendorContactState | char(2) | No |
| 49 | VendorContactZip | varchar(10) | No |
| 50 | VendorContactPhone | varchar(25) | No |
| 51 | VendorContactFax | varchar(20) | No |
| 52 | VendorContactEmail | varchar(255) | No |
| 53 | VendorBidNumber | varchar(50) | No |
| 54 | VendorAwardMsg | varchar(511) | No |
| 55 | DistrictVendorCode | varchar(20) | No |
| 56 | VendorsAccountCode | varchar(50) | No |
| 57 | FullDescription | nvarchar(MAX) | Yes |
| 58 | FullVendorInfo | varchar(726) | Yes |
| 59 | FullDistrictInfo | varchar(420) | No |
| 60 | FullShipToInfo | varchar(315) | Yes |
| 61 | CompliantAlert | tinyint | No |
| 62 | SortKey | varchar(121) | Yes |
| 63 | SortVendorKey | varchar(51) | Yes |
| 64 | BidType | tinyint | No |
| 65 | PrintBidAs | tinyint | No |
| 66 | ItemsNotBid | int | No |
| 67 | BidsThisVendor | int | No |
| 68 | BelowMinimum | int | No |
| 69 | AdditionalShipping | int | Yes |

#### vw_ReqDetailSummary {view-dbo-vw-reqdetailsummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-26 13:00:19.947000 |
| **Modified** | 2022-04-28 12:45:31.443000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionNumber | varchar(24) | No |
| 2 | DateEntered | datetime | No |
| 3 | TotalRequisitionCost | money | No |
| 4 | TotalItemsCost | money | No |
| 5 | ShippingCost | money | No |
| 6 | CategoryName | varchar(50) | No |
| 7 | AccountCode | varchar(50) | No |
| 8 | BudgetName | varchar(30) | No |
| 9 | BidHeaderId | int | No |
| 10 | BidMsg | varchar(583) | Yes |
| 11 | FreeHandlingStart | datetime | No |
| 12 | FreeHandlingEnd | datetime | No |
| 13 | FreeHandlingAmount | money | No |
| 14 | HandlingAmount | money | No |
| 15 | RequisitionId | int | No |
| 16 | VendorId | int | No |
| 17 | VendorCode | varchar(16) | No |
| 18 | VendorName | varchar(50) | No |
| 19 | VendorBidNumber | varchar(50) | No |
| 20 | DistrictVendorCode | varchar(20) | No |
| 21 | VendorsAccountCode | varchar(50) | No |
| 22 | FullDistrictInfo | varchar(420) | No |
| 23 | FullShipToInfo | varchar(315) | Yes |
| 24 | Lines | int | Yes |
| 25 | TotalQuantity | int | Yes |
| 26 | TotalBidCost | decimal(38,4) | Yes |
| 27 | BidsThisVendor | int | No |
| 28 | SortVendorKey | varchar(51) | Yes |
| 29 | AdditionalShippingItems | int | Yes |

#### vw_ReqDetailTab {view-dbo-vw-reqdetailtab}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-11-18 12:49:46.783000 |
| **Modified** | 2018-01-21 20:26:48.277000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | RequisitionId | int | Yes |
| 3 | Quantity | int | Yes |
| 4 | BidPrice | money | Yes |
| 5 | TabSelection | varchar(7) | No |

#### vw_ReqDetail_BK20241205 {view-dbo-vw-reqdetail-bk20241205}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2024-12-04 23:59:22.237000 |
| **Modified** | 2024-12-04 23:59:22.237000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemId | int | Yes |
| 3 | ItemCode | varchar(50) | No |
| 4 | Quantity | int | No |
| 5 | LastYearsQuantity | int | No |
| 6 | Description | nvarchar(MAX) | Yes |
| 7 | LongDescription | nvarchar(MAX) | Yes |
| 8 | UnitCode | varchar(20) | No |
| 9 | BidPrice | money | No |
| 10 | Extended | money | No |
| 11 | LastAlteredSessionID | int | No |
| 12 | VendorName | varchar(50) | Yes |
| 13 | VendorCode | varchar(16) | No |
| 14 | CatalogName | varchar(50) | No |
| 15 | AltDescription | varchar(1024) | No |
| 16 | VendorItemCode | varchar(50) | Yes |
| 17 | CatalogPage | char(4) | Yes |
| 18 | NoBid | int | No |
| 19 | ItemMustBeBid | int | No |
| 20 | BidInfo | varchar(53) | Yes |
| 21 | HasBeenBid | int | No |
| 22 | AllowOverride | int | No |
| 23 | VendorOverridden | int | No |
| 24 | ItemBidType | varchar(32) | Yes |
| 25 | SortSeq | varchar(64) | Yes |
| 26 | RequisitionId | int | No |
| 27 | AddendumAdded | tinyint | No |
| 28 | MostPopular | int | No |
| 29 | TabSelection | varchar(7) | No |
| 30 | AddedFromAddenda | datetime | Yes |
| 31 | VendorID | int | Yes |
| 32 | UnitId | int | Yes |
| 33 | HeadingID | int | Yes |
| 34 | KeywordID | int | Yes |
| 35 | BrandName | varchar(50) | Yes |
| 36 | ManufacturerId | int | Yes |
| 37 | ManufacturorNumber | varchar(50) | Yes |
| 38 | VendorPartNumber | varchar(50) | Yes |
| 39 | ListPrice | money | Yes |
| 40 | ItemsPerUnit | varchar(50) | Yes |
| 41 | Items_VendorID | int | Yes |
| 42 | VendorToSupplyManufacturer | tinyint | Yes |
| 43 | ExtraDescription | varchar(1024) | Yes |
| 44 | DateAvailable | datetime | Yes |
| 45 | Modified | datetime | Yes |
| 46 | BidStatus | varchar(14) | No |
| 47 | BaseDescription | varchar(512) | No |
| 48 | SortKey | datetime | Yes |
| 49 | BidHeaderId | int | Yes |
| 50 | CatalogRefs | varchar(1) | No |
| 51 | BidderToSupplyVendor | tinyint | Yes |
| 52 | BidderToSupplyVendorPartNbr | tinyint | Yes |
| 53 | DistrictVendorCode | varchar(20) | No |
| 54 | VendorsAccountCode | varchar(50) | No |
| 55 | VendorBidInfo | varchar(576) | Yes |
| 56 | BidItemId | int | Yes |
| 57 | BelowMinimumItem | int | No |
| 58 | MinimumPOAmount | money | No |
| 59 | AdditionalShipping | tinyint | No |
| 60 | SDSAvail | int | Yes |
| 61 | ShortDescription | nvarchar(MAX) | Yes |
| 62 | ImageURL | varchar(1024) | Yes |
| 63 | ShippingCost | decimal(9,2) | Yes |
| 64 | ShippingUpdateRequired | int | No |
| 65 | DeliveryDate | nvarchar(4000) | Yes |
| 66 | PerishableItem | bit | Yes |
| 67 | DoctorsName | varchar(100) | Yes |
| 68 | DEANumber | varchar(9) | Yes |
| 69 | PrescriptionRequired | bit | Yes |

#### vw_ReqDetail_BK20241227 {view-dbo-vw-reqdetail-bk20241227}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2024-12-27 01:48:35.660000 |
| **Modified** | 2024-12-27 01:48:35.660000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DetailId | int | No |
| 2 | ItemId | int | Yes |
| 3 | ItemCode | varchar(50) | No |
| 4 | Quantity | int | No |
| 5 | LastYearsQuantity | int | No |
| 6 | Description | nvarchar(MAX) | Yes |
| 7 | LongDescription | nvarchar(MAX) | Yes |
| 8 | UnitCode | varchar(20) | No |
| 9 | BidPrice | money | No |
| 10 | Extended | money | No |
| 11 | LastAlteredSessionID | int | No |
| 12 | VendorName | varchar(50) | Yes |
| 13 | VendorCode | varchar(16) | No |
| 14 | CatalogName | varchar(50) | No |
| 15 | AltDescription | varchar(1024) | No |
| 16 | VendorItemCode | varchar(50) | Yes |
| 17 | CatalogPage | char(4) | Yes |
| 18 | NoBid | int | No |
| 19 | ItemMustBeBid | int | No |
| 20 | BidInfo | varchar(53) | Yes |
| 21 | HasBeenBid | int | No |
| 22 | AllowOverride | int | No |
| 23 | VendorOverridden | int | No |
| 24 | ItemBidType | varchar(32) | Yes |
| 25 | SortSeq | varchar(64) | Yes |
| 26 | RequisitionId | int | No |
| 27 | AddendumAdded | tinyint | No |
| 28 | MostPopular | int | No |
| 29 | TabSelection | varchar(7) | No |
| 30 | AddedFromAddenda | datetime | Yes |
| 31 | VendorID | int | Yes |
| 32 | UnitId | int | Yes |
| 33 | HeadingID | int | Yes |
| 34 | KeywordID | int | Yes |
| 35 | BrandName | varchar(50) | Yes |
| 36 | ManufacturerId | int | Yes |
| 37 | ManufacturorNumber | varchar(50) | Yes |
| 38 | VendorPartNumber | varchar(50) | Yes |
| 39 | ListPrice | money | Yes |
| 40 | ItemsPerUnit | varchar(50) | Yes |
| 41 | Items_VendorID | int | Yes |
| 42 | VendorToSupplyManufacturer | tinyint | Yes |
| 43 | ExtraDescription | varchar(1024) | Yes |
| 44 | DateAvailable | datetime | Yes |
| 45 | Modified | datetime | Yes |
| 46 | BidStatus | varchar(14) | No |
| 47 | BaseDescription | varchar(512) | No |
| 48 | SortKey | datetime | Yes |
| 49 | BidHeaderId | int | Yes |
| 50 | CatalogRefs | varchar(1) | No |
| 51 | BidderToSupplyVendor | tinyint | Yes |
| 52 | BidderToSupplyVendorPartNbr | tinyint | Yes |
| 53 | DistrictVendorCode | varchar(20) | No |
| 54 | VendorsAccountCode | varchar(50) | No |
| 55 | VendorBidInfo | varchar(576) | Yes |
| 56 | BidItemId | int | Yes |
| 57 | BelowMinimumItem | int | No |
| 58 | MinimumPOAmount | money | No |
| 59 | AdditionalShipping | tinyint | No |
| 60 | SDSAvail | int | Yes |
| 61 | ShortDescription | nvarchar(MAX) | Yes |
| 62 | ImageURL | varchar(1024) | Yes |
| 63 | ShippingCost | decimal(9,2) | Yes |
| 64 | ShippingUpdateRequired | int | No |
| 65 | DeliveryDate | nvarchar(4000) | Yes |
| 66 | PerishableItem | bit | Yes |
| 67 | DoctorsName | varchar(100) | Yes |
| 68 | DEANumber | varchar(9) | Yes |
| 69 | PrescriptionRequired | bit | Yes |
| 70 | DigitallyDelivered | tinyint | Yes |
| 71 | DigitallyDeliveredEmail | varchar(255) | Yes |
| 72 | UserId | int | Yes |
| 73 | SchoolId | int | Yes |
| 74 | DistrictId | int | Yes |
| 75 | SDS_URL | varchar(300) | Yes |
| 76 | ManufacturorNumberDetail | varchar(50) | Yes |
| 77 | BrandNameDetail | varchar(50) | Yes |
| 78 | OrderedYear | int | Yes |

#### vw_ReqTotalsByVendor {view-dbo-vw-reqtotalsbyvendor}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-11 16:15:32.290000 |
| **Modified** | 2026-03-04 12:53:17.093000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | AdditionalHandlingAmount | money | No |
| 5 | FreeHandlingAmount | money | No |
| 6 | FreeHandlingStart | datetime | Yes |
| 7 | FreeHandlingEnd | datetime | Yes |
| 8 | HandlingAmount | money | No |
| 9 | VendorTotal | decimal(38,2) | Yes |
| 10 | ItemsTotal | money | Yes |
| 11 | POBelowMinimum | int | No |
| 12 | MinimumPOAmount | money | No |
| 13 | AdditionalShipping | tinyint | Yes |
| 14 | TotalShippingCost | decimal(38,2) | Yes |
| 15 | UpdateRequired | int | Yes |

#### vw_ReqTotalsByVendorTest {view-dbo-vw-reqtotalsbyvendortest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-02-13 11:30:18.203000 |
| **Modified** | 2018-01-21 20:26:46.697000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | AdditionalHandlingAmount | money | No |
| 5 | FreeHandlingAmount | money | No |
| 6 | FreeHandlingStart | datetime | Yes |
| 7 | FreeHandlingEnd | datetime | Yes |
| 8 | HandlingAmount | money | No |
| 9 | VendorTotal | money | Yes |
| 10 | ItemsTotal | money | Yes |

#### vw_ReqTotalsByVendor_TEST {view-dbo-vw-reqtotalsbyvendor-test}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2026-03-04 12:51:30.500000 |
| **Modified** | 2026-03-04 12:51:30.500000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | AdditionalHandlingAmount | money | No |
| 5 | FreeHandlingAmount | money | No |
| 6 | FreeHandlingStart | datetime | Yes |
| 7 | FreeHandlingEnd | datetime | Yes |
| 8 | HandlingAmount | money | No |
| 9 | VendorTotal | decimal(38,2) | Yes |
| 10 | ItemsTotal | money | Yes |
| 11 | POBelowMinimum | int | No |
| 12 | MinimumPOAmount | money | No |
| 13 | AdditionalShipping | tinyint | Yes |
| 14 | TotalShippingCost | decimal(38,2) | Yes |
| 15 | UpdateRequired | int | Yes |

#### vw_ReqVendors {view-dbo-vw-reqvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-11 21:40:20.327000 |
| **Modified** | 2019-01-15 10:13:44.510000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | Yes |
| 4 | WebURL | varchar(255) | Yes |

#### vw_Reqs_Assoc_With_Bid {view-dbo-vw-reqs-assoc-with-bid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-08-30 13:21:05.580000 |
| **Modified** | 2022-07-28 14:43:49.123000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | DistrictId | int | No |
| 3 | RequisitionId | int | No |
| 4 | ApprovalsStatusId | int | No |
| 5 | WaitingBidReadyFlag | int | No |

#### vw_RequisitionAccountBalance {view-dbo-vw-requisitionaccountbalance}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-09-27 07:29:42.163000 |
| **Modified** | 2019-11-07 09:11:01.620000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | AccountCode | varchar(50) | Yes |
| 3 | UseAllocations | int | No |
| 4 | AmountAvailable | varchar(30) | Yes |

#### vw_RequisitionCatalogList {view-dbo-vw-requisitioncataloglist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 20:53:05.003000 |
| **Modified** | 2018-01-21 20:26:48.287000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | CatalogId | int | No |
| 3 | Name | varchar(50) | Yes |

#### vw_RequisitionIsVisible {view-dbo-vw-requisitionisvisible}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-21 10:55:45.013000 |
| **Modified** | 2018-01-21 20:26:45.847000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | RequisitionId | int | No |
| 3 | IsVisible | int | Yes |

#### vw_RequisitionList {view-dbo-vw-requisitionlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-21 11:09:19.807000 |
| **Modified** | 2018-01-21 20:26:45.857000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Tagged | int | No |
| 2 | SessionId | int | No |
| 3 | SchoolId | int | Yes |
| 4 | UserId | int | Yes |
| 5 | RequisitionId | int | No |
| 6 | BudgetId | int | Yes |
| 7 | AccountId | int | Yes |
| 8 | CategoryId | int | Yes |
| 9 | TotalRequisitionCost | money | No |
| 10 | ApprovalLevel | tinyint | No |
| 11 | StatusId | int | Yes |
| 12 | LastApprovalId | int | No |
| 13 | NextApproverId | int | No |
| 14 | LastApproverId | int | No |
| 15 | RequisitionNumber | varchar(24) | Yes |
| 16 | AccountCode | varchar(50) | Yes |
| 17 | SchoolName | varchar(50) | Yes |
| 18 | CategoryName | varchar(50) | Yes |
| 19 | Attention | varchar(50) | Yes |
| 20 | CometId | varchar(5) | Yes |
| 21 | DateEntered | datetime | Yes |
| 22 | OrderDate | datetime | Yes |
| 23 | POCreated | int | No |
| 24 | BidInfo | varchar(51) | Yes |
| 25 | Status | varchar(104) | No |

#### vw_RequisitionShippingCosts {view-dbo-vw-requisitionshippingcosts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-14 12:06:36.210000 |
| **Modified** | 2026-03-04 12:33:19.417000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | BidHeaderId | int | Yes |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | Yes |
| 5 | Extended | money | Yes |
| 6 | ShippingCost | money | No |
| 7 | FreeHandlingAmount | money | No |
| 8 | FreeHandlingStart | datetime | Yes |
| 9 | FreeHandlingEnd | datetime | Yes |
| 10 | AdditionalHandlingAmount | money | No |
| 11 | POBelowMinimum | int | No |
| 12 | MinimumPOAmount | money | No |
| 13 | AdditionalShipping | tinyint | Yes |
| 14 | DistrictVendorCode | varchar(20) | No |
| 15 | VendorBidInfo | varchar(576) | No |
| 16 | TotalShippingCost | decimal(38,2) | Yes |
| 17 | UpdateRequired | int | Yes |

#### vw_RequisitionShippingCostsTest {view-dbo-vw-requisitionshippingcoststest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-06-05 14:02:19.137000 |
| **Modified** | 2018-06-05 14:02:19.137000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | VendorId | int | No |
| 4 | VendorName | varchar(50) | Yes |
| 5 | Extended | money | Yes |
| 6 | ShippingCost | money | No |
| 7 | FreeHandlingAmount | money | No |
| 8 | FreeHandlingStart | datetime | Yes |
| 9 | FreeHandlingEnd | datetime | Yes |
| 10 | AdditionalHandlingAmount | money | No |
| 11 | POBelowMinimum | int | No |
| 12 | MinimumPOAmount | money | No |
| 13 | AdditionalShipping | tinyint | Yes |
| 14 | DistrictVendorCode | varchar(20) | No |
| 15 | VendorBidInfo | varchar(576) | No |

#### vw_RequisitionStatus {view-dbo-vw-requisitionstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-02-10 13:09:56.977000 |
| **Modified** | 2018-01-21 20:26:46.520000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | StatusId | int | No |
| 3 | StatusDesc | varchar(104) | No |
| 4 | StatusCode | int | No |
| 5 | ApprovalDate | datetime | Yes |
| 6 | BidStatus | varchar(20) | No |
| 7 | BaseStatus | varchar(50) | No |

#### vw_RequisitionStatusBySession {view-dbo-vw-requisitionstatusbysession}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-03 11:46:20.747000 |
| **Modified** | 2021-09-01 14:57:43.180000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | SessionId | int | No |
| 3 | StatusId | int | No |
| 4 | StatusDesc | varchar(104) | No |
| 5 | StatusCode | int | No |
| 6 | ApprovalDate | datetime | Yes |
| 7 | BidStatus | varchar(20) | No |
| 8 | BaseStatus | varchar(50) | No |

#### vw_RequisitionStatus_orig {view-dbo-vw-requisitionstatus-orig}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-09-13 15:16:10.420000 |
| **Modified** | 2018-01-21 20:26:48.320000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | StatusId | int | No |
| 3 | StatusDesc | varchar(104) | No |
| 4 | StatusCode | int | No |
| 5 | ApprovalDate | datetime | Yes |
| 6 | BidStatus | varchar(20) | No |

#### vw_Requisitions {view-dbo-vw-requisitions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-02 16:40:48.343000 |
| **Modified** | 2022-04-21 08:43:40.657000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | RequisitionNumber | varchar(24) | Yes |
| 4 | SchoolId | int | Yes |
| 5 | UserId | int | Yes |
| 6 | BudgetId | int | Yes |
| 7 | BudgetAccountId | int | Yes |
| 8 | UserAccountId | int | Yes |
| 9 | CategoryId | int | Yes |
| 10 | ShippingId | int | Yes |
| 11 | Attention | varchar(50) | Yes |
| 12 | AccountCode | varchar(50) | Yes |
| 13 | DateEntered | datetime | Yes |
| 14 | ShippingPercent | decimal(9,5) | Yes |
| 15 | DiscountPercent | decimal(9,5) | Yes |
| 16 | ShippingCost | money | Yes |
| 17 | TotalItemsCost | money | Yes |
| 18 | TotalRequisitionCost | money | Yes |
| 19 | Comments | varchar(1023) | Yes |
| 20 | ApprovalRequired | tinyint | Yes |
| 21 | ApprovalId | int | Yes |
| 22 | ApprovalLevel | tinyint | Yes |
| 23 | StatusId | int | Yes |
| 24 | OrderDate | datetime | Yes |
| 25 | DateExported | datetime | Yes |
| 26 | BidId | int | Yes |
| 27 | BookId | int | Yes |
| 28 | SourceId | int | Yes |
| 29 | BidHeaderId | int | Yes |
| 30 | LastAlteredSessionId | int | Yes |
| 31 | DateUpdated | datetime | Yes |
| 32 | OrderType | tinyint | Yes |
| 33 | NotesCount | int | Yes |
| 34 | AddendaTotal | money | Yes |
| 35 | ApprovalCount | int | Yes |
| 36 | AdditionalShipping | int | Yes |
| 37 | ShippingUpdateRequired | int | Yes |
| 38 | AdditionalShippingCost | decimal(38,2) | Yes |
| 39 | AllowRequestAddenda | tinyint | No |
| 40 | CSAllowRequestAddenda | tinyint | No |

#### vw_RequisitionsAccounts {view-dbo-vw-requisitionsaccounts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-27 11:40:15.863000 |
| **Modified** | 2018-01-21 20:26:48.300000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | BudgetId | int | Yes |
| 3 | UserId | int | Yes |
| 4 | UserAccountId | int | No |
| 5 | BudgetAccountId | int | Yes |
| 6 | Code | varchar(77) | Yes |

#### vw_RequisitionsCategories {view-dbo-vw-requisitionscategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-27 11:18:36.820000 |
| **Modified** | 2018-01-21 20:26:48.303000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | CategoryId | int | No |
| 3 | Name | varchar(69) | Yes |

#### vw_RequisitionsPrint {view-dbo-vw-requisitionsprint}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-02-04 13:30:47.197000 |
| **Modified** | 2018-01-21 20:26:48.310000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | RequisitionNumber | varchar(24) | No |
| 3 | Attention | varchar(50) | No |
| 4 | ItemsNotBid | int | No |

#### vw_RequisitionsShippingLocations {view-dbo-vw-requisitionsshippinglocations}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-27 11:42:43.777000 |
| **Modified** | 2018-01-21 20:26:48.310000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Requisitionid | int | No |
| 2 | ShippingId | int | No |
| 3 | Name | varchar(50) | Yes |

#### vw_RptExpireDateBidDocs {view-dbo-vw-rptexpiredatebiddocs}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2021-09-21 10:41:19.570000 |
| **Modified** | 2025-10-27 20:09:57.553000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorName | varchar(50) | Yes |
| 3 | VendorCode | varchar(16) | No |
| 4 | DocumentName | varchar(50) | Yes |
| 5 | ExpirationDatePerDMS | varchar(10) | Yes |
| 6 | ExpirationDatePerDocUpload | varchar(10) | Yes |
| 7 | DocUploadStatus | char(1) | No |
| 8 | ExpirationDateStatus | varchar(46) | Yes |
| 9 | StatusCode | int | Yes |
| 10 | EffectiveFrom | date | Yes |
| 11 | EffectiveUntil | date | Yes |
| 12 | DocumentUploadId | int | Yes |
| 13 | DMSId | uniqueidentifier | Yes |

#### vw_RptExpireDateBidDocsAndMore {view-dbo-vw-rptexpiredatebiddocsandmore}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2021-09-21 10:43:43.820000 |
| **Modified** | 2021-09-21 10:43:43.820000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorName | varchar(50) | No |
| 3 | VendorCode | varchar(16) | No |
| 4 | DocumentName | varchar(50) | Yes |
| 5 | ExpirationDatePerDMS | varchar(10) | Yes |
| 6 | ExpirationDatePerDocUpload | varchar(10) | Yes |
| 7 | DocUploadStatus | char(1) | No |
| 8 | ExpirationDateStatus | varchar(46) | Yes |
| 9 | StatusCode | int | Yes |
| 10 | EffectiveFrom | date | Yes |
| 11 | EffectiveUntil | date | Yes |
| 12 | DocInOtherBid | varchar(10) | No |
| 13 | ExpirationDatePerOtherBid | varchar(10) | No |
| 14 | DocumentUploadId | int | Yes |
| 15 | DMSId | uniqueidentifier | Yes |

#### vw_RptMarkedReadyEmailBlastStats {view-dbo-vw-rptmarkedreadyemailblaststats}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2021-09-28 16:08:36.080000 |
| **Modified** | 2021-09-28 16:08:36.080000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | varchar(50) | Yes |
| 2 | BidHeaderId | int | Yes |
| 3 | DistrictName | varchar(50) | Yes |
| 4 | DistrictCode | varchar(4) | Yes |
| 5 | RepName | varchar(30) | Yes |
| 6 | BlastSent | varchar(10) | Yes |
| 7 | NotifyByEmail | varchar(5) | Yes |
| 8 | AssocReqsAll | int | Yes |
| 9 | AssocReqsWtgForBidReady | int | Yes |
| 10 | AssocUsers | int | Yes |
| 11 | Approvers | int | Yes |

#### vw_RptMissingURLsByBidAndVendor {view-dbo-vw-rptmissingurlsbybidandvendor}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2023-01-16 15:18:29.253000 |
| **Modified** | 2023-01-16 15:18:29.253000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | bidheaderid | int | Yes |
| 2 | VendorId | int | Yes |
| 3 | Vendor Code | varchar(16) | No |
| 4 | Awarded Vendor Name | varchar(50) | No |
| 5 | AwardedItems | int | Yes |
| 6 | MissingURLs | int | Yes |

#### vw_SDSImportView {view-dbo-vw-sdsimportview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-08-18 13:14:45.980000 |
| **Modified** | 2018-07-11 20:48:51.720000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | MSDSId | int | No |
| 2 | MSDSRef | varchar(255) | Yes |
| 3 | ItemDescription | varchar(512) | Yes |
| 4 | ItemList | varchar(MAX) | Yes |
| 5 | Manufacturer | varchar(MAX) | Yes |
| 6 | ManufacturerPartNumber | varchar(MAX) | Yes |

#### vw_SDSItems {view-dbo-vw-sdsitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2018-07-11 12:30:39.140000 |
| **Modified** | 2025-02-07 17:40:14.373000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | Yes |
| 2 | MSDSId | int | Yes |
| 3 | DocId | uniqueidentifier | No |
| 4 | SDSURL | varchar(99) | Yes |

#### vw_SDSItemsAll {view-dbo-vw-sdsitemsall}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2024-12-10 14:39:29.647000 |
| **Modified** | 2024-12-10 14:39:29.647000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SafetyDataSheetId | bigint | No |
| 2 | SDSURL | varchar(512) | No |

#### vw_SDSReferencedURLs {view-dbo-vw-sdsreferencedurls}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2020-06-16 16:11:47.967000 |
| **Modified** | 2020-06-16 16:11:47.967000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | Yes |
| 2 | CrossRefId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | SDS_URL | varchar(300) | Yes |
| 5 | Manufacturer | varchar(50) | Yes |

#### vw_Savings1 {view-dbo-vw-savings1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-02-05 20:06:51.123000 |
| **Modified** | 2018-01-21 20:26:48.357000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | BudgetName | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | CYDollars | varchar(30) | Yes |
| 6 | CYIncludedDollars | varchar(30) | Yes |
| 7 | CYIncludedPercent | int | Yes |
| 8 | CYExcludedDollars | varchar(30) | Yes |
| 9 | GTDollars | varchar(30) | Yes |
| 10 | GTYears | int | No |
| 11 | PricePlanCode | varchar(20) | Yes |
| 12 | County | varchar(50) | No |
| 13 | State | char(2) | No |
| 14 | TotalBidCost | money | Yes |
| 15 | TotalCatalogCost | numeric(38,6) | Yes |
| 16 | TotalStateContractCost | numeric(38,6) | Yes |
| 17 | StateContractDiscount | decimal(13,9) | Yes |
| 18 | OverallDiscount | numeric(38,6) | Yes |
| 19 | OverallSavings | numeric(38,6) | Yes |
| 20 | IncludedBidCost | money | Yes |
| 21 | IncludedCatalogCost | numeric(38,6) | Yes |
| 22 | IncludedDiscount | numeric(38,6) | Yes |
| 23 | IncludedSavings | numeric(38,6) | Yes |
| 24 | ExcludedBidCost | money | Yes |
| 25 | ExcludedCatalogCost | numeric(38,6) | Yes |
| 26 | ExcludedDiscount | numeric(38,6) | Yes |
| 27 | ExcludedSavings | numeric(38,6) | Yes |

#### vw_Savings5 {view-dbo-vw-savings5}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-01-20 11:46:33.753000 |
| **Modified** | 2018-01-21 20:26:48.363000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | BudgetName | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | CYDollars | varchar(30) | Yes |
| 6 | CYIncludedDollars | varchar(30) | Yes |
| 7 | CYIncludedPercent | int | Yes |
| 8 | CYExcludedDollars | varchar(30) | Yes |
| 9 | GTDollars | varchar(30) | Yes |
| 10 | GTYears | int | No |
| 11 | PricePlanCode | varchar(20) | Yes |
| 12 | County | varchar(50) | No |
| 13 | State | char(2) | No |

#### vw_SavingsDetail1 {view-dbo-vw-savingsdetail1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-28 22:54:58.447000 |
| **Modified** | 2026-01-07 16:04:01.907000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | DistrictId | int | No |
| 3 | CategoryId | int | No |
| 4 | OnSavingsReport | int | No |
| 5 | DistrictName | varchar(189) | Yes |
| 6 | CategoryName | varchar(50) | Yes |
| 7 | ItemCode | varchar(50) | Yes |
| 8 | Quantity | int | Yes |
| 9 | BidPrice | money | Yes |
| 10 | CatalogPrice | numeric(22,6) | Yes |
| 11 | Discount | numeric(38,17) | Yes |
| 12 | BidExtended | money | Yes |
| 13 | CatalogExtended | numeric(33,6) | Yes |
| 14 | StateContractCost | numeric(38,6) | Yes |
| 15 | StateContractDiscount | decimal(13,9) | Yes |

#### vw_SavingsDetail1NonFiltered {view-dbo-vw-savingsdetail1nonfiltered}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-16 13:23:09.043000 |
| **Modified** | 2018-01-21 20:26:46.243000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | DistrictId | int | No |
| 3 | CategoryId | int | No |
| 4 | OnSavingsReport | int | No |
| 5 | DistrictName | varchar(189) | Yes |
| 6 | CategoryName | varchar(50) | Yes |
| 7 | ItemCode | varchar(50) | Yes |
| 8 | Quantity | int | Yes |
| 9 | BidPrice | money | Yes |
| 10 | CatalogPrice | numeric(22,6) | Yes |
| 11 | Discount | numeric(38,17) | Yes |
| 12 | BidExtended | money | Yes |
| 13 | CatalogExtended | numeric(33,6) | Yes |
| 14 | StateContractCost | numeric(38,6) | Yes |
| 15 | StateContractDiscount | decimal(13,9) | Yes |

#### vw_SavingsDetail2 {view-dbo-vw-savingsdetail2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-28 22:56:39.577000 |
| **Modified** | 2018-01-21 20:26:45.817000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | DistrictId | int | Yes |
| 3 | CategoryId | int | No |
| 4 | OnSavings | int | No |
| 5 | DistrictName | varchar(189) | Yes |
| 6 | CategoryName | varchar(50) | Yes |
| 7 | UniqueItems | int | Yes |
| 8 | TotalItems | int | Yes |
| 9 | TotalBidCost | money | Yes |
| 10 | TotalCatalogCost | numeric(38,6) | Yes |
| 11 | TotalStateContractCost | numeric(38,6) | Yes |
| 12 | StateContractDiscount | decimal(13,9) | Yes |
| 13 | OverallSavings | numeric(38,6) | Yes |
| 14 | OverallDiscount | numeric(38,17) | Yes |

#### vw_SavingsDetail2NonFiltered {view-dbo-vw-savingsdetail2nonfiltered}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-16 13:24:03.993000 |
| **Modified** | 2018-01-21 20:26:46.253000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | DistrictId | int | Yes |
| 3 | CategoryId | int | No |
| 4 | OnSavings | int | No |
| 5 | DistrictName | varchar(189) | Yes |
| 6 | CategoryName | varchar(50) | Yes |
| 7 | UniqueItems | int | Yes |
| 8 | TotalItems | int | Yes |
| 9 | TotalBidCost | money | Yes |
| 10 | TotalCatalogCost | numeric(38,6) | Yes |
| 11 | TotalStateContractCost | numeric(38,6) | Yes |
| 12 | StateContractDiscount | decimal(13,9) | Yes |
| 13 | OverallSavings | numeric(38,6) | Yes |
| 14 | OverallDiscount | numeric(38,17) | Yes |

#### vw_SavingsTotals {view-dbo-vw-savingstotals}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-12-28 22:57:48.013000 |
| **Modified** | 2018-01-21 20:26:45.823000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | Name | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | TotalBidCost | money | Yes |
| 6 | TotalCatalogCost | numeric(38,6) | Yes |
| 7 | TotalStateContractCost | numeric(38,6) | Yes |
| 8 | StateContractDiscount | decimal(13,9) | Yes |
| 9 | OverallSavings | numeric(38,6) | Yes |
| 10 | OverallDiscount | numeric(38,6) | Yes |
| 11 | IncludedCatalogCost | numeric(38,6) | Yes |
| 12 | IncludedBidCost | money | Yes |
| 13 | ExcludedCatalogCost | numeric(38,6) | Yes |
| 14 | ExcludedBidCost | money | Yes |
| 15 | IncludedSavings | numeric(38,6) | Yes |
| 16 | ExcludedSavings | numeric(38,6) | Yes |
| 17 | IncludedDiscount | numeric(38,6) | Yes |
| 18 | ExcludedDiscount | numeric(38,6) | Yes |

#### vw_SavingsTotals5 {view-dbo-vw-savingstotals5}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-08 09:40:04.430000 |
| **Modified** | 2018-01-21 20:26:46.087000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | Name | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | PastYearsCount | int | Yes |
| 6 | GTSavings | numeric(38,6) | No |
| 7 | CatalogExtended | numeric(38,6) | No |
| 8 | BidExtended | money | No |

#### vw_SavingsTotals5NJ {view-dbo-vw-savingstotals5nj}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-01-31 14:18:39.213000 |
| **Modified** | 2018-01-21 20:26:46.847000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | vw_SavingsTotals_Name | varchar(30) | Yes |
| 2 | vw_SavingsTotals_DistrictName | varchar(189) | Yes |
| 3 | vw_SavingsTotals_PastYearsCount | int | Yes |
| 4 | vw_SavingsTotals_GTSavings | numeric(38,6) | No |
| 5 | vw_SavingsTotals_CatalogExtended | numeric(38,6) | No |
| 6 | vw_SavingsTotals_BidExtended | money | No |

#### vw_SavingsTotals5NonFiltered {view-dbo-vw-savingstotals5nonfiltered}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-16 13:25:44.337000 |
| **Modified** | 2018-01-21 20:26:46.263000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | Name | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | PastYearsCount | int | Yes |
| 6 | GTSavings | numeric(38,6) | Yes |
| 7 | CatalogExtended | numeric(38,6) | Yes |
| 8 | BidExtended | money | Yes |

#### vw_SavingsTotals5Test {view-dbo-vw-savingstotals5test}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-08 15:37:40.217000 |
| **Modified** | 2018-01-21 20:26:46.170000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | Name | varchar(30) | Yes |
| 3 | DistrictId | int | Yes |
| 4 | DistrictName | varchar(189) | Yes |
| 5 | PastYearsCount | int | Yes |
| 6 | GTSavings | numeric(38,6) | Yes |
| 7 | CatalogExtended | numeric(38,6) | Yes |
| 8 | BidExtended | money | Yes |

#### vw_ScanDocLookupFields {view-dbo-vw-scandoclookupfields}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-06-11 14:36:31.737000 |
| **Modified** | 2025-10-27 20:10:53.390000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ScanJobId | int | No |
| 2 | DocTypeFieldExternalLookupId | uniqueidentifier | No |
| 3 | ExternalTableName | nvarchar(128) | No |
| 4 | ItemOrder | int | No |
| 5 | DocTypeFieldExternalLookupItemId | uniqueidentifier | No |
| 6 | Type | nvarchar(50) | No |
| 7 | DocTypeFieldExternalLookupItemOrder | int | No |
| 8 | Name | nvarchar(50) | No |
| 9 | DocTypeFieldId | uniqueidentifier | No |

#### vw_ScanDocLookupTargets {view-dbo-vw-scandoclookuptargets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-06-11 14:36:31.813000 |
| **Modified** | 2025-10-27 20:12:04.527000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ScanJobId | int | No |
| 2 | DocTypeFieldExternalLookupId | uniqueidentifier | No |
| 3 | ExternalTableName | nvarchar(128) | No |
| 4 | ItemOrder | int | No |
| 5 | DocTypeFieldExternalLookupItemId | uniqueidentifier | No |
| 6 | DocTypeFieldExternalLookupItemOrder | int | No |
| 7 | ExternalValueColumn | nvarchar(128) | No |
| 8 | Name | nvarchar(50) | No |
| 9 | DocTypeFieldId | uniqueidentifier | No |

#### vw_ScanDocLookups {view-dbo-vw-scandoclookups}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-06-11 14:36:31.627000 |
| **Modified** | 2025-10-27 20:11:29.103000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ScanJobId | int | No |
| 2 | DocTypeFieldExternalLookupId | uniqueidentifier | No |
| 3 | ExternalTableName | nvarchar(128) | No |
| 4 | ItemOrder | int | No |

#### vw_ScannedDocumentDataMSDS {view-dbo-vw-scanneddocumentdatamsds}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-06-21 14:05:54.763000 |
| **Modified** | 2013-06-26 18:34:59.137000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CatalogName | nvarchar(50) | No |
| 2 | DocumentType | nvarchar(50) | No |
| 3 | DocFolder | nvarchar(260) | No |
| 4 | DocName | nvarchar(260) | No |
| 5 | BaseName | nvarchar(260) | No |
| 6 | FullFileName | nvarchar(520) | No |
| 7 | VersionMajor | int | No |
| 8 | VersionMinor | int | No |
| 9 | CreatedUtc | datetime | No |
| 10 | PagesCaptured | int | No |
| 11 | DocId | uniqueidentifier | No |
| 12 | RevisionDate | datetime | Yes |
| 13 | CategoryName | nvarchar(50) | Yes |
| 14 | EDSItemCode | nvarchar(4000) | Yes |
| 15 | ManufacturerName | nvarchar(4000) | Yes |
| 16 | ProductName | nvarchar(4000) | Yes |
| 17 | ManufacturerPartNumber | nvarchar(4000) | Yes |
| 18 | EPARegistrationNumber | nvarchar(4000) | Yes |
| 19 | SendTo | nvarchar(4000) | Yes |

#### vw_ScannedDocumentDataMSDSCategories {view-dbo-vw-scanneddocumentdatamsdscategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-06-27 15:12:14.907000 |
| **Modified** | 2013-07-10 13:25:04.527000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CategoryName | nvarchar(50) | Yes |

#### vw_ScannedDocumentDataMSDSManufacturers {view-dbo-vw-scanneddocumentdatamsdsmanufacturers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-06-28 16:49:37.617000 |
| **Modified** | 2013-07-10 13:25:23.440000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ManufacturerName | varchar(50) | Yes |

#### vw_SchoolUsers {view-dbo-vw-schoolusers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-27 11:32:16.350000 |
| **Modified** | 2018-01-21 20:26:48.380000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SchoolId | int | Yes |
| 2 | UserId | int | No |
| 3 | CometId | varchar(58) | Yes |

#### vw_SearchDescription {view-dbo-vw-searchdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2024-08-30 10:16:41.057000 |
| **Modified** | 2025-06-27 20:59:16.060000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | ItemDescription | nvarchar(MAX) | Yes |
| 4 | ShortDescription | nvarchar(MAX) | Yes |

#### vw_SearchItemsDetail {view-dbo-vw-searchitemsdetail}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 21:54:06.863000 |
| **Modified** | 2018-01-21 20:26:48.387000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | HeadingId | int | No |
| 3 | KeywordId | int | No |
| 4 | BidItems_BidItemId | int | Yes |
| 5 | Price | decimal(34,13) | Yes |
| 6 | BidItems_Alternate | varchar(512) | Yes |
| 7 | BidItems_VendorItemCode | varchar(50) | Yes |
| 8 | ItemBidType | varchar(32) | Yes |
| 9 | PageNo | int | Yes |
| 10 | Items_ItemCode | varchar(50) | Yes |
| 11 | Items_Description | varchar(512) | Yes |
| 12 | Items_HeadingId | int | Yes |
| 13 | Items_SortSeq | varchar(64) | Yes |
| 14 | BidDiscountRate | decimal(8,5) | Yes |
| 15 | Vendors_Name | varchar(50) | Yes |
| 16 | Units_Code | varchar(20) | Yes |
| 17 | DetailId | int | Yes |
| 18 | Quantity | int | Yes |
| 19 | ItemId | int | No |

#### vw_SearchItemsHeadings {view-dbo-vw-searchitemsheadings}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 21:41:52.857000 |
| **Modified** | 2018-01-21 20:26:48.393000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | Title | varchar(255) | No |
| 3 | Description | varchar(4096) | Yes |
| 4 | HeadingId | int | No |
| 5 | SearchLetter | varchar(1) | No |

#### vw_SearchItemsKeywords {view-dbo-vw-searchitemskeywords}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-26 21:59:43.380000 |
| **Modified** | 2018-01-21 20:26:48.400000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | Title | varchar(255) | Yes |
| 4 | Description | varchar(4096) | Yes |
| 5 | HeadingId | int | Yes |
| 6 | Keyword | varchar(50) | Yes |
| 7 | KeywordId | int | Yes |

#### vw_SessionCategories {view-dbo-vw-sessioncategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-25 16:03:24.380000 |
| **Modified** | 2018-01-21 20:26:48.403000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | Name | varchar(50) | Yes |

#### vw_SessionCategoryVendors {view-dbo-vw-sessioncategoryvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-25 16:53:22.383000 |
| **Modified** | 2018-01-21 20:26:48.410000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |
| 4 | VendorId | int | No |
| 5 | VendorName | varchar(50) | Yes |
| 6 | WebURL | varchar(255) | Yes |

#### vw_SessionTableBudgets {view-dbo-vw-sessiontablebudgets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-05-27 11:29:03.107000 |
| **Modified** | 2018-01-21 20:26:48.417000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | BudgetId | int | No |
| 3 | Name | varchar(30) | Yes |
| 4 | EndDate | datetime | Yes |

#### vw_ShortDescription {view-dbo-vw-shortdescription}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-08-19 08:28:52.653000 |
| **Modified** | 2023-03-01 08:58:50.257000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemId | int | No |
| 2 | VendorId | int | Yes |
| 3 | ShortDescription | varchar(4096) | Yes |

#### vw_StatusDetailed {view-dbo-vw-statusdetailed}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-21 11:24:20.753000 |
| **Modified** | 2018-01-21 20:26:48.420000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | No |
| 2 | Status | varchar(104) | No |

#### vw_StatusHistory {view-dbo-vw-statushistory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-02 21:09:09.087000 |
| **Modified** | 2021-09-01 15:04:05.597000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | RequisitionId | int | Yes |
| 2 | StatusName | varchar(104) | No |
| 3 | ApprovalDate | datetime | Yes |
| 4 | ActionUserId | int | No |
| 5 | ActionCometId | int | Yes |
| 6 | ActionAttention | varchar(50) | Yes |
| 7 | ApproverUserId | int | Yes |
| 8 | ApproverAttention | varchar(50) | Yes |
| 9 | ApproverCometId | int | Yes |

#### vw_TMAwardedVendors {view-dbo-vw-tmawardedvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2015-04-13 15:47:15.117000 |
| **Modified** | 2018-01-21 20:26:48.427000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | VendorNameAndAddress | varchar(394) | Yes |
| 5 | Address1 | varchar(50) | Yes |
| 6 | Address2 | varchar(50) | Yes |
| 7 | City | varchar(50) | Yes |
| 8 | State | char(2) | Yes |
| 9 | Zipcode | varchar(10) | Yes |
| 10 | Phone | varchar(25) | Yes |
| 11 | Fax | varchar(20) | Yes |
| 12 | EMail | varchar(255) | Yes |
| 13 | FullName | varchar(150) | Yes |
| 14 | BidHeaderId | int | Yes |
| 15 | BidMessage | varchar(1024) | Yes |
| 16 | VendorBidNumber | varchar(50) | Yes |
| 17 | Title | varchar(255) | No |
| 18 | PackageNumber | int | Yes |
| 19 | StateName | varchar(50) | Yes |
| 20 | CountyName | varchar(50) | No |
| 21 | AwardType | varchar(50) | Yes |
| 22 | EffectiveFrom | datetime | Yes |
| 23 | EffectiveUntil | datetime | Yes |
| 24 | BidAwardDate | datetime | Yes |
| 25 | StateId | int | Yes |
| 26 | HostDistrict | varchar(50) | Yes |
| 27 | ContactName | varchar(170) | Yes |

#### vw_TMCountyTrades {view-dbo-vw-tmcountytrades}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-17 15:21:40.740000 |
| **Modified** | 2018-07-13 15:14:02.090000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | TMSurveyId | int | No |
| 2 | BidTradeId | int | No |
| 3 | Description | varchar(255) | No |
| 4 | CountyId | int | No |
| 5 | TMYear | int | Yes |
| 6 | VendorCount | int | Yes |
| 7 | PrevTradeId | int | Yes |
| 8 | NextTradeId | int | Yes |

#### vw_TMLineItems {view-dbo-vw-tmlineitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-02 21:54:52.393000 |
| **Modified** | 2018-01-21 20:26:48.440000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | Title | varchar(255) | No |
| 4 | ItemCode | varchar(50) | Yes |
| 5 | Description | varchar(512) | No |
| 6 | UnitCode | varchar(20) | No |
| 7 | BidPrice | decimal(33,13) | Yes |
| 8 | Alternate | varchar(512) | No |
| 9 | SortSeq | varchar(64) | Yes |

#### vw_TMSurveyData {view-dbo-vw-tmsurveydata}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-19 09:37:31.227000 |
| **Modified** | 2025-05-21 10:17:02.157000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | TMSurveyResultId | int | No |
| 2 | TMSurveyId | int | No |
| 3 | TMVendorId | int | No |
| 4 | Rating | int | Yes |
| 5 | Comments | varchar(MAX) | Yes |
| 6 | Name | varchar(50) | Yes |
| 7 | Sequence | varchar(50) | Yes |
| 8 | TradeId | int | No |
| 9 | BidTradeId | int | No |
| 10 | Title | varchar(255) | No |

#### vw_TMSurveys {view-dbo-vw-tmsurveys}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-31 10:45:03.870000 |
| **Modified** | 2025-05-21 10:16:29.910000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | TMSurveyId | int | No |
| 2 | DistrictId | int | No |
| 3 | Submitter | varchar(255) | Yes |
| 4 | Title | varchar(255) | Yes |
| 5 | Email | varchar(255) | Yes |
| 6 | Started | datetime | Yes |
| 7 | Finished | datetime | Yes |
| 8 | CountyId | int | Yes |
| 9 | FirstTradeId | int | Yes |

#### vw_TMTrades {view-dbo-vw-tmtrades}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-10-21 16:30:36.453000 |
| **Modified** | 2018-10-26 08:05:11.253000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | TMSurveyId | int | No |
| 2 | TradeId | int | No |
| 3 | TMYear | int | Yes |
| 4 | CountyId | int | No |
| 5 | Description | varchar(255) | No |
| 6 | PrevTradeId | int | Yes |
| 7 | NextTradeId | int | Yes |

#### vw_TMTradesAwardedVendors {view-dbo-vw-tmtradesawardedvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-29 10:40:22.683000 |
| **Modified** | 2018-07-13 15:13:52.590000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | VendorCode | varchar(16) | Yes |
| 3 | VendorName | varchar(50) | Yes |
| 4 | VendorNameAndAddress | varchar(394) | Yes |
| 5 | Address1 | varchar(50) | Yes |
| 6 | Address2 | varchar(50) | Yes |
| 7 | City | varchar(50) | Yes |
| 8 | State | char(2) | Yes |
| 9 | Zipcode | varchar(10) | Yes |
| 10 | Phone | varchar(25) | Yes |
| 11 | Fax | varchar(20) | Yes |
| 12 | EMail | varchar(255) | Yes |
| 13 | FullName | varchar(150) | Yes |
| 14 | BidHeaderId | int | Yes |
| 15 | BidMessage | varchar(1024) | Yes |
| 16 | VendorBidNumber | varchar(50) | Yes |
| 17 | Title | varchar(255) | No |
| 18 | PackageNumber | int | Yes |
| 19 | StateName | char(2) | No |
| 20 | CountyName | varchar(50) | No |
| 21 | AwardType | varchar(50) | Yes |
| 22 | EffectiveFrom | datetime | Yes |
| 23 | EffectiveUntil | datetime | Yes |
| 24 | BidAwardDate | datetime | Yes |
| 25 | StateId | int | Yes |
| 26 | HostDistrict | varchar(50) | Yes |
| 27 | ContactName | varchar(170) | Yes |
| 28 | CategoryName | varchar(50) | Yes |
| 29 | CategoryId | int | No |
| 30 | AwardingType | varchar(10) | No |
| 31 | ReawardDate | datetime | Yes |
| 32 | ReawardFrom | datetime | Yes |
| 33 | ReawardUntil | datetime | Yes |
| 34 | PricePlanId | int | Yes |
| 35 | BidTradeCountyId | int | No |

#### vw_TMTradesSummary {view-dbo-vw-tmtradessummary}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-05-19 22:34:56.487000 |
| **Modified** | 2018-01-21 20:26:48.457000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | No |
| 2 | BidTradeCountyId | int | No |
| 3 | CountyId | int | No |
| 4 | AwardType | varchar(50) | Yes |
| 5 | VendorName | varchar(101) | Yes |

#### vw_TMUsers {view-dbo-vw-tmusers}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-03-29 14:06:36.290000 |
| **Modified** | 2018-01-21 20:26:48.460000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictCode | varchar(4) | Yes |
| 2 | DistrictName | varchar(50) | Yes |
| 3 | Attention | varchar(50) | Yes |
| 4 | UserNbr | varchar(5) | Yes |
| 5 | UserName | varchar(10) | Yes |
| 6 | Password | varchar(10) | Yes |
| 7 | userId | int | No |
| 8 | DistrictId | int | No |
| 9 | useCF | int | No |

#### vw_TMVendorsForReports {view-dbo-vw-tmvendorsforreports}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-04-03 23:37:05.993000 |
| **Modified** | 2018-01-21 20:26:48.470000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidTradeCountyId | int | Yes |
| 2 | BidImportId | int | Yes |
| 3 | BidHeaderId | int | Yes |
| 4 | BidCounty | varchar(30) | Yes |
| 5 | BidState | varchar(50) | Yes |
| 6 | TradeName | varchar(30) | Yes |
| 7 | PackageNumber | int | Yes |
| 8 | TradeDescription | varchar(30) | Yes |
| 9 | AwardType | varchar(15) | No |
| 10 | BidDate | datetime | Yes |
| 11 | BidAwardDate | datetime | Yes |
| 12 | EffectiveFrom | datetime | Yes |
| 13 | EffectiveUntil | datetime | Yes |
| 14 | VendorCode | varchar(16) | No |
| 15 | VendorName | varchar(50) | No |
| 16 | ContactName | varchar(150) | No |
| 17 | ContactPhone | varchar(25) | No |
| 18 | ContactFax | varchar(20) | No |
| 19 | ContactEmail | varchar(255) | No |
| 20 | Address1 | varchar(50) | No |
| 21 | Address2 | varchar(50) | No |
| 22 | City | varchar(50) | No |
| 23 | State | char(2) | No |
| 24 | Zipcode | varchar(10) | No |
| 25 | VendorContactInfo | varchar(1726) | Yes |
| 26 | HostName | varchar(50) | Yes |
| 27 | HostNameAndAddress | varchar(222) | Yes |
| 28 | CategoryType | int | Yes |
| 29 | CategoryName | varchar(1075) | Yes |
| 30 | Grouping | varchar(50) | No |

#### vw_UsedAccountData {view-dbo-vw-usedaccountdata}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2008-06-20 13:52:53.140000 |
| **Modified** | 2018-01-21 20:26:48.477000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | BudgetName | varchar(30) | Yes |
| 3 | SchoolId | int | No |
| 4 | SchoolName | varchar(50) | Yes |
| 5 | UserId | int | No |
| 6 | CometId | int | Yes |
| 7 | UserAttention | varchar(50) | Yes |
| 8 | RequisitionId | int | No |
| 9 | Attention | varchar(50) | Yes |
| 10 | TotalRequisitionCost | money | Yes |
| 11 | CategoryId | int | No |
| 12 | CategoryName | varchar(50) | Yes |
| 13 | UserAccountId | int | Yes |
| 14 | UseUserAllocations | tinyint | Yes |
| 15 | AllocationAmount | money | Yes |
| 16 | AllocationAvailable | money | Yes |
| 17 | AccountId | int | Yes |
| 18 | Code | varchar(50) | Yes |

#### vw_UserNotificationOptions {view-dbo-vw-usernotificationoptions}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2019-11-02 21:54:17.827000 |
| **Modified** | 2019-12-10 10:40:19.030000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | NotificationOptionId | int | No |
| 2 | Name | varchar(50) | No |

#### vw_Users_Assoc_With_Bid {view-dbo-vw-users-assoc-with-bid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2016-08-30 13:19:55.083000 |
| **Modified** | 2022-07-28 14:46:16.697000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | DistrictId | int | No |
| 3 | UserId | int | No |
| 4 | ApproverId | int | Yes |

#### vw_VPOLoginCheck {view-dbo-vw-vpologincheck}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-03-23 12:55:58.173000 |
| **Modified** | 2018-01-21 20:26:48.580000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VPORegistrationId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | VPOUserCode | varchar(50) | No |
| 4 | VPOPassword | varchar(50) | No |
| 5 | VPOLastChange | datetime | No |
| 6 | VPOEMail | varchar(255) | No |
| 7 | VPOName | varchar(50) | No |
| 8 | VPOPhone | varchar(50) | No |
| 9 | VPOParentId | int | No |
| 10 | VPOCanCreateUser | tinyint | No |
| 11 | VPOStatus | tinyint | Yes |

#### vw_VPOVendors {view-dbo-vw-vpovendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-03-24 11:59:52.387000 |
| **Modified** | 2018-01-21 20:26:48.583000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorSessionId | int | No |
| 2 | VPORegistrationId | int | Yes |
| 3 | VendorId | int | No |
| 4 | Name | varchar(50) | Yes |

#### vw_ValidLogins {view-dbo-vw-validlogins}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-22 13:44:53.670000 |
| **Modified** | 2018-01-21 20:26:48.493000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | UserId | int | No |
| 2 | UserMatch | varchar(26) | Yes |
| 3 | Password | varchar(10) | No |

#### vw_Vendor0528Items {view-dbo-vw-vendor0528items}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-06-22 12:53:19.927000 |
| **Modified** | 2018-01-21 20:26:46.307000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | ItemCode | varchar(50) | Yes |
| 2 | VendorItemCode | varchar(50) | No |
| 3 | description | varchar(1024) | Yes |
| 4 | Code | varchar(20) | Yes |
| 5 | atReq | int | Yes |
| 6 | atPO | int | Yes |

#### vw_VendorBidDocumentsList {view-dbo-vw-vendorbiddocumentslist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-12-28 11:08:23.837000 |
| **Modified** | 2018-01-21 20:26:48.497000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(50) | No |

#### vw_VendorBidInfoStats {view-dbo-vw-vendorbidinfostats}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2022-01-14 12:03:33.403000 |
| **Modified** | 2022-01-14 12:42:41.397000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | BidImportId | int | No |
| 3 | Name | varchar(50) | Yes |
| 4 | ItemsWon | int | Yes |
| 5 | UPC_ISBN_Provided | int | Yes |
| 6 | SDS_URLsProvided | int | Yes |
| 7 | URLsProvided | int | Yes |
| 8 | Max_URL_Duplicate_Count | int | No |
| 9 | Max_Duplicate_URL | varchar(300) | No |

#### vw_VendorBlast {view-dbo-vw-vendorblast}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-04 16:33:54.363000 |
| **Modified** | 2018-01-21 20:26:46.727000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorName | varchar(50) | Yes |
| 2 | VendorId | int | No |
| 3 | ContactFullName | varchar(150) | Yes |
| 4 | ContactEMail | varchar(255) | Yes |
| 5 | BidContact | tinyint | Yes |
| 6 | POContact | tinyint | Yes |
| 7 | CategoryId | int | Yes |
| 8 | BidHeaderId | int | Yes |
| 9 | BidScheduleId | int | Yes |
| 10 | VBCategoryId | int | Yes |
| 11 | AwardedBid | int | No |
| 12 | SubmittedBid | int | No |
| 13 | RegisteredToBid | int | No |
| 14 | DownloadedBid | int | No |
| 15 | RegisteredCategory | int | No |

#### vw_VendorBlast_AwardedByBid {view-dbo-vw-vendorblast-awardedbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-09 13:37:58.377000 |
| **Modified** | 2018-01-21 20:26:48.500000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorID | int | Yes |
| 2 | BidHeaderId | int | Yes |

#### vw_VendorBlast_DownloadedBySchedule {view-dbo-vw-vendorblast-downloadedbyschedule}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-09 13:37:58.633000 |
| **Modified** | 2018-01-21 20:26:48.503000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | Yes |
| 2 | BidScheduleId | int | Yes |

#### vw_VendorBlast_RegisteredByBid {view-dbo-vw-vendorblast-registeredbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-09 13:37:58.090000 |
| **Modified** | 2018-01-21 20:26:46.763000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | Yes |
| 2 | BidHeaderId | int | Yes |

#### vw_VendorBlast_RegisteredByCategory {view-dbo-vw-vendorblast-registeredbycategory}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-09 13:37:58.757000 |
| **Modified** | 2018-01-21 20:26:46.777000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | Yes |
| 2 | CategoryId | int | No |

#### vw_VendorBlast_RegisteredBySchedule {view-dbo-vw-vendorblast-registeredbyschedule}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-09 13:37:58.520000 |
| **Modified** | 2018-01-21 20:26:48.507000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | Yes |
| 2 | BidScheduleId | int | No |

#### vw_VendorBlast_SubmittedByBid {view-dbo-vw-vendorblast-submittedbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-05-09 13:37:58.230000 |
| **Modified** | 2018-01-21 20:26:48.510000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | BidHeaderId | int | Yes |

#### vw_VendorCategoryBids {view-dbo-vw-vendorcategorybids}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-11-16 11:18:28.963000 |
| **Modified** | 2023-03-30 11:36:08.490000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | No |
| 4 | ContactInfo | varchar(548) | Yes |
| 5 | CategoryId | int | No |
| 6 | CategoryName | varchar(308) | Yes |
| 7 | BidHeaderId | int | Yes |
| 8 | VendorBidNumber | varchar(50) | No |
| 9 | AdditionalHandlingAmount | money | No |
| 10 | FreeHandlingAmount | money | No |
| 11 | BidComments | varchar(512) | No |
| 12 | CatalogId | int | Yes |
| 13 | EMail | varchar(255) | No |
| 14 | VendorCode | varchar(16) | No |
| 15 | DistrictVendorCode | varchar(20) | No |
| 16 | VendorsAccountCode | varchar(50) | No |

#### vw_VendorCategoryBids_Cats {view-dbo-vw-vendorcategorybids-cats}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-11-17 14:31:40.283000 |
| **Modified** | 2018-01-21 20:26:47.050000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | CategoryId | int | No |
| 3 | CategoryName | varchar(50) | Yes |

#### vw_VendorCategoryBids_Vendors {view-dbo-vw-vendorcategorybids-vendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-11-17 14:48:12.250000 |
| **Modified** | 2018-01-21 20:26:47.060000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BudgetId | int | No |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | No |

#### vw_VendorDocRequestStatus {view-dbo-vw-vendordocrequeststatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2020-12-08 20:48:24.283000 |
| **Modified** | 2020-12-08 20:48:24.283000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorDocRequestId | int | No |
| 2 | Status | varchar(18) | Yes |
| 3 | StatusDate | datetime | Yes |
| 4 | FollowUpDate | datetime | Yes |
| 5 | VendorDocRequestStatusId | int | Yes |

#### vw_VendorDocumentsList {view-dbo-vw-vendordocumentslist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-06-17 14:02:37.067000 |
| **Modified** | 2018-01-21 20:26:48.513000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Name | varchar(50) | No |

#### vw_VendorPODistrictList {view-dbo-vw-vendorpodistrictlist}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-04-08 01:06:17.073000 |
| **Modified** | 2018-01-21 20:26:48.517000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | name | varchar(50) | Yes |
| 2 | dataValue | int | No |
| 3 | VendorSessionId | int | No |
| 4 | VendorId | int | No |
| 5 | VendorsAccountCode | varchar(50) | No |
| 6 | SummaryName | varchar(106) | Yes |

#### vw_VendorPODistricts {view-dbo-vw-vendorpodistricts}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-04-07 18:51:16.330000 |
| **Modified** | 2018-01-21 20:26:48.520000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | VendorSessionId | int | No |
| 3 | VendorId | int | No |
| 4 | DistrictName | varchar(50) | Yes |
| 5 | VendorsAccountCode | varchar(50) | No |
| 6 | SummaryName | varchar(106) | Yes |

#### vw_VendorPODistrictsAndBudgets {view-dbo-vw-vendorpodistrictsandbudgets}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-03-10 17:36:30.527000 |
| **Modified** | 2025-07-11 13:56:37.040000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | BudgetId | int | No |
| 3 | VendorSessionId | int | No |
| 4 | VendorId | int | No |
| 5 | DistrictName | varchar(50) | Yes |
| 6 | BudgetName | varchar(30) | Yes |
| 7 | VendorsAccountCode | varchar(50) | No |
| 8 | SummaryName | varchar(151) | Yes |
| 9 | BudgetFilterId | int | Yes |

#### vw_VendorPODistrictsAndBudgetsCF {view-dbo-vw-vendorpodistrictsandbudgetscf}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-07-10 06:32:14.840000 |
| **Modified** | 2018-01-21 20:26:48.533000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | BudgetId | int | No |
| 3 | VendorSessionId | int | No |
| 4 | VendorId | int | No |
| 5 | DistrictName | varchar(50) | Yes |
| 6 | BudgetName | varchar(30) | Yes |
| 7 | VendorsAccountCode | varchar(50) | No |
| 8 | TotalPOCount | int | Yes |
| 9 | TotalPOAmount | money | No |
| 10 | ExportedPOCount | int | Yes |
| 11 | ExportedPOAmount | money | No |
| 12 | WaitingPOCount | int | Yes |
| 13 | WaitingPOAmount | money | No |
| 14 | BudgetFilterId | int | Yes |

#### vw_VendorPODistrictsAndBudgetsOld {view-dbo-vw-vendorpodistrictsandbudgetsold}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-07-07 18:07:52.513000 |
| **Modified** | 2018-01-21 20:26:48.540000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | BudgetId | int | No |
| 3 | VendorSessionId | int | No |
| 4 | VendorId | int | No |
| 5 | DistrictName | varchar(50) | Yes |
| 6 | BudgetName | varchar(30) | Yes |
| 7 | VendorsAccountCode | varchar(50) | No |
| 8 | SummaryName | varchar(111) | Yes |
| 9 | BudgetFilterId | int | Yes |

#### vw_VendorPODistrictsAndBudgetsTest {view-dbo-vw-vendorpodistrictsandbudgetstest}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2017-07-10 23:18:54.880000 |
| **Modified** | 2018-08-01 00:03:29.350000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | DistrictId | int | No |
| 2 | BudgetId | int | No |
| 3 | VendorSessionId | int | No |
| 4 | VendorId | int | No |
| 5 | DistrictName | varchar(50) | Yes |
| 6 | BudgetName | varchar(30) | Yes |
| 7 | VendorsAccountCode | varchar(50) | No |
| 8 | SummaryName | varchar(150) | Yes |
| 9 | BudgetFilterId | int | Yes |

#### vw_VendorPOView {view-dbo-vw-vendorpoview}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-02-27 12:02:17.097000 |
| **Modified** | 2018-01-21 20:26:46.340000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorSessionId | int | No |
| 2 | VendorId | int | No |
| 3 | DistrictId | int | No |
| 4 | POId | int | No |
| 5 | PONumber | varchar(24) | Yes |
| 6 | Amount | money | Yes |
| 7 | RequisitionNumber | varchar(24) | Yes |
| 8 | Attention | varchar(50) | No |
| 9 | TotalRequisitionCost | money | Yes |
| 10 | DistrictName | varchar(50) | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | UserNbr | int | Yes |
| 13 | CategoryId | int | No |
| 14 | CategoryName | varchar(50) | Yes |
| 15 | BudgetId | int | No |
| 16 | BudgetName | varchar(30) | Yes |
| 17 | OrderDate | datetime | Yes |
| 18 | RequisitionId | int | No |
| 19 | UploadId | int | No |
| 20 | DateUploaded | datetime | No |
| 21 | FileName | varchar(255) | No |
| 22 | Tagged | int | No |
| 23 | POLines | int | Yes |
| 24 | PayloadId | varchar(255) | No |
| 25 | UploadUser | varchar(50) | No |
| 26 | VendorsAccountCode | varchar(50) | No |
| 27 | UploadEMailList | varchar(4096) | No |
| 28 | UploadType | int | No |
| 29 | VendorName | varchar(50) | No |
| 30 | Cancelled | tinyint | No |

#### vw_VendorPOView1 {view-dbo-vw-vendorpoview1}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-03-19 00:45:16.450000 |
| **Modified** | 2018-01-21 20:26:46.350000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorSessionId | int | No |
| 2 | VendorId | int | No |
| 3 | DistrictId | int | No |
| 4 | POId | int | No |
| 5 | PONumber | varchar(24) | Yes |
| 6 | Amount | money | Yes |
| 7 | RequisitionNumber | varchar(24) | Yes |
| 8 | Attention | varchar(50) | No |
| 9 | TotalRequisitionCost | money | Yes |
| 10 | DistrictName | varchar(50) | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | UserNbr | int | Yes |
| 13 | CategoryId | int | No |
| 14 | CategoryName | varchar(50) | Yes |
| 15 | BudgetId | int | No |
| 16 | BudgetName | varchar(30) | Yes |
| 17 | OrderDate | datetime | Yes |
| 18 | RequisitionId | int | No |
| 19 | UploadId | int | No |
| 20 | DateUploaded | datetime | No |
| 21 | FileName | varchar(255) | No |
| 22 | Tagged | int | No |
| 23 | POLines | int | Yes |
| 24 | PayloadId | varchar(255) | No |
| 25 | UploadUser | varchar(50) | No |
| 26 | VendorsAccountCode | varchar(50) | No |
| 27 | UploadEMailList | varchar(4096) | No |
| 28 | UploadType | int | No |
| 29 | VendorName | varchar(50) | No |
| 30 | Cancelled | tinyint | No |

#### vw_VendorPOView2 {view-dbo-vw-vendorpoview2}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-04-06 22:46:28.660000 |
| **Modified** | 2018-01-21 20:26:48.550000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorSessionId | int | No |
| 2 | VendorId | int | No |
| 3 | DistrictId | int | No |
| 4 | POId | int | No |
| 5 | PONumber | varchar(24) | Yes |
| 6 | Amount | money | Yes |
| 7 | RequisitionNumber | varchar(24) | Yes |
| 8 | Attention | varchar(50) | Yes |
| 9 | TotalRequisitionCost | money | Yes |
| 10 | DistrictName | varchar(50) | Yes |
| 11 | SchoolName | varchar(50) | Yes |
| 12 | UserNbr | int | Yes |
| 13 | CategoryId | int | No |
| 14 | CategoryName | varchar(50) | Yes |
| 15 | BudgetId | int | No |
| 16 | BudgetName | varchar(30) | Yes |
| 17 | OrderDate | datetime | Yes |
| 18 | RequisitionId | int | No |
| 19 | UploadId | int | No |
| 20 | DateUploaded | datetime | No |
| 21 | FileName | varchar(255) | No |
| 22 | Tagged | tinyint | No |
| 23 | POLines | int | Yes |

#### vw_VendorQueryMSRPStatus {view-dbo-vw-vendorquerymsrpstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-02-28 13:52:29.553000 |
| **Modified** | 2018-01-21 20:26:48.557000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorQueryMSRPId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | BidImportId | int | Yes |
| 5 | EmailAddress | varchar(255) | Yes |
| 6 | ContactName | varchar(255) | Yes |
| 7 | SendDate | datetime | Yes |
| 8 | VendorQueryMSRPNotes | varchar(1000) | Yes |
| 9 | Status | varchar(18) | Yes |
| 10 | StatusDate | datetime | Yes |
| 11 | FollowUpDate | datetime | Yes |
| 12 | VendorQueryMSRPStatusId | int | Yes |
| 13 | VendorName | varchar(50) | Yes |

#### vw_VendorQueryStatus {view-dbo-vw-vendorquerystatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-07-29 17:50:05.307000 |
| **Modified** | 2018-01-21 20:26:48.560000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorQueryId | int | No |
| 2 | Status | varchar(18) | Yes |
| 3 | StatusDate | datetime | Yes |
| 4 | FollowUpDate | datetime | Yes |
| 5 | VendorQueryStatusId | int | Yes |

#### vw_VendorQueryTandMStatus {view-dbo-vw-vendorquerytandmstatus}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-01-22 13:16:27.540000 |
| **Modified** | 2018-01-21 20:26:48.567000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorQueryTandMId | int | No |
| 2 | BidHeaderId | int | Yes |
| 3 | VendorId | int | Yes |
| 4 | BidImportId | int | Yes |
| 5 | EmailAddress | varchar(255) | Yes |
| 6 | ContactName | varchar(255) | Yes |
| 7 | SendDate | datetime | Yes |
| 8 | VendorQueryTandMNotes | varchar(1000) | Yes |
| 9 | Status | varchar(18) | Yes |
| 10 | StatusDate | datetime | Yes |
| 11 | FollowUpDate | datetime | Yes |
| 12 | VendorQueryTandMStatusId | int | Yes |
| 13 | VendorName | varchar(50) | Yes |

#### vw_Vendors {view-dbo-vw-vendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-11-16 09:44:55.080000 |
| **Modified** | 2025-09-18 15:12:44.663000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | Code | varchar(16) | No |
| 3 | Name | varchar(50) | Yes |
| 4 | Address1 | varchar(50) | No |
| 5 | Address2 | varchar(50) | No |
| 6 | Address3 | varchar(1) | No |
| 7 | City | varchar(50) | No |
| 8 | State | char(2) | No |
| 9 | Zipcode | varchar(10) | No |
| 10 | Phone | varchar(25) | No |
| 11 | Fax | varchar(20) | No |
| 12 | EMail | varchar(255) | No |
| 13 | ShippingPercentage | decimal(9,5) | No |
| 14 | ContactInfo | varchar(548) | Yes |
| 15 | FullName | varchar(150) | Yes |

#### vw_VendorsByBid {view-dbo-vw-vendorsbybid}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2010-01-05 18:11:30.260000 |
| **Modified** | 2018-01-21 20:26:45.977000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | No |
| 3 | VendorName | varchar(50) | No |

#### vw_VendorsTable {view-dbo-vw-vendorstable}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2011-09-09 13:25:00.760000 |
| **Modified** | 2018-01-21 20:26:48.573000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | VendorId | int | No |
| 2 | Active | tinyint | Yes |
| 3 | Code | varchar(16) | Yes |
| 4 | Name | varchar(50) | Yes |
| 5 | Address1 | varchar(50) | No |
| 6 | Address2 | varchar(50) | No |
| 7 | Address3 | varchar(50) | No |
| 8 | City | varchar(50) | No |
| 9 | State | varchar(12) | No |
| 10 | ZipCode | varchar(12) | No |
| 11 | Phone | varchar(25) | No |
| 12 | Fax | varchar(20) | No |
| 13 | EMail | varchar(255) | No |
| 14 | UseGrossPrices | tinyint | Yes |
| 15 | ShippingPercentage | decimal(9,5) | Yes |
| 16 | DistrictId | int | Yes |
| 17 | Password | varchar(50) | Yes |
| 18 | HostURL | varchar(255) | Yes |
| 19 | HostPort | int | Yes |
| 20 | HostDirectory | varchar(255) | Yes |
| 21 | HostUserName | varchar(255) | Yes |
| 22 | HostPassword | varchar(255) | Yes |
| 23 | UploadEMailList | varchar(4096) | Yes |
| 24 | UploadType | int | Yes |
| 25 | BusinessUnit | varchar(17) | Yes |
| 26 | POPassword | varchar(50) | Yes |
| 27 | cXMLAddress | varchar(255) | Yes |
| 28 | Emails | varchar(2048) | Yes |
| 29 | Phones | varchar(2048) | Yes |

#### vw_WincapVendors {view-dbo-vw-wincapvendors}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-02 22:44:11.690000 |
| **Modified** | 2018-01-21 20:26:48.590000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Vendor Code | varchar(16) | No |
| 2 | Vendors Name | varchar(50) | Yes |
| 3 | Full Name And Address | varchar(704) | Yes |
| 4 | Category | varchar(50) | Yes |
| 5 | Vendor Bid Number | varchar(50) | No |
| 6 | Comments | varchar(1024) | No |
| 7 | District Vendor Code | varchar(20) | No |

#### vw_WincapVendorsMaster {view-dbo-vw-wincapvendorsmaster}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2012-07-02 22:49:02.307000 |
| **Modified** | 2018-01-21 20:26:48.597000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | Vendor Name | varchar(50) | Yes |
| 2 | Ed-Data Vendor Code | varchar(16) | No |
| 3 | Contact Name | varchar(150) | No |
| 4 | Address1 | varchar(50) | No |
| 5 | Address2 | varchar(50) | No |
| 6 | City | varchar(50) | No |
| 7 | State | char(2) | No |
| 8 | Zip | varchar(10) | No |
| 9 | Phone | varchar(25) | No |
| 10 | Fax | varchar(20) | No |
| 11 | Email | varchar(255) | No |

#### vw_WinningMSRPEntryPrices {view-dbo-vw-winningmsrpentryprices}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2013-12-12 15:03:09.433000 |
| **Modified** | 2018-01-21 20:26:47.130000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | BidHeaderId | int | Yes |
| 2 | VendorId | int | Yes |
| 3 | ManufacturerId | int | Yes |
| 4 | ManufacturerProductLineId | int | Yes |
| 5 | MSRPOptionId | int | Yes |
| 6 | RangeBase | money | Yes |
| 7 | RangeValue | decimal(9,5) | Yes |
| 8 | BidMSRPResultPricesId | int | No |
| 9 | BidMSRPResultsProductLineId | int | No |
| 10 | BidMSRPResultsId | int | No |

#### vw_ZonalItems {view-dbo-vw-zonalitems}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2014-04-11 16:34:33.023000 |
| **Modified** | 2025-10-27 20:12:50.647000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | CaptureName | nvarchar(50) | No |
| 2 | Folder | nvarchar(260) | Yes |
| 3 | CatalogName | nvarchar(50) | No |
| 4 | DocCategory | nvarchar(50) | No |
| 5 | DocType | nvarchar(50) | No |
| 6 | DocTypeFieldId | uniqueidentifier | No |
| 7 | TopLeftX | decimal(8,2) | Yes |
| 8 | TopLeftY | decimal(8,2) | Yes |
| 9 | TopRightX | decimal(9,2) | Yes |
| 10 | TopRightY | decimal(8,2) | Yes |
| 11 | BottomLeftX | decimal(8,2) | Yes |
| 12 | BottomLeftY | decimal(9,2) | Yes |
| 13 | BottomRightX | decimal(9,2) | Yes |
| 14 | BottomRightY | decimal(9,2) | Yes |
| 15 | ZonalRemovePage | bit | No |
| 16 | UseRegularExpression | bit | Yes |
| 17 | RegularExpression | nvarchar(1500) | Yes |
| 18 | DocTypeFieldRecognitionZoneId | uniqueidentifier | No |
| 19 | ScanJobId | int | No |

#### vw_scARCategories {view-dbo-vw-scarcategories}

| Property | Value |
|----------|-------|
| **Schema** | dbo |
| **Created** | 2009-09-25 16:31:20.013000 |
| **Modified** | 2018-01-21 20:26:48.377000 |

| # | Column | Type | Nullable |
|---|--------|------|----------|
| 1 | SessionId | int | No |
| 2 | DistrictId | int | No |
| 3 | BudgetId | int | No |
| 4 | CategoryId | int | No |
| 5 | Name | varchar(50) | Yes |

