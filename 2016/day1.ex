defmodule Somefile do
  def get_filename() do
    IO.gets("Input filename:") |> String.trim
  end

  def read_file() do
    File.read!(get_filename)
  end
end

defmodule compass do
  def init do
    Task.start_link(fn -> loop([{0,1}, {1,0}, {0,-1}, {-1,0}]) end)
  end

  defp loop(directions) 
    receive do
      {:get, caller} ->
        send caller, hd(directions)
        loop(directions)
      {:turn, :left, caller} ->
        [1| [2 | [3 | 4]]] = directions
        loop(4 ++ 1 ++ 2 ++ 3)
      {:turn, :right, caller} ->
        [head | tail] = directions
        loop(tail ++ head)


{:ok, pid} = Compass.init
Process.register(pid, :compass)
coordinates = {0,0}
file = Somefile.read_file


