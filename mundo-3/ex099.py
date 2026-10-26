from time import sleep

def maior(* nums):
    m = nums[0] if len(nums) > 0 else 0
    print('-='*15)
    print('Analisando os valores passados...')
    for num in nums:
        print(num, end=' ')
        if num > m:
            m = num
        sleep(0.25)
    print(f'Foram informados {len(nums)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()