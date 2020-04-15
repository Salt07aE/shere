import pprint

class numpre2():
    def main():
        print("="*20)
        number = [
            [0, 0, 5, 3, 0, 0, 0, 0, 0], 
            [8, 0, 0, 0, 0, 0, 0, 2, 0], 
            [0, 7, 0, 0, 1, 0, 5, 0, 0], 
            [4, 0, 0, 0, 0, 5, 3, 0, 0], 
            [0, 1, 0, 0, 7, 0, 0, 0, 6], 
            [0, 0, 3, 2, 0, 0, 0, 8, 0], 
            [0, 6, 0, 5, 0, 0, 0, 0, 9], 
            [0, 0, 4, 0, 0, 0, 0, 3, 0], 
            [0, 0, 0, 0, 0, 9, 7, 0, 0]]

        def width(number, target_height):
            exist = [1,2,3,4,5,6,7,8,9]
            result = []
            for target_width in range(9):
                for search in range(1,10):
                    if number[target_height][target_width] == search:
                        if exist.count(search) == 0:
                            break
                        exist.remove(search)

            for target in range(9):
                if number[target_height][target] != 0:
                    result.append([number[target_height][target]])
                else:
                    result.append(exist)
            return (result)

        def height(number, target_width):
            exist = [1,2,3,4,5,6,7,8,9]
            result = []
            for target_height in range(9):
                for search in range(1,10):
                    if number[target_height][target_width] == search:
                        if exist.count(search) == 0:
                            break
                        exist.remove(search)

            for target in range(9):
                if number[target][target_width] != 0:
                    result.append([number[target][target_width]])
                else:
                    result.append(exist)
                
            return (result)

        def square(number, target_square):
        target_height = ([[0,1,2]]*3 + [[3,4,5]]*3 + [[6,7,8]]*3)
        target_width = [[0,1,2],[3,4,5],[6,7,8]]*3
        exist = [1,2,3,4,5,6,7,8,9]
        result = []
        for i in target_height[target_square]:
            for j in target_width[target_square]:
                for search in range(1,10):
                    if number[i][j] == search:
                        if exist.count(search) == 0:
                            break
                        exist.remove(search)

        for i in target_height[target_square]:
            for j in target_width[target_square]:
                if number[i][j] != 0:
                    result.append([number[i][j]])
                else:
                    result.append(exist)

        return (result)