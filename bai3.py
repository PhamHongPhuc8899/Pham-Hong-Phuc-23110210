def chuyen_doi_nhiet_do():
    print("\n--- Chuyển đổi Nhiệt độ ---")
    print("1. Từ độ C sang độ F")
    print("2. Từ độ F sang độ C")
    
    try:
        chon = input("Lựa chọn của bạn (1/2): ")
        if chon == '1':
            c = float(input("Nhập độ C: "))
            f = (c * 9/5) + 32
            print(f"==> {c}°C = {f:.2f}°F")
        elif chon == '2':
            f = float(input("Nhập độ F: "))
            c = (f - 32) * 5/9
            print(f"==> {f}°F = {c:.2f}°C")
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số thực cho nhiệt độ!")

def chuyen_doi_tien_te():
    print("\n--- Chuyển đổi Tiền tệ (USD -> VND) ---")
    try:
        usd = float(input("Nhập số tiền USD cần chuyển: "))
        ty_gia = float(input("Nhập tỷ giá hiện tại (1 USD = ? VND): "))
        
        if usd < 0 or ty_gia < 0:
            print("Lỗi: Số tiền và tỷ giá không thể âm!")
            return

        vnd = usd * ty_gia
        print(f"==> {usd:,.2f} USD = {vnd:,.0f} VND")
    except ValueError:
        print("Lỗi: Bạn phải nhập vào một con số!")

def main():
    while True:
        print("\n" + "="*25)
        print("   CÔNG CỤ CHUYỂN ĐỔI")
        print("="*25)
        print("1. Chuyển đổi nhiệt độ")
        print("2. Chuyển đổi tiền tệ (USD-VND)")
        print("3. Thoát")
        
        chon = input("Chọn chức năng (1-3): ")
        
        if chon == '1':
            chuyen_doi_nhiet_do()
        elif chon == '2':
            chuyen_doi_tien_te()
        elif chon == '3':
            print("Cảm ơn bạn đã sử dụng ứng dụng!")
            break
        else:
            print("Vui lòng chọn từ 1 đến 3.")

if __name__ == "__main__":
    main()