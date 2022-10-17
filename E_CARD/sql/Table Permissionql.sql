USE [DIEUXE]
GO

/****** Object:  Table [dbo].[EPERMISSION_USER]    Script Date: 06/10/2022 11:17:48 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[EPERMISSION_USER](
-- THông tin user
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[USER_ID] [nchar](10) NOT NULL,
	[PERMISS_TYPE] [nchar](30) NULL,
	
-- TẠO ĐƠN: danh sách FORM, tạo đơn
	[LIST_FORM] [decimal](2, 0) NULL,
	[NEW_BUS] [decimal](2, 0) NULL,
	
-- HÒM THƯ: đơn chờ ký, đơn đã tạo, đơn lưu trữ
	[APPROVAL] [decimal](2, 0) NULL,
	[MY_DOC] [decimal](2, 0) NULL,
	[ARCHIVED_DOC] [decimal](2, 0) NULL,
	
-- QUẢN LÝ HỆ THỐNG: Cài đặt tham số, quản lý tài khoản, tổ chức dữ liệu, thông tin cá nhân
	[PARA_SETING] [decimal](2, 0) NULL,
	[USER_MANAGE] [decimal](2, 0) NULL,
	[DATA_ORGANIZATION] [decimal](2, 0) NULL,
	[PROFILE_SETING] [decimal](2, 0) NULL,
	
--DỮ LIỆU HOẠT ĐỘNG: thông tin lái xe, thông tin xe, kiểm phiếu, điều động, tổ chức đăng ký, yêu cầu mẫu đơn, thống kê thông tin sử dụng
	[DRIVER_INF] [decimal](2, 0) NULL,
	[CAR_INF] [decimal](2, 0) NULL,
	[FORM_APPLY] [decimal](2, 0) NULL,
	[VEHICLE_SCHE] [decimal](2, 0) NULL,
	[FORM_ORGANI] [decimal](2, 0) NULL,
	[FORM_QUERY] [decimal](2, 0) NULL,
	[VEHICLE_USAGE] [decimal](2, 0) NULL,
	
	
-- THông tin quyền hạn
	[CREATED_BY] [nchar](30) NULL,
	[CREATED_AT] [datetime] NULL,
	[EXPIRATION_DATE] [datetime] NULL
) ON [PRIMARY]

GO


