let filename = "day7/input.in"

let lines = Advent.read_lines filename

let solve =
  let line = List.hd lines |> String.map (fun c -> if c = 'S' then '|' else c) |> String.to_seq |> Array.of_seq in
  let rest_lines = List.tl lines |> List.map (fun line -> List.of_seq (String.to_seq line)) in
  let ans = ref 0 in
  let rec parse index lst =
    match lst with
    | [] -> ()
    | x :: xs ->
      if x = '^' then (
        if line.(index) = '|' then (
          incr ans;
          line.(index - 1) <- '|';
          line.(index) <- '.';
          line.(index + 1) <- '|'
        )
      ); parse (index + 1) xs
  in
  List.iter (parse 0) rest_lines;
  !ans

let () =
  solve
  |> Printf.printf "%d\n"