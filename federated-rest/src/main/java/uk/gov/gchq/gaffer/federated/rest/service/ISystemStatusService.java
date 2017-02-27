/*
 * Copyright 2016-2017 Crown Copyright
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package uk.gov.gchq.gaffer.federated.rest.service;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import uk.gov.gchq.gaffer.federated.rest.dto.FederatedSystemStatus;
import uk.gov.gchq.gaffer.federated.rest.dto.SystemStatus;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Response;

import static javax.ws.rs.core.MediaType.APPLICATION_JSON;

@Path("/")
@Produces(APPLICATION_JSON)
@Api(value = "/status", description = "Methods to check the status of the system.")
public interface ISystemStatusService {

    @GET
    @Path("/status")
    @ApiOperation(
            value = "Returns the status of the federated server",
            response = SystemStatus.class)
    @ApiResponses(
            value = {@ApiResponse(code = 200, message = "OK"),
                    @ApiResponse(code = 500, message = "Something wrong in Server")})
    Response status();

    @GET
    @Path("/statuses")
    @ApiOperation(
            value = "Returns the statuses of the child servers",
            response = FederatedSystemStatus.class,
            responseContainer = "List"
    )
    @ApiResponse(code = 207, message = "See individual statuses for more information")
    Response statuses();
}
