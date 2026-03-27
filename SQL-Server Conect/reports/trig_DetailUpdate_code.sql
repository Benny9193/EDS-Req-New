CREATE TRIGGER [dbo].[trig_DetailUpdate] on [dbo].[Detail] 
after INSERT, UPDATE not for replication
AS
set nocount on
declare @BidsList table (RequisitionId int, BidHeaderId int null)
declare @CatPrices table (sysid int identity(1,1) not null primary key, DetailId int, BidHeaderId int, BidId int, CrossRefId int, CatalogYear char(4), NetPrice money, DiscountRate decimal(9,5))
declare @FrozenReqs table (RequisitionId int not null primary key)

if update(LastAlteredSessionId) or update(SessionId)
begin
  Update Detail
     set SessionId = case when inserted.SessionId is null then inserted.LastAlteredSessionId else inserted.SessionId end,
         LastAlteredSessionId = case when inserted.LastAlteredSessionId is null then inserted.SessionId else inserted.LastAlteredSessionId end
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
end

if update(ItemId) or update(BidHeaderId) or update(Reproc)
begin
  -- Build Base List of Bids for each Requisition
  insert @BidsList (RequisitionId, BidHeaderId)
    select Requisitions.RequisitionId, Requisitions.BidHeaderId
      from inserted
      join Detail on Detail.DetailId = inserted.DetailId
      join Requisitions on Requisitions.RequisitionId = isnull(inserted.RequisitionId, Detail.RequisitionId)
     group by Requisitions.RequisitionId, Requisitions.BidHeaderId
   
  -- Add All other bids needed to list
  while @@rowcount != 0
  begin
	-- Add Parent PreBids
	insert @BidsList (RequisitionId, BidHeaderId)
	  select Requisitions.RequisitionId, BidHeaders.BidHeaderId
		from Requisitions with (nolock)
		join @BidsList bl on bl.RequisitionId = Requisitions.RequisitionId
		join Budgets on Budgets.BudgetId = Requisitions.BudgetId
		join Category on Category.CategoryId = Requisitions.CategoryId
		join BidHeaders on BidHeaders.CategoryId = Requisitions.CategoryId
		               and BidHeaders.Active = 1
		               and BidHeaders.ParentBidHeaderId = bl.BidHeaderId
 		               and isnull(BidHeaders.DistrictId,0) = case isnull(BidHeaders.BidType,1) when 2 then Budgets.DistrictId else isnull(BidHeaders.DistrictId,0) end
					   and getdate() between BidHeaders.EffectiveFrom and BidHeaders.EffectiveUntil
		join PPCategory on PPCategory.PricePlanId = BidHeaders.PricePlanId
				       and PPCategory.CategoryId = BidHeaders.CategoryId
		join DistrictPP on DistrictPP.PricePlanId = BidHeaders.PricePlanId
					   and DistrictPP.DistrictId = Budgets.DistrictId
		left outer join @BidsList ble on ble.RequisitionId = Requisitions.RequisitionId
		                             and ble.BidHeaderId = BidHeaders.BidHeaderId
	   where BidHeaders.PricePlanId = DistrictPP.PricePlanId
	     and ble.BidHeaderId is null
	   group by Requisitions.RequisitionId, BidHeaders.BidHeaderId
  end

  -- Build List of Frozen Reqs
  insert @FrozenReqs (RequisitionId)
	select Requisitions.RequisitionId
	  from inserted
      join Detail on Detail.DetailId = inserted.DetailId
      join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
	  outer apply (Select top 1 PO.POId from PO where PO.RequisitionId = Requisitions.RequisitionId) p
	  outer apply (Select top 1 Approvals.ApprovalId from Approvals where Approvals.RequisitionId = Requisitions.RequisitionId and Approvals.StatusId in (6,35,45,49)) ap
	 where p.POId is not null
	    or ap.ApprovalId is not null
	 group by Requisitions.RequisitionId

  -- Remap items with new Id's
  Update Detail
     set ItemId = MappedItems.NewItemId,
         OriginalItemId = coalesce(Detail.OriginalItemId,MappedItems.OrigItemId),
         Modified = getdate()
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join MappedItems on MappedItems.OrigItemId = coalesce(inserted.ItemId, Detail.ItemId)
                    and MappedItems.NewItemId != coalesce(inserted.ItemId, Detail.ItemId)
   where not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
