with open(r'C:\Users\Acer\PycharmProjects\KEGE20261\Task26\Files\26_12113.txt') as file:
    N = int(file.readline())
    boxes = [int(i) for i in file]

boxes = sorted(boxes, reverse=True)

red_trajectory = [max(i for i in boxes if i % 2 == 1)]
blue_trajectory = [max(boxes, key=lambda x: (x % 2 == 0, x))]
for box in boxes:
    if red_trajectory[-1] % 2 != box % 2 and red_trajectory[-1] - box >= 7:
        red_trajectory.append(box)
    if blue_trajectory[-1] % 2 != box % 2 and blue_trajectory[-1] - box <= 7:
        blue_trajectory.append(box)

print('Ответ:', len(red_trajectory), red_trajectory[-1])
print(len(blue_trajectory), blue_trajectory[-1])
