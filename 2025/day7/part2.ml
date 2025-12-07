let filename = "day7/input.in"

let lines = Advent.read_lines filename

let solve =
  let line = List.hd lines |> String.to_seq |> Array.of_seq |> Array.map (fun c -> if c = 'S' then 1 else 0) in
  let rest_lines = List.tl lines |> List.map (fun line -> List.of_seq (String.to_seq line)) in
  let rec parse index lst =
    match lst with
    | [] -> ()
    | x :: xs ->
      if x = '^' then (
        if line.(index) > 0 then (
          line.(index - 1) <- line.(index - 1) + line.(index);
          line.(index + 1) <- line.(index + 1) + line.(index);
          line.(index) <- 0;
        )
      ); parse (index + 1) xs
  in
  List.iter (parse 0) rest_lines;
  Array.fold_left ( + ) 0 line

let () =
  solve
  |> Printf.printf "%d\n"