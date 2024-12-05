def merge_sort(arr):
    # Listenin eleman sayısı 1'e eşit olduğunda geri dön
    if len(arr) > 1:
        # Listenin yarısını sol ve sağ alt listelere böldük
        mid = len(arr) // 2
        left_list = arr[:mid]
        right_list = arr[mid:]

        # Sol ve sağ alt listeleri sıraladık
        merge_sort(left_list)
        merge_sort(right_list)

        # Sıralanmış iki alt listenin birleştirilmesinı yapıyoruz
        i = j = k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                arr[k] = left_list[i]
                i += 1
            else:
                arr[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            arr[k] = left_list[i]
            i += 1
            k +=1

        while j < len(right_list):
            arr[k] = right_list[j]
            j += 1
            k += 1

# Örnek
arr = [9, 6, 3, 8, 4, 1, 7, 5, 2, 17, 12, 15, 18, 14, 10, 11, 13, 16]
# İlk hali yazılıyor
print("Girdi: ", arr)

# Üç parçaya böl
size = len(arr) // 3
part1 = arr[:size]
part2 = arr[size:size * 2]
part3 = arr[size * 2:]

# Her parçayı sırala
merge_sort(part1)
merge_sort(part2)
merge_sort(part3)

# Her parçanın sıralanmış hallerini yazdır
print("Parça 1: ", part1)
print("Parça 2: ", part2)
print("Parça 3: ", part3)

# Sıralanmış parçaları birleştirip ve yazdırma
result = merge_sort(part1 + part2 + part3)
print("Çıktı: ", result)