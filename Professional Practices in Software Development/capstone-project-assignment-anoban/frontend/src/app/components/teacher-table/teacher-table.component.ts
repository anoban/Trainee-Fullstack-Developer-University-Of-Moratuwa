import { Component, OnInit } from '@angular/core';
import { Router, NavigationExtras } from '@angular/router';
import { faTrash, faPlus, faPenSquare } from '@fortawesome/free-solid-svg-icons';
import { AppServiceService } from '../../app-service.service';
@Component({
  selector: 'app-teacher-table',
  templateUrl: './teacher-table.component.html',
  styleUrls: ['./teacher-table.component.css']
})
export class TeacherTableComponent implements OnInit {

  faTrash = faTrash;
  faPlus = faPlus;
  faPenSquare = faPenSquare;
  teacherData: any;
  selected: any;

  constructor(private service: AppServiceService, private router: Router) { }

  ngOnInit(): void {
    this.getTeacherData();
  }

  addNewTeacher() {
    this.router.navigate(['addTeacher'])
  }

  editTeacher(id) {
    const navigationExtras: NavigationExtras = {
      state: {
        id: id
      }
    };
    this.router.navigate(['editTeacher'], navigationExtras)
  }

  initializeDB(){
    this.service.initializeDB().subscribe((response) => {
      console.log('DB is Initialized')
    }, (error) => {
      console.log('ERROR - ', error)
    })
  }

  getTeacherData() {
    this.selected = 'Teachers';
    this.service.getTeacherData().subscribe((response) => {
      this.teacherData = Object.keys(response).map((key) => [response[key]]);
    }, (error) => {
      console.log('ERROR - ', error)
    })
  }

  getStudentData() {
    this.selected = 'Students';
    this.service.getStudentData().subscribe((response) => {
      this.teacherData = response;
    }, (error) => {
      console.log('ERROR - ', error)
    })
  }

  search(value) {
    let foundItems = [];
    if (value.length <= 0) {
      this.getTeacherData();
    } else {
      let b = this.teacherData.filter((teacher) => {
        if (teacher[0].name.toLowerCase().indexOf(value) > -1) {
          foundItems.push(teacher)
        }
      });
      this.teacherData = foundItems;
    }
  }

  deleteTeacher(itemid) {
    const test = {
      id: itemid
    }
    this.service.deleteTeacher(test).subscribe((response) => {
      this.getTeacherData()
    })
  }
}