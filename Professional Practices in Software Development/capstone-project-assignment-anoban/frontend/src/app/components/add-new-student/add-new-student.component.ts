import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from 'src/app/app-service.service';

@Component({
  selector: 'app-add-new-student',
  templateUrl: './add-new-student.component.html',
  styleUrls: ['./add-new-student.component.css']
})
export class AddNewStudentComponent implements OnInit {

  constructor(private service : AppServiceService, private router: Router) { }

  ngOnInit(): void {
  }

  createStudent(value){

    const student = {
      id : value.id,
      name : value.name,
      age : value.age,
      hometown : value.Hometown
    }


    this.service.addStudent(student).subscribe((response)=>{
      this.router.navigate(['student'])
    },(error)=>{
      console.log('ERROR - ', error)
    })
  }

}
