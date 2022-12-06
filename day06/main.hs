packetMarker :: Int -> String -> Int
packetMarker n = packetMarker' n n
packetMarker' :: Int -> Int -> String -> Int
packetMarker' n k xs
    | distinctChars $ take n xs = k
    | otherwise = packetMarker' n (k + 1) (tail xs)

distinctChars :: String -> Bool
distinctChars (x:xs) = x `notElem` xs && distinctChars xs
distinctChars _ = True

main :: IO()
main = do
    contents <- init <$> readFile "day06/input.txt"
    putStrLn $ "1: " ++ show (packetMarker 4 contents)
    putStrLn $ "2: " ++ show (packetMarker 14 contents)
