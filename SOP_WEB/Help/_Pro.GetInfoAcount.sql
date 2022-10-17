
USE SOP_V2
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<V0515000,,Chiến>
-- Create date: <13.08.2022,,>
-- Description:	<Lấy thông tin tài khoản,,>
-- =============================================
CREATE PROCEDURE sp_GetInfoAcount(
	@TenDangNhap nvarchar(50)
)
	
AS
BEGIN
	if(@TenDangNhap='')
		BEGIN
			SELECT * FROM [SOP_V2].[dbo].[Users1]
		END
	if(@TenDangNhap<>'')
		BEGIN
			SELECT * FROM [SOP_V2].[dbo].[Users1] WHERE TenDangNhap=@TenDangNhap
		END
END
GO
