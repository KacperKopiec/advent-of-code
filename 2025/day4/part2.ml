let filename = "day4/input.in"
let grid = Advent.read_lines filename |> Array.of_list |> Array.map (fun s -> Array.of_seq (String.to_seq s))

let count_neightbours grid i j =
  Seq.fold_left (fun acc (y, x) -> acc + if grid.(y).(x) = '@' then 1 else 0) 0 (Advent.neighbours grid i j Advent.all_directions)

let solve grid =
  let rows = Array.length grid in
  let cols = Array.length grid.(0) in
  let count = ref 0 in
  let q = Queue.create () in
  for i = 0 to rows - 1 do
    for j = 0 to cols - 1 do
      if grid.(i).(j) = '@' && count_neightbours grid i j < 4 then (
        incr count;
        grid.(i).(j) <- '.';
        Queue.push (i, j) q
      )
    done
  done;
  
  while not (Queue.is_empty q) do
    let y, x = Queue.pop q in
    Seq.iter (fun (ny, nx) -> 
      if grid.(ny).(nx) = '@' && count_neightbours grid ny nx < 4 then (
        incr count;
        grid.(ny).(nx) <- '.';
        Queue.push (ny, nx) q
      )
    ) (Advent.neighbours grid y x Advent.all_directions)
  done;
  !count

let () =
  solve grid 
  |> Printf.printf "%d\n"