/*
    left outer join PO on PO.RequisitionId = Requisitions.RequisitionId
   where PO.POId is null
*/
  -- Bid specific Remap items with new Id's
/* Disabled to 9/6/2018 to allow new lookup code to work correctly
  Update Detail
     set ItemId = BidMappedItems.NewItemId,
         OriginalItemId = coalesce(Detail.OriginalItemId,BidMappedItems.OrigItemId),
         Modified = getdate()
    from inserted
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join BidHeaders on BidHeaders.BidHeaderId in (select case coalesce(Detail.BidHeaderId,0) when 0 then bl.BidHeaderId else Detail.BidHeaderId end from @BidsList bl where bl.RequisitionId = Requisitions.RequisitionId group by case coalesce(Detail.BidHeaderId,0) when 0 then bl.BidHeaderId else Detail.BidHeaderId end)
    join BidMappedItems on BidMappedItems.OrigItemId = Detail.ItemId
                       and BidMappedItems.BidHeaderId = BidHeaders.BidHeaderId
                       and BidMappedItems.NewItemId != coalesce(inserted.ItemId, Detail.ItemId)
   where not exists(select PO.POId from PO where PO.RequisitionId = Requisitions.RequisitionId)
*/
/*
    left outer join PO on PO.RequisitionId = Requisitions.RequisitionId
   where PO.POId is null
*/
  -- Reset info for All Items
  Update Detail
     set CatalogId = null,
         BidPrice = null,
         CatalogPrice = null,
         GrossPrice = null,
         DiscountRate = null,
         CatalogPage = null,
         PricePlanId = null,
         AwardId = null,
         VendorId = null,
         VendorItemCode = null,
         Alternate = null,
         BidItemId = null,
         ItemMustBeBid = null,
         CrossRefId = null,
         AdditionalShipping = null,
         Reproc = null
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
   where not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
/*
    left outer join PO on PO.RequisitionId = Requisitions.RequisitionId
   where PO.POId is null
*/
--  insert DebugMsgs (Msg) values ((select Detail.DetailId, Detail.CatalogId, Detail.BidItemId, Detail.BidPrice, Detail.ItemMustBeBid from inserted join Detail on Detail.DetailId = inserted.DetailId for xml auto))
  -- Set Bid Item info if valid and no other prices are set
  Update Detail
     set CatalogId = BestBid.CatalogId,
         BidPrice = BestBid.BidPrice,
         CatalogPrice = BestBid.CatalogPrice,
         GrossPrice = BestBid.GrossPrice,
         DiscountRate = BestBid.DiscountRate,
         CatalogPage = BestBid.Page,
         PricePlanId = BestBid.PricePlanId,
         AwardId = BestBid.AwardId,
         VendorId = BestBid.VendorId,
         VendorItemCode = BestBid.VendorItemCode,
         Alternate = BestBid.Alternate,
         BidItemId = BestBid.BidItemId,
         CrossRefId = BestBid.CrossRefId,
         ItemMustBeBid = 0
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join Category on Category.CategoryId = Requisitions.CategoryId
                 and Category.Type in (1,2,4)
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
	outer apply (select top 1 CrossRefs.CatalogId, 
	                    round(BidItems.Price - round(BidItems.Price * isnull(Bids.BidDiscountRate,0) / 100,2),2) BidPrice, 
						CrossRefs.CatalogPrice, 
						round(BidItems.Price,2) GrossPrice, 
						isnull(Bids.BidDiscountRate,0) DiscountRate,
						CrossRefs.Page,
						BidHeaders.PricePlanId,
						Awards.AwardId,
						Bids.VendorId,
						BidItems.VendorItemCode,
						BidItems.Alternate,
						BidItems.BidItemId,
						BidItems.CrossRefId
				   from BidItems
				   join Bids on Bids.BidId = BidItems.BidId
				            and Bids.Active = 1
				   join BidHeaders on BidHeaders.BidHeaderId = Bids.BidHeaderId
				                  and BidHeaders.BidHeaderId = Bids.BidHeaderId
								  and BidHeaders.BidHeaderId in (select case coalesce(Detail.BidHeaderId,0) 
				                                                          when 0 then bl.BidHeaderId 
																		  else Detail.BidHeaderId 
																		end 
																   from @BidsList bl 
																  where bl.RequisitionId = Requisitions.RequisitionId 
																  group by case coalesce(Detail.BidHeaderId,0) 
																             when 0 then bl.BidHeaderId 
																			 else Detail.BidHeaderId 
																		   end)
				   join Awards on Awards.BidId = Bids.BidId
			       left outer join CrossRefs on CrossRefs.CrossRefId = BidItems.CrossRefId
				  where BidItems.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
				  order by case when isnull(Bids.VendorId,0) in (0,7691) then 1 else 0 end, round(BidItems.Price - round(BidItems.Price * isnull(Bids.BidDiscountRate,0) / 100,2),2)) BestBid
   where Detail.ItemMustBeBid is null
     and BestBid.BidItemId is not null
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)

  -- Set Catalog Prices for Catalog Items
