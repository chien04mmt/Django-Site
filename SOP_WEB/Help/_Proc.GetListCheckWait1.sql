USE [SOP_V2]
GO
/****** Object:  StoredProcedure [dbo].[sp_GetListCheckWait1]    Script Date: 08/30/2022 09:37:48 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
ALTER PROCEDURE [dbo].[sp_GetListCheckWait1]
	@Department as nvarchar(10),
	@CodeDocument nvarchar(50),
	@DocumentNo nvarchar(50),
	@CheckWait nvarchar(50),
	@Code_Name nvarchar(50),
	@CreatedBy nvarchar(50),
	@ToDate datetime,
	@FromDate datetime
AS
	

	declare @order int
	declare @doc nvarchar(50)
	declare @order1 int
	declare @doc1 nvarchar(50)
	declare @min int
	declare @user varchar(50)
	declare @user1 varchar(50)

	if not exists (select * from INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='TheSchema' and TABLE_NAME='#tam')
		begin
			create table #tam (
				CodeDocument varchar(50),
				Orders int,
				UserName varchar(50)
				)
		end

	delete #tam



		if not exists (select * from INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='TheSchema' and TABLE_NAME='#TEMPX')
		begin
			create table #TEMPX (
				CodeDocument varchar(50),
				Orders int,
				UserName varchar(50)
				)
		end

	delete #TEMPX



	set @order1=0
	set @doc1=''
	set @user1=''
	set @min = 0
	declare @start int
	set @start=0

	declare cursorDocument CURSOR for

			-- tạo bảng chứa dữ liệu 
	select distinct b.CodeDocument
                from    (SELECT 
                        [CodeDocument]
                        ,[Orders]
                        ,[UserName]
                    FROM [ApprovalSection]
                    where UpdatedBy is NULL AND Orders <>1  ) as b               
					order by CodeDocument
	

	open cursorDocument
	fetch next from cursorDocument
	into  @doc
	while @@FETCH_STATUS = 0
	
		BEGIN
			INSERT INTO #TEMPX
			SELECT TOP 1 CodeDocument, Orders,UserName
			 FROM [ApprovalSection] 
			 Where CodeDocument=@doc and UpdatedDate is null order by Orders asc
			

	FETCH NEXT FROM cursorDocument
	into @doc
	END

	CLOSE cursorDocument
	DEALLOCATE cursorDocument
	
	
	
	-- con tror 2 
	declare cursorDocument CURSOR for

			-- tạo bảng chứa dữ liệu 
	select distinct b.CodeDocument
                from    (SELECT 
                        [CodeDocument]
                        ,[Orders]
                        ,[UserName]
                    FROM [ApprovalSection]
					WHERE UpdatedBy is not null and Station='DCC' ) as b               
					order by CodeDocument
	

	open cursorDocument
	fetch next from cursorDocument
	into  @doc
	while @@FETCH_STATUS = 0
	
		BEGIN
			INSERT INTO #TEMPX
			SELECT TOP 1 CodeDocument, Orders,UserName
			 FROM [ApprovalSection] 
			 Where CodeDocument=@doc and UpdatedBy is not null and Station='DCC'  order by Orders asc
			

	FETCH NEXT FROM cursorDocument
	into @doc
	END

	CLOSE cursorDocument
	DEALLOCATE cursorDocument
	


declare @sql as nvarchar(max)

set @sql=''

--'C-00046'' --Đơn xin mã
--'C-00048'' --Đơn sửa văn bản
--'C-00047'' --Đơn Phát hành
--'C-00049' --Đơn hủy văn bản
--'C-00050' --Đơn Hủy mã		
										
set @sql+=N'
 SELECT tb.*,u.HoTen as CheckWait,u1.HoTen as CreatedBy1, CASE
										WHEN tb.CodeDocument like ''%SOP-A%'' THEN ''C-00046''
										WHEN tb.CodeDocument like ''%SOP-B%'' THEN ''C-00048''
										WHEN tb.CodeDocument like ''%SOP-C%'' THEN ''C-00047''
										WHEN tb.CodeDocument like ''%SOP-D%'' THEN ''C-00049''
										WHEN tb.CodeDocument like ''%SOP-G%'' THEN ''C-00050'' 							
										ELSE ''''
									END as Code_Name
 FROM (
 SELECT r.CancelDocument as CodeDocument,r.Department,r.States,r.EffectiveDate,r.CreatedDate,r.CreatedBy,r.DocNo_DCC as DocumentNo FROM RegisterCancelDocument as r
 UNION ALL  SELECT rc.CodeDocument as CodeDocument,rc.Department,rc.States,rc.EffectiveDate,rc.CreatedDate,rc.CreatedBy,pl.DocumentNo FROM RegisterCodeDocument as rc
 left JOIN RegisterPublishDocument as pl on rc.CodeDocument=pl.CodeDocument
 UNION ALL  SELECT re.EditDocument as CodeDocument,re.Department,re.States,re.EffectiveDate,re.CreatedDate,re.CreatedBy,re.DocumentNo FROM RegisterEditDocument as re
 UNION ALL  SELECT rp.PublishDocument as CodeDocument,rp.Department,rp.States,rp.EffectiveDate,rp.CreatedDate,rp.CreatedBy,rp.DocumentNo FROM RegisterPublishDocument as rp
 UNION ALL  SELECT rn.RenewalCode as CodeDocument,rn.Department,rn.States,rn.EffectiveDate,rn.CreatedDate,rn.CreatedBy,rn.DocumentNo FROM RenewalsDocument as rn) as tb
 LEFT JOIN  #TEMPX as tb1 on tb.CodeDocument=tb1.CodeDocument
 LEFT JOIN Users as u on u.TenDangNhap= tb1.UserName
 LEFT JOIN Users as u1 on tb.CreatedBy= u1.TenDangNhap '

if (@Department<>'') begin set @sql+='WHERE tb.Department='''+@Department+'''' end
if (@Department='') begin set @sql+='WHERE tb.Department is not null ' end

if (@CodeDocument<>'') begin set @sql+=' and tb.CodeDocument='''+@CodeDocument+'''' end
if (@CheckWait<>'') begin set @sql+=' and tb.CheckWait='''+@CheckWait+'''' end
if (@DocumentNo<>'') begin set @sql+=' and tb.DocumentNo='''+@DocumentNo+'''' end
if (@Code_Name<>'') begin set @sql+=' and tb.Code_Name='''+@Code_Name+'''' end
if (@CreatedBy<>'') begin set @sql+=' and tb.CreatedBy='''+@CreatedBy+'''' end
if (@ToDate<>'' and @FromDate<>'') begin set @sql+=' and tb.CreatedDate between '''+CONVERT(char(10),@Todate,111)+''' and '''+CONVERT(char(10),@FromDate,111)+'''' end


set @sql+=' order by tb.CreatedDate desc'
--print(@sql)
exec(@sql)
	--@Department as nvarchar(10),
	--@CodeDocument nvarchar(50),
	--@DocumentNo nvarchar(50),
	--@CheckWait nvarchar(50),
	--@Code_Name nvarchar(50),
	--@CreatedBy nvarchar(50),
	--@ToDate datetime,
	--@FromDate datetime
	
-- exec sp_GetListCheckWait1 'C-00015'
-- exec sp_GetListCheckWait1 'C-00015','','','','','V0515000','2022-08-13','2022-08-30'



