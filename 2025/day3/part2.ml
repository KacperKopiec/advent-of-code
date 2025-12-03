let filename = "day3/input.in"
let input = Advent.read_lines filename |> List.map String.to_seq

let new12 n d = 
  let rec aux ans iter =
    if iter < 0 then ans
    else
      let left = n / (Advent.pow 10 (iter + 1)) in
      let mid = n / (Advent.pow 10 (iter)) mod 10 in
      let right = n - left * (Advent.pow 10 (iter + 1)) - mid * (Advent.pow 10 iter) in
      let num = (left * (Advent.pow 10 (iter)) + right) * 10 + d in
      aux (max ans num) (iter - 1)
  in
  aux n 11

let solve seq = 
  let rec aux ans seq =
    match seq () with
    | Seq.Nil -> ans
    | Seq.Cons (x, xs) ->
      let n = int_of_char x - int_of_char '0' in 
      let ans = new12 ans n in 
      aux ans xs
  in
  aux 0 seq

let () = 
  List.map solve input 
  |> List.fold_left ( + ) 0 
  |> Printf.printf "%d\n"