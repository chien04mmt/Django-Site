-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE sp_InsertOrUpdateRegisterCancelDocument
	@CancelDocument varchar(50),
	@ApplicationDate varchar(50),
	@EffectiveDate varchar(50),
	@ApplicationSite varchar(50),
	@CloseDocument varchar(50),
	@ApplicationNo_Code varchar(50),
	@DocNo_DCC varchar(50),
	@ReasonOfApplication varchar(50),
	@States varchar(50),
	@CreatedBy varchar(50),
	@Department varchar(50),
	@Action varchar(50)
		
AS
BEGIN
	if (@Action='UPDATE')
		BEGIN			
            UPDATE RegisterCancelDocument 
				SET EffectiveDate=@EffectiveDate,ApplicationSite=@ApplicationSite,CloseDocument=@CloseDocument,
					ApplicationNo_Code=@ApplicationNo_Code,DocNo_DCC=@DocNo_DCC,ReasonOfApplication=@ReasonOfApplication,
					States=@States,UpdatedBy=@CreatedBy,UpdatedDate=GETDATE(),IsDeleted='0',Department=@Department
		END
		
	if (@Action='INSERT')
		BEGIN
			insert into RegisterCancelDocument
                            (ID, CancelDocument, ApplicationDate, EffectiveDate, ApplicationSite, CloseDocument,
                            ApplicationNo_Code, DocNo_DCC, ReasonOfApplication, States, CreatedBy, CreatedDate, IsDeleted, Department)
                 values(NEWID(), @CancelDocument, @ApplicationDate, @EffectiveDate, @ApplicationSite, @CloseDocument, @ApplicationNo_Code,
                        @DocNo_DCC, @ReasonOfApplication, @States, @CreatedBy, GETDATE(), 0, @Department)
                        
                declare @CodeDocument varchar(50)
                select top 1 @CodeDocument=CodeDocument from RegisterCodeDocument where CodeDocument=@ApplicationNo_Code
                update DCC_Ref set [Status] ='2' where CodeDocument =@CodeDocument  and DocNo =@DocNo_DCC
		END	
END
GO
