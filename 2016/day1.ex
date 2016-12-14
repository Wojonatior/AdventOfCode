defmodule ProblemInput do
  defp read_file(filename) do
    File.read!(filename)
  end
  
  def readAndParse(filename) do
    fileAsString = read_file(filename)
    parsedInput = Regex.split(~r/, /, fileAsString)
  end
end

defmodule Compass do
  def init do
    {:ok, _} = Agent.start_link(fn -> [[0,1], [1,0], [0,-1], [-1,0]] end, name: :compass)
  end

  defp turn(:left) do
      Agent.get_and_update :compass,
        fn (directionList) ->
          [a, b, c, d] = directionList
          {[d, a, b, c], [d, a, b, c]}
        end
  end

  defp turn(:right) do
      Agent.get_and_update :compass,
        fn(directionList) ->
          [head | tail] = directionList
          {tail ++ [head], tail ++ [head]}
        end
  end

  def turnAndGetMove(scalarDistance, turnDir) do
    #Scalar distance = 5
    #Cartesian = {0,0} at start
    #Direction = {1,0} or something
    # I want to return {5,0}
    [direction|_] = turn(turnDir)
    Enum.map(direction, fn (coord) -> scalarDistance * coord end)
  end

  def moveDistance(current, move) do
    [xCurr, yCurr] = current
    [xMov, yMov] = move
    [xCurr+xMov, yCurr+yMov]
  end

  def getManhattanDistance(coords) do
    [xCurr, yCurr] = coords
    Kernel.abs(xCurr) + Kernel.abs(yCurr)
  end

  def walkInputAndSolve(input) do
    [currentMove | remainingMoves] = input
    case currentMove do
      ["R", distance] ->
        distanceToMove = turnAndGetMove(distance, :right)
      ["L", distance] ->
        distanceToMove = turnAndGetMove(distance, :left)
    end
  end
end
    



{:ok, _} = Compass.init()

coordinates = [0,0]
problemInput = ProblemInput.readAndParse("day1input.txt")
result = Compass.walkInputAndSolve(problemInput)
IO.inspect result

#move = Compass.turnAndGetMove(5, :right)
#coordinates = Compass.moveDistance(coordinates, move)
#IO.inspect(coordinates, char_lists: false)
#move = Compass.turnAndGetMove(5, :left)
#coordinates = Compass.moveDistance(coordinates, move)
#IO.inspect(coordinates, char_lists: false)
#move = Compass.turnAndGetMove(5, :right)
#coordinates = Compass.moveDistance(coordinates, move)
#IO.inspect(coordinates, char_lists: false)
#move = Compass.turnAndGetMove(5, :left)
#coordinates = Compass.moveDistance(coordinates, move)
#IO.inspect(coordinates, char_lists: false)
#IO.inspect(Compass.getManhattanDistance(coordinates), char_lists: false)