--  insert DebugMsgs (Msg) values ((select Detail.DetailId, Detail.CatalogId, Detail.BidItemId, Detail.BidPrice, Detail.ItemMustBeBid from inserted join Detail on Detail.DetailId = inserted.DetailId for xml auto))
  Update Detail
     set CatalogId = CrossRefs.CatalogId,
         BidPrice = round(case isnull(Crossrefs.DoNotDiscount,0) when 0 then CrossRefs.GrossPrice - round(CrossRefs.GrossPrice * isnull(BidsCatalogList.DiscountRate,0) / 100,2) else Crossrefs.GrossPrice end,2),
         CatalogPrice = CrossRefs.CatalogPrice,
         GrossPrice = round(CrossRefs.GrossPrice,2),
         DiscountRate = case isnull(Crossrefs.DoNotDiscount,0) when 0 then isnull(BidsCatalogList.DiscountRate,0) else 0 end,
         CatalogPage = CrossRefs.Page,
         PricePlanId = BidHeaders.PricePlanId,
         AwardId = Awards.AwardId,
         VendorId = Bids.VendorId,
         VendorItemCode = CrossRefs.VendorItemCode,
         Alternate = null,
         BidItemId = null,
         CrossRefId = CrossRefs.CrossRefId,
         AdditionalShipping = isnull(CrossRefs.AdditionalShipping,0),
         ItemMustBeBid = 0,
		 BidHeaderId = case when BidHeaders.BidHeaderId != Requisitions.BidHeaderId then BidHeaders.BidHeaderId else null end
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = Detail.RequisitionId
    join Category on Category.CategoryId = Requisitions.CategoryId
                 and Category.Type in (1,2,4)
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
    join CrossRefs on CrossRefs.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
                  and CrossRefs.CrossRefId = 
      (select top 1 xr.CrossRefId
         from CrossRefs xr with (nolock)
         join Catalog cat on Cat.CatalogId = xr.CatalogId
         join BidsCatalogList bcl on bcl.CatalogId = Cat.CatalogId
         join Bids b on b.BidId = bcl.BidId
                    and b.Active = 1
         join BidHeaders bh on bh.BidHeaderId = b.BidHeaderId
         join @BidsList bl on bl.RequisitionId = Requisitions.RequisitionId
                          and bl.BidHeaderId = bh.BidHeaderId
        where xr.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
          and xr.Active = 1
        order by case isnull(xr.DoNotDiscount,0) when 0 then xr.GrossPrice - round(xr.GrossPrice * isnull(bcl.DiscountRate,0) / 100,2) else xr.GrossPrice end, xr.CatalogYear desc, xr.CrossRefId
       )
    join BidsCatalogList on BidsCatalogList.BidCatalogId = 
      (select top 1 bcl.BidCatalogId
         from CrossRefs xr with (nolock)
         join Catalog cat on cat.CatalogId = xr.CatalogId
         join BidsCatalogList bcl on bcl.CatalogId = cat.CatalogId
         join Bids b on b.BidId = bcl.BidId
                    and b.Active = 1
         join BidHeaders bh on bh.BidHeaderId = b.BidHeaderId
         join @BidsList bl on bl.RequisitionId = Requisitions.RequisitionId
                          and bl.BidHeaderId = bh.BidHeaderId
        where xr.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
          and xr.Active = 1
        order by case isnull(xr.DoNotDiscount,0) when 0 then xr.GrossPrice - round(xr.GrossPrice * isnull(bcl.DiscountRate,0) / 100,2) else xr.GrossPrice end, xr.CatalogYear desc, xr.CrossRefId
       )
    join Bids on Bids.BidId = BidsCatalogList.BidId
    join BidHeaders on BidHeaders.BidHeaderId = Bids.BidHeaderId
    join Awards on Awards.BidId = Bids.BidId
   where Detail.ItemMustBeBid is null
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
     
  -- Set MSRP Pricing 
  Update Detail
     set CatalogId = CrossRefs.CatalogId,
         BidPrice = coalesce(round(Items.ListPrice - round(Items.ListPrice * isnull(BidManufacturers.DiscountRate,0) / 100,2),2),0),
         CatalogPrice = coalesce(Items.ListPrice,0),
         GrossPrice = coalesce(Items.ListPrice,0),
         DiscountRate = isnull(BidManufacturers.DiscountRate,0),
         CatalogPage = CrossRefs.Page,
         PricePlanId = null,
         AwardId = null,
         VendorId = Bids.VendorId,
         VendorItemCode = case coalesce(rtrim(Items.VendorPartNumber),'') when '' then 'N/A' else Items.VendorPartNumber end,
         Alternate = null,
         BidItemId = null,
         CrossRefId = CrossRefs.CrossRefId,
         AdditionalShipping = isnull(CrossRefs.AdditionalShipping,0),
         ItemMustBeBid = 0
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join Category on Category.CategoryId = Requisitions.CategoryId
                 and Category.Type = 5
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
    join Items on Items.ItemId = Detail.ItemId
    join BidHeaders on BidHeaders.BidHeaderId in (select case coalesce(Detail.BidHeaderId,0) when 0 then bl.BidHeaderId else Detail.BidHeaderId end from @BidsList bl where bl.RequisitionId = Requisitions.RequisitionId group by case coalesce(Detail.BidHeaderId,0) when 0 then bl.BidHeaderId else Detail.BidHeaderId end)
    join Bids on Bids.BidHeaderId = BidHeaders.BidHeaderId
             and Bids.Active = 1
    join BidManufacturers on BidManufacturers.BidId = Bids.BidId
                         and BidManufacturers.ManufacturerId = Items.ManufacturerId
    left outer join CrossRefs on CrossRefs.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
                             and CrossRefs.CrossRefId = 
      (select top 1 xr.CrossRefId
         from CrossRefs xr with (nolock)
         join Catalog cat on Cat.CatalogId = xr.CatalogId
                         and Cat.Active = 1
                         and Cat.CategoryId = Requisitions.CategoryId
        where xr.ItemId = Detail.ItemId
          and xr.Active = 1
        order by case isnull(xr.GrossPrice,0) when 0 then 0 else 1 end desc, xr.CatalogYear desc, isnull(xr.GrossPrice,0), xr.CrossRefId desc) 
   where Detail.ItemMustBeBid is null
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)

  -- Set Addenda item info if valid and no other prices are set
