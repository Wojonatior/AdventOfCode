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

  def getAllIntersections(move, current, intersections) do
    IO.inspect move
    if move == [0,0] do
      intersections
    else
      [xCurr, yCurr] = current
      [xMov, yMov] = move
      {xMov, xCurr} = if xMov > 0 do
        {xMov - 1, xCurr + 1}
      else
        {xMov, xCurr}
      end
      {yMov, yCurr} = if yMov > 0 do
        {yMov - 1, yCurr + 1}
      else
        {yMov, yCurr}
      end
      current = [xCurr, yCurr]
      move = [xMov, yMov]
      Map.put(intersections, String.to_atom(List.to_string(current)), true)
      getAllIntersections(move, current, intersections)
    end
  end

  def walkInputAndSolve(input, currentCoordinates, intersections) when input == [] do
    { getManhattanDistance(currentCoordinates), intersections }
  end

  def walkInputAndSolve(input, currentCoordinates, intersections) do
    [currentMove | remainingMoves] = input
    direction = String.at(currentMove, 0)
    distance = currentMove |> String.trim |> String.slice( 1, 4) 
    dirAtom =
      if direction == "L" do
        :left
      else #direction == "R" do
        :right
      end
    distToMove = turnAndGetMove(String.to_integer(distance), dirAtom)
    endCoordinates = moveDistance(currentCoordinates, distToMove)
    #intersections = getAllIntersections(distToMove, currentCoordinates, intersections)
    walkInputAndSolve(remainingMoves, endCoordinates, intersections)
  end
end
    



{:ok, _} = Compass.init()

problemInput = ProblemInput.readAndParse("day1input.txt")
result = Compass.walkInputAndSolve(problemInput, [0,0], %{})
IO.inspect result
