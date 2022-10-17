-- ================================================
--Insert RegisterCode
-- ================================================
Use SOP_V2
Go
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.sp_UpdateRegisterCode(
	@CodeDocument varchar(50),
	@ApplicationSite varchar(20),
	@EffectiveDate datetime,
	@DocumentType varchar(20),
	@ReasonApplication nvarchar(500),	
	@ApplicableSite nvarchar(1000),
	@ApplicableBU nvarchar(1000),	
	@UpdatedBy varchar(50),
	@Department varchar(50)	
)
AS
BEGIN	
declare @Type varchar(50)
declare @IsDeleted bit
declare @Status varchar(50)
declare @States varchar(50)

	set @Status='A01'
	set @States=''
	set @Type='1'
	set @IsDeleted='0'
      
      update RegisterCodeDocument 
      set	ApplicationSite=@ApplicationSite,
			EffectiveDate=@EffectiveDate,
			DocumentType=@DocumentType,
			ReasonApplication=@ReasonApplication,
			ApplicableSite=@ApplicableSite,
			ApplicableBU=@ApplicableBU,
			UpdatedDate=GETDATE(),
			UpdatedBy=@UpdatedBy,
			Status=@Status,
			States=@States,
			Department=@Department
      where CodeDocument=@CodeDocument
      
END
GO


-- exec sp_UpdateRegisterCode '@CodeDocument',
--	'@ApplicationSite',@EffectiveDate','@DocumentType',
--  '@ReasonApplication','@ApplicableSite','@ApplicableBU',@UpdatedBy,'@Department'