--  insert DebugMsgs (Msg) values ((select Detail.DetailId, Detail.CatalogId, Detail.BidItemId, Detail.BidPrice, Detail.ItemMustBeBid from inserted join Detail on Detail.DetailId = inserted.DetailId for xml auto))
  Update Detail
     set CatalogId = xr.CatalogId,
         BidPrice = round(coalesce(Items.ListPrice, xr.CatalogPrice, xr.GrossPrice / .85,0),2),--round(case coalesce(Items.ListPrice,0) when 0 then coalesce(CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85) else Items.ListPrice end,2),
         CatalogPrice = round(coalesce(Items.ListPrice, xr.CatalogPrice, xr.GrossPrice / .85,0),2),--case coalesce(Items.ListPrice,0) when 0 then coalesce(CrossRefs.CatalogPrice, CrossRefs.GrossPrice) else Items.ListPrice end,
         GrossPrice = round(coalesce(Items.ListPrice, xr.CatalogPrice, xr.GrossPrice / .85,0),2),--round(case coalesce(Items.ListPrice,0) when 0 then coalesce(CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85) else Items.ListPrice end,2),
         DiscountRate = null,
         CatalogPage = xr.Page,
         PricePlanId = null,
         AwardId = null,
         VendorId = null,
         VendorItemCode = null,
         Alternate = null,
         BidItemId = null,
         CrossRefId = null,
         AdditionalShipping = null,
         ItemMustBeBid = 1
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Items on Items.ItemId = Detail.ItemId
--	          and coalesce(Items.DistrictId,0) != 0
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
    join DistrictCategories on DistrictCategories.DistrictId = Budgets.DistrictId
                           and DistrictCategories.CategoryId = Requisitions.CategoryId
                           and DistrictCategories.AllowAddenda = 1
	outer apply (Select top 1 CrossRefs.CrossRefId, Crossrefs.CatalogId, CrossRefs.CatalogPrice, CrossRefs.GrossPrice, CrossRefs.Page
	               from CrossRefs
				   join Catalog on Catalog.CatalogId = CrossRefs.CatalogId
				               and Catalog.Name = 'EDS'
							   and Catalog.Active = 1
				  where CrossRefs.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
				    and CrossRefs.Active = 1
				  order by case isnull(CrossRefs.GrossPrice,0) when 0 then 0 else 1 end desc, CrossRefs.CatalogYear desc, isnull(CrossRefs.GrossPrice,0), CrossRefs.CrossRefId desc) xr
	outer apply (Select top 1 CrossRefs.CrossRefId
	               from CrossRefs
				   join Catalog on Catalog.CatalogId = CrossRefs.CatalogId
				               and Catalog.Name != 'EDS'
							   and Catalog.Active = 1
							   and Catalog.CatalogYear > year(getdate()) - 2000 - 3
				  where CrossRefs.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
				    and CrossRefs.Active = 1) CatCheck
   where Detail.ItemMustBeBid is null
	 and CatCheck.CrossRefId is null
     and (coalesce(Requisitions.BidHeaderId,0) = 0 or coalesce(Items.DistrictId,0) != 0)
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
/*
  Update Detail
     set CatalogId = CrossRefs.CatalogId,
         BidPrice = round(coalesce(Items.ListPrice,CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85,0),2),--round(case coalesce(Items.ListPrice,0) when 0 then coalesce(CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85) else Items.ListPrice end,2),
         CatalogPrice = round(coalesce(Items.ListPrice,CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85,0),2),--case coalesce(Items.ListPrice,0) when 0 then coalesce(CrossRefs.CatalogPrice, CrossRefs.GrossPrice) else Items.ListPrice end,
         GrossPrice = round(coalesce(Items.ListPrice,CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85,0),2),--round(case coalesce(Items.ListPrice,0) when 0 then coalesce(CrossRefs.CatalogPrice, CrossRefs.GrossPrice / .85) else Items.ListPrice end,2),
         DiscountRate = null,
         CatalogPage = CrossRefs.Page,
         PricePlanId = null,
         AwardId = null,
         VendorId = null,
         VendorItemCode = null,
         Alternate = null,
         BidItemId = null,
         CrossRefId = null,
         AdditionalShipping = null,
         ItemMustBeBid = 1
    from inserted
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
    join DistrictCategories on DistrictCategories.DistrictId = Budgets.DistrictId
                           and DistrictCategories.CategoryId = Requisitions.CategoryId
                           and DistrictCategories.AllowAddenda = 1
    join Items on Items.ItemId = Detail.ItemId
    left outer join CrossRefs on CrossRefs.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
                             and CrossRefs.CrossRefId = 
      (select top 1 xr.CrossRefId
         from CrossRefs xr with (nolock)
         join Catalog cat on Cat.CatalogId = xr.CatalogId
                         and Cat.Active = 1
                         and Cat.CategoryId = Requisitions.CategoryId
        where xr.ItemId = Detail.ItemId
          and xr.Active = 1
        order by case isnull(xr.GrossPrice,0) when 0 then 0 else 1 end desc, xr.CatalogYear desc, isnull(xr.GrossPrice,0), xr.CrossRefId desc) 
--    left outer join PO on PO.RequisitionId = Requisitions.RequisitionId
   where Detail.ItemMustBeBid is null
     and not exists(select PO.POId from PO where PO.RequisitionId = Requisitions.RequisitionId)
--     and PO.POId is null
*/
  -- Mark items which did not fall into any of the previous updates as NoBid items
  Update Detail
     set CatalogId = null,
         BidPrice = null,
         CatalogPrice = null,
         GrossPrice = null,
         DiscountRate = null,
         CatalogPage = null,
         PricePlanId = null,
         AwardId = null,
         VendorId = 7691,
         VendorItemCode = null,
         Alternate = null,
         BidItemId = null,
         ItemMustBeBid = 0,
         CrossRefId = null,
         AdditionalShipping = null,
         Reproc = null
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join Budgets on Budgets.BudgetId = Requisitions.BudgetId
   where Detail.ItemMustBeBid is null
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
   
  --Update Common Information 
