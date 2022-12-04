import Data.List (elemIndex)
import Data.Bifunctor (bimap)

splitOn :: (Eq a, Show a) => a -> [a] -> ([a], [a])
splitOn d xs = case elemIndex d xs of
    (Just i) -> let (x, _:y) = splitAt i xs in (x, y)
    _ -> error $ "Error splitting list on " ++ show d

subsetOf :: Ord a => (a, a) -> (a, a) -> Bool
subsetOf (x1, y1) (x2, y2) = x1 >= x2 && y1 <= y2

overlaps :: Ord a => (a, a) -> (a, a) -> Bool
overlaps (x1, y1) (x2, _) = x1 <= x2 && x2 <= y1

readInts :: (String, String) -> (Int, Int)
readInts = bimap read read

main :: IO()
main = do
    contents <- fmap lines (readFile "day04/input.txt")
    let xs = map (bimap (readInts . splitOn '-') (readInts . splitOn '-') . splitOn ',') contents
    putStrLn $ "1: " ++ show (length $ filter (\(a, b) -> a `subsetOf` b || b `subsetOf` a) xs)
    putStrLn $ "2: " ++ show (length $ filter (\(a, b) -> a `overlaps` b || b `overlaps` a) xs)
