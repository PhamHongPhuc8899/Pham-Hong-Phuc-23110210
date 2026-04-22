def nhap_du_lieu():
    """Hàm nhập danh sách chi tiêu từ bàn phím."""
    danh_sach_chi_tieu = []
    print("--- Nhập danh sách chi tiêu (Nhập 'thoat' tại tên món hàng để dừng) ---")
    
    while True:
        ten = input("Tên món hàng: ").strip()
        if ten.lower() == 'thoat':
            break
        
        try:
            gia = float(input(f"Giá tiền của '{ten}': "))
            danh_sach_chi_tieu.append({"ten": ten, "gia": gia})
        except ValueError:
            print("Lỗi: Vui lòng nhập số tiền hợp lệ!")
            
    return danh_sach_chi_tieu

def xu_ly_du_lieu(danh_sach):
    """Tính tổng và tìm món hàng đắt nhất."""
    if not danh_sach:
        return 0, None

    tong_tien = sum(item['gia'] for item in danh_sach)
    # Tìm món hàng có giá cao nhất bằng hàm max()
    mon_dat_nhat = max(danh_sach, key=lambda x: x['gia'])
    
    return tong_tien, mon_dat_nhat

def xuat_file(danh_sach, tong_tien, mon_dat_nhat, filename="chi_tieu.txt"):
    """Ghi kết quả ra file .txt."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("--- DANH SÁCH CHI TIÊU ---\n")
            for item in danh_sach:
                f.write(f"- {item['ten']}: {item['gia']:,} VNĐ\n")
            
            f.write("-" * 30 + "\n")
            f.write(f"Tổng cộng: {tong_tien:,} VNĐ\n")
            if mon_dat_nhat:
                f.write(f"Món hàng đắt nhất: {mon_dat_nhat['ten']} ({mon_dat_nhat['gia']:,} VNĐ)\n")
        print(f"\nĐã xuất kết quả thành công ra file '{filename}'!")
    except Exception as e:
        print(f"Có lỗi khi ghi file: {e}")

# --- Chương trình chính ---
def main():
    ds = nhap_du_lieu()
    
    if ds:
        tong, dat_nhat = xu_ly_du_lieu(ds)
        
        # Hiển thị nhanh ra màn hình
        print("\n--- KẾT QUẢ ---")
        print(f"Tổng tiền: {tong:,} VNĐ")
        print(f"Món đắt nhất: {dat_nhat['ten']} với {dat_nhat['gia']:,} VNĐ")
        
        # Xuất file
        xuat_file(ds, tong, dat_nhat)
    else:
        print("Danh sách trống, không có dữ liệu để xử lý.")

if __name__ == "__main__":
    main()