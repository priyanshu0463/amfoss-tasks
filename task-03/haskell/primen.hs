isPrime :: Int -> Bool
isPrime n
    | n <= 1    = False
    | otherwise = all (\x -> n `mod` x /= 0) [2..(n - 1)]

main :: IO ()
main = do
    putStrLn "Enter a number: "
    input <- getLine
    let x = read input :: Int
    putStrLn "Prime numbers:"
    mapM_ (\i -> if isPrime i then putStrLn (show i ++ " : prime") else return ()) [1..x]
