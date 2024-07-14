import I2C_LCD_driver
from time import sleep

# Создайте объект LCD
lcd = I2C_LCD_driver.lcd()

# Вывод текста на дисплей
lcd.lcd_display_string("Hello, World!", 1)
lcd.lcd_display_string("Raspberry Pi", 2)

sleep(5)  # Подождите 5 секунд
lcd.lcd_clear()  # Очистите дисплей
 