--  insert DebugMsgs (Msg) values ((select Detail.DetailId, Detail.CatalogId, Detail.BidItemId, Detail.BidPrice, Detail.ItemMustBeBid from inserted join Detail on Detail.DetailId = inserted.DetailId for xml auto))
  Update Detail
     set ItemCode = Items.ItemCode,
         Description = case when datalength(dd.ItemDescription) > 1024 then left(dd.ItemDescription,1021) + '...' else dd.ItemDescription end,
         UnitId = Items.UnitId,
         UnitCode = Units.Code,
         HeadingId = Items.HeadingId,
         KeywordId = Items.KeywordId,
         HeadingTitle = Headings.Title,
         Keyword = Keywords.Keyword,
         SortSeq = Items.SortSeq
    from inserted with (updlock,rowlock)
    join Detail on Detail.DetailId = inserted.DetailId
    join Requisitions on Requisitions.RequisitionId = coalesce(inserted.RequisitionId, Detail.RequisitionId)
    join vw_DetailDescription dd on dd.DetailId = inserted.DetailId
    join Items on Items.ItemId = coalesce(Detail.ItemId, inserted.ItemId)
    left outer join Units on Units.UnitId = Items.UnitId
    left outer join Headings on Headings.HeadingId = Items.HeadingId
    left outer join Keywords on Keywords.KeywordId = Items.KeywordId
   where not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)

