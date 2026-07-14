class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        cars = []
        for i in range(0,len(position)):
            cars.append([position[i],speed[i],((target-position[i])/speed[i])])
        sorted_cars = sorted(cars, key=lambda x: x[0], reverse=True)
        lead_car_time = sorted_cars[0][2]

        for c in sorted_cars:
            print(c[2],".")
            if lead_car_time >= c[2]:
                continue
            else:
                fleets+=1
                lead_car_time = c[2]
            print(lead_car_time)
        return fleets

             
        