allure_normal = 495
allure_soutenu = 432

heure = 6
minute = 52
seconde = 0

temps_parcouru = (allure_normal * 2) + (allure_soutenu * 3)

temps_parcouru_min = (temps_parcouru // 60)


h = temps_parcouru_min // 60
m = temps_parcouru_min % 60
s = (temps_parcouru % 60)

print('temps parcouru:  ', h, 'h', m, 'm', s, 's')
print('il rentre à: ', heure + h + (minute + m) // 60,'h ',(minute + m) % 60,"m", seconde + s, 's' )