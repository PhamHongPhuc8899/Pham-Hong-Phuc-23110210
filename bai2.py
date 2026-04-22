def chuan_hoa_ten(name):
    """
    Chuẩn hóa chuỗi: bỏ khoảng trắng thừa và viết hoa chữ cái đầu mỗi từ.
    """
    # split() không tham số sẽ tự động tách theo mọi khoảng trắng và loại bỏ khoảng trắng thừa
    cac_tu = name.split()
    # Viết hoa chữ cái đầu của từng từ và nối lại bằng một khoảng trắng duy nhất
    ten_chuan_hoa = " ".join(tu.capitalize() for tu in cac_tu)
    return ten_chuan_hoa

def sap_xep_theo_ten(danh_sach):
    """
    Sắp xếp danh sách dựa trên Tên (từ cuối cùng trong chuỗi).
    """
    # Sử dụng hàm sorted với key là từ cuối cùng của chuỗi đã chuẩn hóa
    danh_sach_sap_xep = sorted(danh_sach, key=lambda x: x.split()[-1])
    return danh_sach_sap_xep

# --- Thực thi chương trình ---
danh_sach_tho = ["  nguYen vaN a  ", "tRAn tHi b", "  le  hoang   Anh ", "pham minh   tuan  "]

# 1. Chuẩn hóa dữ liệu
danh_sach_sach = [chuan_hoa_ten(ten) for ten in danh_sach_tho]

# 2. Sắp xếp theo Tên
danh_sach_cuoi_cung = sap_xep_theo_ten(danh_sach_sach)

# 3. Xuất kết quả
print("Danh sách sau khi chuẩn hóa và sắp xếp theo Tên:")
for i, ten in enumerate(danh_sach_cuoi_cung, 1):
    print(f"{i}. {ten}")