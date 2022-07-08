$('.seat').ready(function(){
  let seats = $('.seats').attr('seats')
  let seats_taken = $('.seats').attr('seats_taken')

  showSeats(seats)
  markRowNumbers()
  markTakenSeats(seats_taken)
});

function markRowNumbers(){
  for (let i = 1; i <= $(".row").length; i++) {
    rowNumberId = "#row-number" + i;
    console.log('yes')
    $(rowNumberId).html(i)
  }
}

function showSeats(seats){
  seats = seats.split(";");
  // console.log(seats)
  for (seat_line of seats) {
    split_ = seat_line.split('_')
    let row = split_[0]
    let col_start = parseInt(split_[1].split(':')[0])
    let col_end = parseInt(seat_line.split(':')[1])
    for (let i = col_start; i <= col_end; i++) {
      let seat_id = '#' + row + '_' + i
      $(seat_id).css("opacity", 1);
      $(seat_id).css("pointer-events", 'auto');
    }
  }
}

function markTakenSeats(taken_seats){
  for (seat of taken_seats.split(';')) {
    let seat_id = '#' + seat
    $(seat_id).addClass('seat-taken')
    $(seat_id).css("pointer-events", 'none');
    }
}

//   }
// }

var seats_taken_new = []
var seats_string = ''
var link = $('#submit-btn').attr('data-href')
console.log(link)
console.log('hereeeeeeee')
function chooseSeat(seat_id){
  $(seat_id).toggleClass('seat-chosen')
  let seats_taken = $('#id_seats_taken').val()
  seat_id = seat_id.split('#')[1]
  if (!seats_taken.split(';').includes(seat_id)){
    seats_taken_new.push(seat_id)
    $('#id_seats_taken').val(seats_taken + seat_id + ';')
  } else{
    seats_taken = seats_taken.split(';')
    let index = seats_taken.indexOf(seat_id, 0)
    let index_new = seats_taken_new.indexOf(seat_id, 0)
    seats_taken.splice(index, 1)
    seats_taken_new.splice(index_new, 1)
    $('#id_seats_taken').val(seats_taken.join(';'))
    seats_taken = seats_taken.join(';')
  }

  let href = $('#id_seats_taken').val()
  // link = href
  $('#submit-btn').attr('data-href', link)
  seats_string = ''
  for (seat of seats_taken_new){
    seats_string += '<li>row ' + seat.split('_')[0] + ' seat ' + seat.split('_')[1] + '</li>'
  }
  $('#seats-chosen').html(seats_string)
  if (seats_taken_new.length == 0){
    $('#none-chosen').css({'display': 'block'})
    $('#seats-chosen').html('<li id="none-chosen">None choosen </li>')
  } else {
    $('#none-chosen').css({'display': 'none'})
  }
}

function book_seats(){
  $.ajax({
    url: link,
    method: "get",
    data: {'seats_taken': $('#id_seats_taken').val()},
    success: (data) => {
      console.log(data);
    },
    error: (data) => {
      console.log(link);
    }

  }),
  // $('#none-chosen').css({'display': 'block'})
  $('#seats-chosen').html('<li id="none-chosen">None choosen </li>')
  markTakenSeats(seats_taken_new.join(';'))
  seats_taken_new = []
}
