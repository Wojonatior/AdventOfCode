main do
	import Data.List

	n `quotCeil` d = (n-1) `quot` d + 1

	hits health damage = health `quotCeil` max 1 damage

	weapons = zip [8,10,25,40,74] $ zip [4..] (repeat 0)
	armor = zip [13,31,53,75,102] $ zip (repeat 0) [1..]
	rings = zip [25,50,100,20,40,80] $ zip [1,2,3,0,0,0] [0,0,0,1,2,3]

	loadouts = [ [w,a]++rs
		| w <- weapons, a <- (0,(0,0)) : armor
		, rs <- filter ((<=2).length) $ subsequences rings ]

	playerHP = 100
	bossHP = 103
	bossDmg = 9
	bossArm = 2

	cost = sum . map fst
	dmg = sum . map (fst . snd)
	arm = sum . map (snd . snd)

	viable items =
		hits bossHP (dmg items - bossArm) <= hits playerHP (bossDmg - arm items)
	part1 = minimum . map cost . filter viable $ loadouts
	part2 = maximum . map cost . filter (not . viable) $ loadouts