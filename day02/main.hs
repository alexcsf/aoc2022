shapeValue :: Char -> Int
shapeValue 'X' = 1
shapeValue 'Y' = 2
shapeValue 'Z' = 3
shapeValue _ = 0

outcome :: Char -> Char -> Int
outcome 'A' 'X' = 3
outcome 'A' 'Y' = 6
outcome 'A' 'Z' = 0
outcome 'B' 'X' = 0
outcome 'B' 'Y' = 3
outcome 'B' 'Z' = 6
outcome 'C' 'X' = 6
outcome 'C' 'Y' = 0
outcome 'C' 'Z' = 3
outcome _ _ = 0

choose :: Char -> Char -> Char
choose 'A' 'X' = 'Z'
choose 'A' 'Y' = 'X'
choose 'A' 'Z' = 'Y'
choose 'B' 'X' = 'X'
choose 'B' 'Y' = 'Y'
choose 'B' 'Z' = 'Z'
choose 'C' 'X' = 'Y'
choose 'C' 'Y' = 'Z'
choose 'C' 'Z' = 'X'
choose _ _ = '.'

part1 :: String -> Int
part1 (x:_:y:_) = shapeValue y + outcome x y
part1 _ = 0

part2 :: String -> Int
part2 (x:_:y:_) = let z = choose x y in shapeValue z + outcome x z
part2 _ = 0

main :: IO()
main = do
    contents <- readFile "day02/input.txt"
    putStrLn $ "1: " ++ show (sum $ map part1 $ lines contents)
    putStrLn $ "2: " ++ show (sum $ map part2 $ lines contents)
