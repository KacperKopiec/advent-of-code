let filename = "day3/input.in"
let input = Advent.read_lines filename |> List.map String.to_seq

let solve seq = 
  let rec aux ans prv seq =
    match seq () with
    | Seq.Nil -> ans
    | Seq.Cons (x, xs) -> let n = int_of_char x - int_of_char '0' in aux (max ans (prv * 10 + n)) (max prv n) xs
  in
  aux 0 0 seq

let () = 
  List.map solve input 
  |> List.fold_left ( + ) 0 
  |> Printf.printf "%d\n"