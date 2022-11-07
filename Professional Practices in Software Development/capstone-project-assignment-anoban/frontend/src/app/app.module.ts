import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { StudentTableComponent } from './components/student-table/student-table.component';
import { TeacherTableComponent } from './components/teacher-table/teacher-table.component';
import { AddNewTeacherComponent } from './components/add-new-teacher/add-new-teacher.component';
import { AddNewStudentComponent } from './components/add-new-student/add-new-student.component';
import { EditStudentComponent } from './components/edit-student/edit-student.component';
import { EditTeacherComponent } from './components/edit-teacher/edit-teacher.component';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    StudentTableComponent,
    TeacherTableComponent,
    AddNewTeacherComponent,
    AddNewStudentComponent,
    EditStudentComponent,
    EditTeacherComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FontAwesomeModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