--Special Price Freeze Logic for Items already in system for items that were incorrectly priced 4/14/2010 dch
  update Detail
     set BidPrice = fi.OrigBidPrice,
         VendorId = fi.OrigVendorId,
         CatalogId = fi.OrigCatalogId,
         CatalogPrice = fi.OrigCatalogPrice,
         VendorItemCode = fi.OrigVendorItemCode,
         AwardId = fi.OrigAwardId,
		 GrossPrice = fi.OrigBidPrice,
		 DiscountRate = 0,
		 CrossRefId = xr.CrossRefId
    from Detail with (updlock,rowlock)
    join FreezeItems2015 fi on fi.DetailId = Detail.DetailId
    join inserted on inserted.DetailId = Detail.DetailId
	outer apply (select top 1 CrossRefs.CrossRefId from CrossRefs where CrossRefs.CatalogId = fi.CatalogId and CrossRefs.ItemId = Detail.ItemId and CrossRefs.VendorItemCode = fi.VendorItemCode order by CrossRefs.GrossPrice) xr
   where not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Detail.RequisitionId)

-- Price freeze for WB Mason Items 2016
  update Detail
     set BidPrice = fi.GrossPrice,
         VendorItemCode = fi.VendorItemCode,
		 GrossPrice = fi.GrossPrice,
		 DiscountRate = 0,
		 VendorId = fi.VendorId,
		 CatalogPrice = CrossRefs.CatalogPrice,
		 CrossRefId = fi.CrossRefId
    from Detail with (updlock,rowlock)
    join Requisitions on Requisitions.REquisitionId = Detail.RequisitionId
    join FreezeItems fi on fi.ItemId = Detail.ItemId
                       and fi.BidHeaderId = Requisitions.BidHeaderId
                       and fi.VendorId = Detail.VendorId
    join inserted on inserted.DetailId = Detail.DetailId
	left outer join CrossRefs on CrossRefs.CrossRefId = fi.CrossRefId
   where Detail.BidItemId is null
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
   
