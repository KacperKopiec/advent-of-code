open Z3

let filename = "day10/input.in"

let parse lst = 
  let parse_voltages s =
    String.sub s 1 (String.length s - 2)
    |> String.split_on_char ','
    |> List.map int_of_string
    |> Array.of_list
  in
  let parse_button s =
    String.sub s 1 (String.length s - 2)
    |> String.split_on_char ','
    |> List.map int_of_string
  in
  let parse_buttons lst = List.map parse_button lst in
  let first = List.hd lst in
  let last = List.hd (List.rev lst) in
  let mid = List.tl lst |> List.rev |> List.tl in
  (first, parse_buttons mid, parse_voltages last)

let lines = Advent.read_lines filename |> List.map(fun s -> parse (String.split_on_char ' ' s))

let make_matrix buttons num_voltages =
  Array.init num_voltages (fun row ->
    Array.init (List.length buttons) (fun col ->
      if List.mem row (List.nth buttons col) then 1 else 0
    )  
  )

let solve buttons voltages =
  let m = Array.length voltages in
  let n = List.length buttons in
  let a = make_matrix buttons m in
  let ctx = mk_context [("model", "true")] in
  let opt = Optimize.mk_opt ctx in
  let xs = 
    Array.init n (fun i ->
      Arithmetic.Integer.mk_const_s ctx (Printf.sprintf "x_%d" i)
    )
  in
  for row = 0 to m - 1 do
    let sum_terms = ref [] in
    for col = 0 to n - 1 do
      if a.(row).(col) = 1 then
        sum_terms := xs.(col) :: !sum_terms
    done;
    let lhs = Arithmetic.mk_add ctx !sum_terms in
    let rhs = Arithmetic.Integer.mk_numeral_i ctx voltages.(row) in
    let eq = Boolean.mk_eq ctx lhs rhs in
    Optimize.add opt [eq];
  done;

  let zero = Arithmetic.Integer.mk_numeral_i ctx 0 in
  for i = 0 to n - 1 do
    let ge = Arithmetic.mk_ge ctx xs.(i) zero in
    Optimize.add opt [ge]
  done;

  let objective = Arithmetic.mk_add ctx (Array.to_list xs) in
  ignore (Optimize.minimize opt objective);

  match Optimize.check opt with
  | SATISFIABLE ->
      let model_opt = Optimize.get_model opt in
      (match model_opt with
      | None -> failwith "No model returned"
      | Some m ->
          Array.init n (fun i ->
            match Model.eval m xs.(i) true with
            | Some v -> int_of_string (Expr.to_string v)
            | None -> failwith "Incomplete model"
          )
      )
  | _ -> failwith "Invalid input"

let () =
  List.fold_left (fun acc (_, buttons, voltages) -> acc + Array.fold_left ( + ) 0 (solve buttons voltages)) 0 lines
  |> Printf.printf "%d\n"