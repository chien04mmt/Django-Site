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
CREATE PROCEDURE dbo.sp_InsertRegisterCode(
	@CodeDocument varchar(50),
	@CreatedBy varchar(50),
	@ApplicationSite varchar(20),
	@EffectiveDate datetime,
	@ReasonApplication nvarchar(500),
	@ApplicableSite nvarchar(1000),
	@ApplicableBU nvarchar(1000),	
	@Department varchar(50)	,
	@action varchar(50)
)
AS
BEGIN	
declare @Type varchar(50)
declare @IsDeleted bit
declare @Status varchar(50)
declare @States varchar(50)
declare @DocumentType varchar(20)

	set @DocumentType=''
	set @Status='A01'
	set @States=''
	set @Type='1'
	set @IsDeleted='0'
	
	
	if(@action='CREATE')
		Begin
			 Insert Into [SOP_V2].[dbo].[RegisterCodeDocument]
			([ID],[CodeDocument],[CreatedDate],[CreatedBy],[ApplicationSite]
			  ,[EffectiveDate],[DocumentType],[ReasonApplication],[ApplicableSite],[ApplicableBU]
			  ,[IsDeleted],[Status],[States],[CheckWait],[ApplicationDate]
			  ,[Type],[Department])

			  Values
			  (NEWID(),@CodeDocument,getdate(),@CreatedBy,@ApplicationSite,
			  @EffectiveDate,@DocumentType,@ReasonApplication,@ApplicableSite,@ApplicableBU,
			  @IsDeleted,@Status,@States,'',getdate(),
			  @Type,@Department)
		END




	if(@action='UPDATE')
		Begin
			   UPDATE RegisterCodeDocument 
			   SET ApplicationSite=@ApplicationSite,
				   EffectiveDate=@EffectiveDate,
				   DocumentType=@DocumentType,			   
				   ReasonApplication=@ReasonApplication,
				   ApplicableSite=@ApplicableSite,
				   ApplicableBU=@ApplicableBU,
				   UpdatedDate=GETDATE(),
				   UpdatedBy=@CreatedBy,
				   Status=@Status,
				   States=@States,
				   Department=@Department,
				   ApplicationDate=getdate()
               WHERE CodeDocument = @CodeDocument
		End
      
END
GO


-- exec sp_InsertRegisterCode '@CodeDocument',
--	'@CreatedBy','@ApplicationSite',@EffectiveDate',
--  '@ReasonApplication','@ApplicableSite','@ApplicableBU','@Department'