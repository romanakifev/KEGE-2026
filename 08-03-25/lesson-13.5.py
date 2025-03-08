# Убирает определенные символы в начале и в конце строки
data = '**ivanov ivanovitch***'
print(data.strip('*'))
print(data.rstrip('*'))
print(data.lstrip('*'))
