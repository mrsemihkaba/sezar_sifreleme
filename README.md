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
