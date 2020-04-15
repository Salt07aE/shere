import pprint

class numpre():
    def main():
        print("\nPhase【1】")
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

        phase1 = numpre.phase1(number)
        x = phase1[0]
        flag = phase1[1]
        result_all = phase1[2]
        print(x,flag)
        pprint.pprint(result_all)

        


    def phase1(number):
        x = 0
        for i in number:
            x += i.count(0)
        pprint.pprint(number)
        print(x)

        flag = 0
        back_flag = 0
        count = 1
        log = []
        
        while x > 0:
            result_al = []
            result_all = []
            target_square_s = [[0]*3 + [1]*3 + [2]*3]*3 + [[3]*3 + [4]*3 + [5]*3]*3  + [[6]*3 + [7]*3 + [8]*3]*3
            target_square_a = ([[0,1,2]*3] + [[3,4,5]*3] + [[6,7,8]*3])*3
            for i in range(9):
                for j in range(9):
                    result1 = numpre.width(number, i)
                    result = result1[j]

                    result2 = numpre.height(number, j)
                    result += result2[i]

                    result3 = numpre.square(number, target_square_s[i][j])
                    result += result3[target_square_a[i][j]]

                    result = [i for i in set(result) if result.count(i) > 2]
                    result_al.append(result)

                result_all.append(result_al)
                result_al = []
            
            for i in range(9):
                for j in range(9):
                    if len(result_all[i][j]) == 1:
                        number[i][j] = result_all[i][j][0]
            
            pprint.pprint(number)
            x = 0
            for i in number:
                x += i.count(0)
            if log == x:
                flag = 1
                print(x)
                print(count)
                break
            print(x)
            log = x
            print(count)
            count += 1
        
        return (x, flag, result_all)


                


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



numpre.main()