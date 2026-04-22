import matplotlib.pyplot as plt

# 1. Dữ liệu đầu vào
sales_data = {'Laptop': 10, 'Mouse': 50, 'Keyboard': 30}
price_list = {'Laptop': 15000000, 'Mouse': 200000, 'Keyboard': 500000}

def tao_bao_cao(sales, prices):
    print(f"{'Mặt hàng':<15} | {'Số lượng':<10} | {'Doanh thu (VNĐ)':<15}")
    print("-" * 45)
    
    tong_doanh_thu = 0
    doanh_thu_tung_mon = {}

    for item, quantity in sales.items():
        # Tính doanh thu từng món
        thanh_tien = quantity * prices.get(item, 0)
        doanh_thu_tung_mon[item] = thanh_tien
        tong_doanh_thu += thanh_tien
        
        print(f"{item:<15} | {quantity:<10} | {thanh_tien:,.0f}")

    print("-" * 45)
    print(f"TỔNG DOANH THU: {tong_doanh_thu:,.0f} VNĐ\n")
    return tong_doanh_thu

def ve_bieu_do(sales):
    # Lấy danh sách tên mặt hàng và số lượng
    items = list(sales.keys())
    quantities = list(sales.values())

    # Cấu hình biểu đồ
    plt.figure(figsize=(8, 6))
    bars = plt.bar(items, quantities, color=['#3498db', '#e74c3c', '#2ecc71'])

    # Thêm tiêu đề và nhãn
    plt.title('BÁO CÁO SỐ LƯỢNG SẢN PHẨM ĐÃ BÁN', fontsize=14, fontweight='bold')
    plt.xlabel('Sản phẩm', fontsize=12)
    plt.ylabel('Số lượng (Cái)', fontsize=12)

    # Hiển thị số liệu trên đầu mỗi cột
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, yval, ha='center', va='bottom')

    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()

# --- Chạy chương trình ---
if __name__ == "__main__":
    tong = tao_bao_cao(sales_data, price_list)
    ve_bieu_do(sales_data)