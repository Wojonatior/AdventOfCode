defmodule Somefile do
  def get_filename() do
    IO.gets("Input filename:") |> String.trim
  end

  def read_file() do
    File.read!(get_filename)
  end
end

defmodule Compass do
  def init do
    {:ok, _} = Agent.start_link(fn -> [[0,1], [1,0], [0,-1], [-1,0]] end, name: :compass)
  end

  def get() do
    Agent.get(:compass, fn(n) -> n end)
  end

  defp turn(:left) do
      Agent.get_and_update :compass,
        fn (directionList) ->
          [a, b, c, d] = directionList
          [d, a, b, c]
        end
  end

  defp turn(:right) do
      Agent.get_and_update :compass,
        fn(directionList) ->
          [head | tail] = directionList
          tail ++ [head]
        end
  end

  def getMove(scalarDistance) do
    #Scalar distance = 5
    #Cartesian = {0,0} at start
    #Direction = {1,0} or something
    # I want to return {5,0}
    IO.puts "getMove was called"
    
    [direction|_] = [[0,-1],[]]#get()
    IO.inspect direction
    IO.puts "You made this happen"
    Enum.map(direction, fn (coord) -> scalarDistance * coord end)
  end
end
    


{:ok, _} = Compass.init()

#coordinates = {0,0}
#file = Somefile.read_file

move = Compass.getMove(5)
IO.puts "Hello"
IO.inspect(move)