end

-- Create Notifications if needed
insert DetailNotifications (DetailId, OrigItemId, NewItemId, OrigVendorId, NewVendorId, OrigBidPrice, NewBidPrice)
  select Detail.DetailId, deleted.ItemId, Detail.ItemId, deleted.VendorId, Detail.VendorId, deleted.BidPrice, Detail.BidPrice
    from inserted
	join Detail on Detail.DetailId = inserted.DetailId
	join deleted on deleted.DetailId = inserted.DetailId
   where coalesce(deleted.ItemMustBeBid,0) = 0
     and coalesce(Detail.ItemMustBeBid,0) = 0
     and (   (coalesce(deleted.ItemId,0) != coalesce(Detail.ItemId,0))
          or (coalesce(deleted.VendorId,7691) != coalesce(Detail.VendorId,7691))
	      or (coalesce(deleted.BidPrice,0) != coalesce(Detail.BidPrice,0)))
     and not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Detail.RequisitionId)
   group by Detail.DetailId, deleted.ItemId, Detail.ItemId, deleted.VendorId, Detail.VendorId, deleted.BidPrice, Detail.BidPrice

if update(Quantity) or update(BidPrice) or update(ItemId) or update(BidHeaderId) or update(Reproc) or update(ShippingCost)
begin
 -- Bad trick but only way to solve right now should be fixed correctly dch 11/14/2012
  set Ansi_warnings off
  update Requisitions
     set TotalItemsCost = coalesce((select sum(coalesce(Detail.Quantity,0) * round(coalesce(Detail.BidPrice,0),2)) 
                                    from Detail with (nolock) 
                                    join Requisitions r1 on r1.RequisitionId = Detail.RequisitionId
                                                        and r1.RequisitionId = Requisitions.RequisitionId
--                                    left outer join BidHeaders on BidHeaders.BidHeaderId = case coalesce(Detail.BidHeaderId,0) when 0 then R1.BidHeaderId else Detail.BidHeaderId end
                                   where Detail.RequisitionId = Requisitions.RequisitionId
--                                     and coalesce(Detail.ItemMustBeBid,0) = 0
/*                                   and (   Detail.AddedFromAddenda is not null
                                          or coalesce(BidHeaders.BidType,2) = 1)*/),0)
/* DCH Removed 1/20/2023 and moved to Requisitions trigger
         ShippingCost = (select sum(coalesce(rsc.ShippingCost,0)) 
                           from vw_RequisitionShippingCosts rsc with (nolock) 
                          where rsc.RequisitionId = Requisitions.RequisitionId)
*/
    from Requisitions with (updlock,rowlock)
    join (
      select RequisitionId 
        from inserted 
       union (
         select RequisitionId 
           from deleted)
          ) ss on ss.RequisitionId = Requisitions.RequisitionId
   where not exists(select RequisitionId from @FrozenReqs f where f.RequisitionId = Requisitions.RequisitionId)
  set Ansi_warnings on
end
set nocount off
