import random
import os

# Đường dẫn file lưu kỷ lục
KY_LUC_FILE = "ky_luc.txt"

def doc_ky_luc():
    """Đọc số lần đoán ít nhất từ file."""
    if os.path.exists(KY_LUC_FILE):
        with open(KY_LUC_FILE, "r") as f:
            content = f.read().strip()
            return int(content) if content else 999
    return 999

def luu_ky_luc(so_lan):
    """Lưu kỷ lục mới nếu người chơi thắng với ít lượt hơn."""
    ky_luc_cu = doc_ky_luc()
    if so_lan < ky_luc_cu:
        with open(KY_LUC_FILE, "w") as f:
            f.write(str(so_lan))
        return True
    return False

def goi_y(so_can_tim):
    """Cung cấp gợi ý về tính chất của số."""
    print("--- GỢI Ý ---")
    if so_can_tim % 2 == 0:
        print("Mẹo: Số cần tìm là một số CHẴN.")
    else:
        print("Mẹo: Số cần tìm là một số LẺ.")
    
    if so_can_tim > 50:
        print("Mẹo: Số này nằm trong khoảng từ 51 đến 100.")
    else:
        print("Mẹo: Số này nằm trong khoảng từ 1 đến 50.")

def tro_choi():
    so_may_chon = random.randint(1, 100)
    so_luot_toi_da = 7
    so_lan_doan = 0
    thang = False
    
    ky_luc_hien_tai = doc_ky_luc()
    print("="*30)
    print(" CHÀO MỪNG ĐẾN VỚI TRÒ CHƠI ĐOÁN SỐ ")
    print(f"Kỷ lục hiện tại: {ky_luc_hien_tai if ky_luc_hien_tai != 999 else 'Chưa có'} lượt")
    print("Máy đã chọn một số từ 1 đến 100. Bạn có 7 lượt!")
    print("="*30)

    while so_lan_doan < so_luot_toi_da:
        so_lan_doan += 1
        try:
            doan = int(input(f"\nLượt {so_lan_doan}/{so_luot_toi_da} - Nhập số bạn đoán: "))
            
            if doan < 1 or doan > 100:
                print("Vui lòng chỉ đoán số trong khoảng từ 1 đến 100!")
                so_lan_doan -= 1 # Không tính lượt nếu nhập sai khoảng
                continue

            if doan == so_may_chon:
                print(f" CHÚC MỪNG! Bạn đã đoán đúng số {so_may_chon} ở lượt thứ {so_lan_doan}!")
                thang = True
                break
            elif doan < so_may_chon:
                print("Kết quả: LỚN HƠN")
            else:
                print("Kết quả: NHỎ HƠN")
            
            # Cung cấp gợi ý ở lượt thứ 3 nếu chưa đúng
            if so_lan_doan == 3:
                goi_y(so_may_chon)

        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
            so_lan_doan -= 1

    if thang:
        if luu_ky_luc(so_lan_doan):
            print(f" KỶ LỤC MỚI! Bạn là người chơi xuất sắc nhất với {so_lan_doan} lượt.")
    else:
        print(f"\n Bạn đã hết lượt! Số của máy là: {so_may_chon}. Chúc bạn may mắn lần sau!")

if __name__ == "__main__":
    while True:
        tro_choi()
        tiep_tuc = input("\nBạn có muốn chơi lại không? (c/k): ").lower()
        if tiep_tuc != 'c':
            print("Tạm biệt!")
            break