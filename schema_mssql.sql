-- MS SQL Server schema for simple shop
IF DB_ID('ShopDB') IS NOT NULL
BEGIN
    ALTER DATABASE ShopDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE ShopDB;
END;
GO
CREATE DATABASE ShopDB;
GO
USE ShopDB;
GO

CREATE TABLE dbo.Customers(
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    full_name NVARCHAR(150) NOT NULL,
    email NVARCHAR(100)
);

CREATE TABLE dbo.Products(
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name NVARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

CREATE TABLE dbo.Orders(
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    order_date DATE NOT NULL,
    CONSTRAINT FK_Orders_Customers FOREIGN KEY (customer_id) REFERENCES dbo.Customers(customer_id),
    CONSTRAINT FK_Orders_Products FOREIGN KEY (product_id) REFERENCES dbo.Products(product_id)
);

INSERT INTO dbo.Customers(full_name,email) VALUES
(N'Иван Иванов', N'ivan@example.com'),
(N'Анна Смирнова', N'anna@example.com');

INSERT INTO dbo.Products(product_name,price) VALUES
(N'Ноутбук', 55000.00),
(N'Смартфон', 30000.00);

INSERT INTO dbo.Orders(customer_id,product_id,order_date) VALUES
(1,1,'2025-09-21'),
(2,2,'2025-09-22');
GO
