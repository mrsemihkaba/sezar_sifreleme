# Sezar Şifrelemesi

Bu Python programı, kullanıcıya metinleri şifrelemek ve şifrelenmiş metinleri çözmek için Sezar şifrelemesi yöntemini sunar.

## Fonksiyonlar

### caesar_sifreleme(metin, kaydirma_miktari)

Bu fonksiyon, verilen metni belirtilen kaydırma miktarıyla Sezar şifresine göre şifreler.

- `metin`: Şifrelemek istediğiniz metin.
- `kaydirma_miktari`: Şifreleme için kullanılacak kaydırma miktarı.

#### Örnek Kullanım

```python
sifreli_metin = caesar_sifreleme("Merhaba, dunya!", 3)
print("Şifreli metin:", sifreli_metin)
```
### caesar_sifre_coz(metin, kaydirma_miktari)

Bu fonksiyon, verilen şifreli metni belirtilen kaydırma miktarıyla Sezar şifresine göre çözer.

- `metin`: Şifrelemek istediğiniz metin.
- `kaydirma_miktari`: Şifreleme için kullanılacak kaydırma miktarı.

```python
orijinal_metin = caesar_sifre_coz("Phuudb, gxqnd!", 3)
print("Orijinal metin:", orijinal_metin)
```

## Kurulum

1. Projeyi klonlayın veya indirin:

```bash
https://github.com/mrsemihkaba/sezar_sifreleme.git
```
2. Proje dizinine gidin:
```bash
cd sezar_sifreleme
```
3. Programı çalıştırın:
```bash
python3 sezar_sifreleme.py
```
