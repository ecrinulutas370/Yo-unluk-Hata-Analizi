import math

def prizma_yogunluk_ve_hata(m, a, b, c, delta_m=0.01, delta_boyut=0.001):
    """
    Kütle gram (g), boyutlar santimetre (cm) cinsinden girilmelidir.
    delta_m: Terazinin hata payı (0.01 g)
    delta_boyut: Kumpasın hata payı (Örn: 0.01 mm = 0.001 cm)
    """
    # Hacim hesaplama (V = a * b * c)
    V = a * b * c
    # Yoğunluk hesaplama (rho = m / V)
    rho = m / V
    
    # Bağıl Hata (Relative Error) Hesabı: d_rho/rho = d_m/m + d_a/a + d_b/b + d_c/c
    bagil_hata = (delta_m / m) + (delta_boyut / a) + (delta_boyut / b) + (delta_boyut / c)
    
    # Mutlak Hata (Absolute Error) Hesabı: d_rho = rho * bagil_hata
    mutlak_hata = rho * bagil_hata
    
    return rho, mutlak_hata, bagil_hata

def silindir_yogunluk_ve_hata(m, r, h, delta_m=0.01, delta_boyut=0.001):
    """
    Kütle gram (g), yarıçap ve yükseklik santimetre (cm) cinsinden girilmelidir.
    """
    # Hacim hesaplama (V = pi * r^2 * h)
    V = math.pi * (r ** 2) * h
    # Yoğunluk hesaplama (rho = m / V)
    rho = m / V
    
    # Bağıl Hata Hesabı: d_rho/rho = d_m/m + 2*(d_r/r) + d_h/h
    bagil_hata = (delta_m / m) + 2 * (delta_boyut / r) + (delta_boyut / h)
    
    # Mutlak Hata Hesabı
    mutlak_hata = rho * bagil_hata
    
    return rho, mutlak_hata, bagil_hata

# ---- ÖRNEK KULLANIM ----
if __name__ == "__main__":
    print("--- 1. DİKDÖRTGEN PRİZMA HESABI ---")
    # Örnek Ölçümler (m=150g, a=2cm, b=3cm, c=5cm)
    m_p, a_p, b_p, c_p = 150.0, 2.0, 3.0, 5.0
    rho_p, mutlak_p, bagil_p = prizma_yogunluk_ve_hata(m_p, a_p, b_p, c_p)
    
    print(f"Yoğunluk: {rho_p:.4f} g/cm³")
    print(f"Mutlak Hata: ±{mutlak_p:.4f} g/cm³")
    print(f"Bağıl Hata: %{bagil_p * 100:.2f}\n")

    print("--- 2. SİLİNDİR HESABI ---")
    # Örnek Ölçümler (m=200g, r=1.5cm, h=6cm)
    m_s, r_s, h_s = 200.0, 1.5, 6.0
    rho_s, mutlak_s, bagil_s = silindir_yogunluk_ve_hata(m_s, r_s, h_s)
    
    print(f"Yoğunluk: {rho_s:.4f} g/cm³")
    print(f"Mutlak Hata: ±{mutlak_s:.4f} g/cm³")
    print(f"Bağıl Hata: %{bagil_s * 100:.2f}")
