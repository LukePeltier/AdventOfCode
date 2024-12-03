let string_of_int_list = [%show: int list]
let string_of_tuple_list = [%show: (int * int) list]

let frequencies list =
  let tbl = Hashtbl.create (List.length list) in
  List.iter
    (fun x ->
      Hashtbl.replace tbl x (1 + try Hashtbl.find tbl x with Not_found -> 0))
    list;
  tbl
